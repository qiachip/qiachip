from __future__ import annotations

import importlib.util
import shutil
import sys
import tempfile
import unittest
from pathlib import Path


WORKTREE_ROOT = Path(__file__).resolve().parents[1]
SERVER_PATH = WORKTREE_ROOT / "tools" / "qa_review_server.py"
QA_PATH = WORKTREE_ROOT / "Refer" / "qa-collection" / "KR2202_FAQ_from_QA_collection_2026-06-18.md"


def load_server_module():
    spec = importlib.util.spec_from_file_location("qa_review_server", SERVER_PATH)
    if spec is None or spec.loader is None:
        raise RuntimeError(f"Could not load module from {SERVER_PATH}")
    module = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = module
    spec.loader.exec_module(module)
    return module


class QAReviewServerTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.server = load_server_module()

    def block_for(self, text: str, source_id: str) -> str:
        for match, start, end in self.server.iter_blocks(text):
            if match.group("source_id").strip() == source_id:
                return text[start:end]
        self.fail(f"Source ID not found: {source_id}")

    def test_parse_items_extracts_all_qa_drafts(self) -> None:
        items = self.server.parse_items(self.server.read_text(QA_PATH))

        self.assertEqual(len(items), 11)
        self.assertEqual(items[0].source_id, "38")
        self.assertIn("KR2202", items[0].draft_en)
        self.assertTrue(all(item.draft_zh for item in items))
        self.assertTrue(all(item.draft_en for item in items))
        self.assertTrue(all(item.original_question for item in items))
        self.assertTrue(all(item.original_answer for item in items))

    def test_normalize_draft_labels_marks_optimized_answers_as_pending(self) -> None:
        with tempfile.TemporaryDirectory() as temp_dir:
            temp_path = Path(temp_dir) / QA_PATH.name
            shutil.copyfile(QA_PATH, temp_path)
            text = self.server.read_text(temp_path)
            text = text.replace("**Approved standard answer 中文：**", "**Optimized answer 中文：**")
            text = text.replace("**Approved standard answer English:**", "**Optimized answer English:**")
            self.server.write_text(temp_path, text)

            self.server.normalize_draft_labels(temp_path)
            text = self.server.read_text(temp_path)

        self.assertNotIn("**Optimized answer 中文：**", text)
        self.assertNotIn("**Optimized answer English:**", text)
        self.assertIn("**Draft optimized answer 中文（待审核）：**", text)
        self.assertIn("**Draft optimized answer English (Pending review):**", text)

    def test_update_item_approves_only_target_item_and_preserves_source_sections(self) -> None:
        with tempfile.TemporaryDirectory() as temp_dir:
            temp_path = Path(temp_dir) / QA_PATH.name
            shutil.copyfile(QA_PATH, temp_path)
            before = self.server.read_text(temp_path)
            before_q2 = self.block_for(before, "22")

            self.server.update_item(
                temp_path,
                "38",
                "审核后的中文答案",
                "Approved English answer.",
                approved=True,
            )
            after = self.server.read_text(temp_path)
            after_q2 = self.block_for(after, "22")

        self.assertIn("**Approved standard answer 中文：**\n\n审核后的中文答案", after)
        self.assertIn("**Approved standard answer English:**\n\nApproved English answer.", after)
        self.assertIn("**Original question:**", after)
        self.assertIn("**Original answer:**", after)
        self.assertIn("> When setting up a new radio remote control", after)
        self.assertEqual(before_q2, after_q2)
        self.assertEqual(after.count("审核后的中文答案"), 1)


if __name__ == "__main__":
    unittest.main()
