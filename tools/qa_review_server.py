#!/usr/bin/env python3
from __future__ import annotations

import argparse
import html
import json
import re
import sys
import webbrowser
from dataclasses import dataclass, asdict
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
from pathlib import Path
from typing import Iterable
from urllib.parse import urlparse


QA_HEADING_RE = re.compile(r"^#### Q\d+ \(Source ID (?P<source_id>[^)]+)\): (?P<title>.+)$", re.MULTILINE)
SECTION_LABELS = [
    "Question 中文翻译",
    "Answer 中文翻译",
    "Draft optimized answer 中文（待审核）",
    "Draft optimized answer English (Pending review)",
    "Optimized answer 中文",
    "Optimized answer English",
    "Approved standard answer 中文",
    "Approved standard answer English",
    "Original question",
    "Original answer",
]


@dataclass
class QAItem:
    source_id: str
    title: str
    status: str
    question_zh: str
    answer_zh: str
    draft_zh: str
    draft_en: str
    original_question: str
    original_answer: str


def read_text(path: Path) -> str:
    return path.read_text(encoding="utf-8")


def write_text(path: Path, text: str) -> None:
    path.write_text(text, encoding="utf-8", newline="\n")


def iter_blocks(text: str) -> Iterable[tuple[re.Match[str], int, int]]:
    matches = list(QA_HEADING_RE.finditer(text))
    for index, match in enumerate(matches):
        start = match.start()
        end = matches[index + 1].start() if index + 1 < len(matches) else len(text)
        yield match, start, end


def extract_section(block: str, labels: list[str]) -> str:
    label_pattern = "|".join(re.escape(label) for label in SECTION_LABELS)
    for label in labels:
        pattern = re.compile(
            rf"\*\*{re.escape(label)}(?:[^*]*)?[：:]\*\*\s*\n\n(?P<body>.*?)(?=\n\*\*(?:{label_pattern})(?:[^*]*)?[：:]\*\*|\n#### Q|\n### |\n## |\Z)",
            re.DOTALL,
        )
        match = pattern.search(block)
        if match:
            return match.group("body").strip()
    return ""


def detect_status(block: str) -> str:
    if "**Approved standard answer 中文：**" in block or "**Approved standard answer English:**" in block:
        return "approved"
    return "pending"


def parse_items(text: str) -> list[QAItem]:
    items: list[QAItem] = []
    for match, start, end in iter_blocks(text):
        block = text[start:end]
        items.append(
            QAItem(
                source_id=match.group("source_id").strip(),
                title=match.group("title").strip(),
                status=detect_status(block),
                question_zh=extract_section(block, ["Question 中文翻译"]),
                answer_zh=extract_section(block, ["Answer 中文翻译"]),
                draft_zh=extract_section(
                    block,
                    ["Draft optimized answer 中文（待审核）", "Optimized answer 中文", "Approved standard answer 中文"],
                ),
                draft_en=extract_section(
                    block,
                    ["Draft optimized answer English (Pending review)", "Optimized answer English", "Approved standard answer English"],
                ),
                original_question=extract_section(block, ["Original question"]),
                original_answer=extract_section(block, ["Original answer"]),
            )
        )
    return items


def replace_answer_pair(block: str, zh: str, en: str, approved: bool) -> str:
    zh_label = "Approved standard answer 中文" if approved else "Draft optimized answer 中文（待审核）"
    en_label = "Approved standard answer English" if approved else "Draft optimized answer English (Pending review)"
    answer_pattern = re.compile(
        r"\n\*\*(?:Draft optimized answer 中文（待审核）|Optimized answer 中文|Approved standard answer 中文)：\*\*\s*\n\n"
        r".*?"
        r"\n\*\*(?:Draft optimized answer English \(Pending review\)|Optimized answer English|Approved standard answer English):\*\*\s*\n\n"
        r".*?"
        r"(?=\n\*\*Original question|\n#### Q|\n### |\Z)",
        re.DOTALL,
    )
    replacement = f"\n**{zh_label}：**\n\n{zh.strip()}\n\n**{en_label}:**\n\n{en.strip()}\n"
    new_block, count = answer_pattern.subn(replacement, block, count=1)
    if count != 1:
        raise ValueError("Could not find optimized answer block to replace")
    return new_block


def update_item(path: Path, source_id: str, zh: str, en: str, approved: bool = True) -> None:
    text = read_text(path)
    for match, start, end in iter_blocks(text):
        if match.group("source_id").strip() != source_id:
            continue
        block = text[start:end]
        updated = replace_answer_pair(block, zh, en, approved=approved)
        write_text(path, text[:start] + updated + text[end:])
        return
    raise ValueError(f"Source ID not found: {source_id}")


def normalize_draft_labels(path: Path) -> None:
    text = read_text(path)
    text = text.replace("**Optimized answer 中文：**", "**Draft optimized answer 中文（待审核）：**")
    text = text.replace("**Optimized answer English:**", "**Draft optimized answer English (Pending review):**")
    write_text(path, text)


def render_page() -> str:
    return r"""<!doctype html>
<html lang="zh-CN">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>QA Review Workbench</title>
  <style>
    :root { color-scheme: light; font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", sans-serif; }
    body { margin: 0; background: #f6f7f9; color: #1f2937; }
    header { position: sticky; top: 0; z-index: 2; background: #111827; color: #fff; padding: 14px 22px; display: flex; justify-content: space-between; align-items: center; }
    header h1 { margin: 0; font-size: 18px; }
    #stats { font-size: 14px; color: #d1d5db; }
    main { max-width: 1280px; margin: 20px auto; padding: 0 18px 40px; }
    .card { background: #fff; border: 1px solid #e5e7eb; border-radius: 12px; margin-bottom: 16px; overflow: hidden; box-shadow: 0 1px 2px rgba(0,0,0,.04); }
    .card-header { display: flex; gap: 12px; justify-content: space-between; align-items: center; padding: 14px 16px; border-bottom: 1px solid #e5e7eb; }
    .title { font-weight: 700; }
    .source { color: #6b7280; font-size: 13px; margin-right: 8px; }
    .badge { border-radius: 999px; padding: 4px 10px; font-size: 12px; font-weight: 700; background: #fef3c7; color: #92400e; }
    .badge.approved { background: #dcfce7; color: #166534; }
    .content { display: grid; grid-template-columns: 1fr 1fr; gap: 16px; padding: 16px; }
    .panel { min-width: 0; }
    textarea { width: 100%; min-height: 180px; box-sizing: border-box; border: 1px solid #d1d5db; border-radius: 8px; padding: 10px; font: 14px/1.5 ui-monospace, SFMono-Regular, Menlo, Consolas, monospace; resize: vertical; }
    label { display: block; font-weight: 700; margin: 10px 0 6px; }
    details { margin-top: 12px; background: #f9fafb; border: 1px solid #e5e7eb; border-radius: 8px; padding: 10px; }
    summary { cursor: pointer; font-weight: 700; }
    pre { white-space: pre-wrap; word-break: break-word; background: #fff; border: 1px solid #e5e7eb; padding: 10px; border-radius: 6px; }
    .actions { display: flex; justify-content: flex-end; gap: 10px; padding: 0 16px 16px; }
    button { border: 0; border-radius: 8px; padding: 9px 14px; cursor: pointer; font-weight: 700; }
    .approve { background: #2563eb; color: #fff; }
    .reload { background: #e5e7eb; color: #111827; }
    .msg { font-size: 13px; color: #2563eb; margin-right: auto; align-self: center; }
    @media (max-width: 900px) { .content { grid-template-columns: 1fr; } }
  </style>
</head>
<body>
  <header>
    <h1>QA 审核工作台</h1>
    <div id="stats">加载中...</div>
  </header>
  <main id="app"></main>
<script>
const app = document.querySelector('#app');
const stats = document.querySelector('#stats');

function escapeHtml(value) {
  return String(value || '').replace(/[&<>"']/g, ch => ({'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;',"'":'&#39;'}[ch]));
}

async function loadItems() {
  const res = await fetch('/api/items');
  if (!res.ok) throw new Error(await res.text());
  const data = await res.json();
  render(data.items);
}

function render(items) {
  const approved = items.filter(item => item.status === 'approved').length;
  stats.textContent = `总数 ${items.length}｜已通过 ${approved}｜待审核 ${items.length - approved}`;
  app.innerHTML = items.map(item => `
    <section class="card" data-source-id="${escapeHtml(item.source_id)}">
      <div class="card-header">
        <div><span class="source">Source ID ${escapeHtml(item.source_id)}</span><span class="title">${escapeHtml(item.title)}</span></div>
        <span class="badge ${item.status === 'approved' ? 'approved' : ''}">${item.status === 'approved' ? 'Approved' : 'Pending'}</span>
      </div>
      <div class="content">
        <div class="panel">
          <label>Draft / Approved answer 中文</label>
          <textarea class="zh">${escapeHtml(item.draft_zh)}</textarea>
        </div>
        <div class="panel">
          <label>Draft / Approved answer English</label>
          <textarea class="en">${escapeHtml(item.draft_en)}</textarea>
        </div>
      </div>
      <div class="content">
        <details>
          <summary>查看原始信息与直译</summary>
          <label>Question 中文翻译</label><pre>${escapeHtml(item.question_zh)}</pre>
          <label>Answer 中文翻译</label><pre>${escapeHtml(item.answer_zh)}</pre>
          <label>Original question</label><pre>${escapeHtml(item.original_question)}</pre>
          <label>Original answer</label><pre>${escapeHtml(item.original_answer)}</pre>
        </details>
        <div></div>
      </div>
      <div class="actions">
        <span class="msg"></span>
        <button class="reload" onclick="loadItems()">重新加载</button>
        <button class="approve" onclick="approve('${escapeHtml(item.source_id)}')">通过并保存</button>
      </div>
    </section>
  `).join('');
}

async function approve(sourceId) {
  const card = document.querySelector(`[data-source-id="${CSS.escape(sourceId)}"]`);
  const msg = card.querySelector('.msg');
  msg.textContent = '保存中...';
  const body = {
    source_id: sourceId,
    zh: card.querySelector('.zh').value,
    en: card.querySelector('.en').value,
  };
  const res = await fetch('/api/approve', {
    method: 'POST',
    headers: {'Content-Type': 'application/json'},
    body: JSON.stringify(body),
  });
  if (!res.ok) {
    msg.textContent = '保存失败：' + await res.text();
    return;
  }
  msg.textContent = '已通过并写回 Markdown';
  card.querySelector('.badge').textContent = 'Approved';
  card.querySelector('.badge').classList.add('approved');
  setTimeout(loadItems, 500);
}

loadItems().catch(err => { stats.textContent = '加载失败'; app.innerHTML = `<pre>${escapeHtml(err.message)}</pre>`; });
</script>
</body>
</html>"""


class ReviewHandler(BaseHTTPRequestHandler):
    qa_path: Path

    def log_message(self, format: str, *args: object) -> None:
        sys.stderr.write("%s - %s\n" % (self.address_string(), format % args))

    def send_json(self, payload: object, status: int = 200) -> None:
        body = json.dumps(payload, ensure_ascii=False).encode("utf-8")
        self.send_response(status)
        self.send_header("Content-Type", "application/json; charset=utf-8")
        self.send_header("Content-Length", str(len(body)))
        self.end_headers()
        self.wfile.write(body)

    def send_text(self, text: str, status: int = 200, content_type: str = "text/plain; charset=utf-8") -> None:
        body = text.encode("utf-8")
        self.send_response(status)
        self.send_header("Content-Type", content_type)
        self.send_header("Content-Length", str(len(body)))
        self.end_headers()
        self.wfile.write(body)

    def do_GET(self) -> None:
        path = urlparse(self.path).path
        if path == "/":
            self.send_text(render_page(), content_type="text/html; charset=utf-8")
            return
        if path == "/api/items":
            items = [asdict(item) for item in parse_items(read_text(self.qa_path))]
            self.send_json({"items": items})
            return
        self.send_text("Not found", status=404)

    def do_POST(self) -> None:
        path = urlparse(self.path).path
        if path != "/api/approve":
            self.send_text("Not found", status=404)
            return
        length = int(self.headers.get("Content-Length", "0"))
        try:
            payload = json.loads(self.rfile.read(length).decode("utf-8"))
            source_id = str(payload["source_id"])
            zh = str(payload["zh"])
            en = str(payload["en"])
            update_item(self.qa_path, source_id, zh, en, approved=True)
        except Exception as exc:
            self.send_text(str(exc), status=400)
            return
        self.send_json({"ok": True})


def run_server(path: Path, host: str, port: int, open_browser: bool) -> None:
    ReviewHandler.qa_path = path
    server = ThreadingHTTPServer((host, port), ReviewHandler)
    url = f"http://{host}:{port}"
    print(f"QA review server: {url}")
    print(f"Markdown file: {path}")
    if open_browser:
        webbrowser.open(url)
    server.serve_forever()


def main() -> int:
    parser = argparse.ArgumentParser(description="Local QA review workbench for Markdown QA files.")
    parser.add_argument("markdown_file", type=Path)
    parser.add_argument("--host", default="127.0.0.1")
    parser.add_argument("--port", type=int, default=8765)
    parser.add_argument("--check", action="store_true")
    parser.add_argument("--normalize", action="store_true")
    parser.add_argument("--open", action="store_true")
    args = parser.parse_args()

    path = args.markdown_file.resolve()
    if not path.exists():
        print(f"File not found: {path}", file=sys.stderr)
        return 1

    if args.normalize:
        normalize_draft_labels(path)

    items = parse_items(read_text(path))
    if args.check:
        approved = sum(1 for item in items if item.status == "approved")
        pending = len(items) - approved
        missing = [item.source_id for item in items if not item.draft_zh or not item.draft_en]
        print(f"items={len(items)} approved={approved} pending={pending}")
        if missing:
            print("missing_draft_answers=" + ",".join(missing))
            return 2
        return 0

    run_server(path, args.host, args.port, args.open)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
