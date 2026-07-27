# RX480E Homepage Redesign Implementation Plan

> **For AI agent workers:** Required sub-skill: use `subagent-driven-development` (recommended) or `executing-plans` to implement this plan task by task. Track progress with the checkboxes below.

**Goal:** Build a standalone, responsive RX480E homepage reference that keeps the live storefront header structure and applies the approved Signal Lab content and visual direction.

**Architecture:** Use one self-contained HTML file with inline CSS and minimal inline JavaScript. Keep generated scene images beside the HTML, reuse verified product diagrams from `docs/RX480E/`, and leave the previous preview and all live systems unchanged.

**Tech stack:** Semantic HTML5, CSS Grid/Flexbox, vanilla JavaScript, local WebP/PNG assets, Microsoft Edge headless screenshots, PowerShell verification.

---

## File Structure

- Create `Forum/RX480E/00_strategy/rx480e_homepage_signal_lab.html`: complete local prototype, styles, navigation, responsive layout, and mobile menu behavior.
- Create `Forum/RX480E/00_strategy/rx480e_homepage_signal_lab_hero.webp`: full-width workbench background with clear left-side text space and no generated RX480E hardware.
- Create `Forum/RX480E/00_strategy/rx480e_homepage_project_lighting.webp`: lighting-control outcome scene.
- Create `Forum/RX480E/00_strategy/rx480e_homepage_project_garage.webp`: garage/door-control outcome scene.
- Create `Forum/RX480E/00_strategy/rx480e_homepage_project_pump.webp`: pump/motor-control outcome scene.
- Create `Forum/RX480E/00_strategy/rx480e_logo.png`: local copy of the current public storefront logo.
- Do not modify `Forum/RX480E/00_strategy/shopify_homepage_preview.html`.

## Specification Coverage

- Header and Hero: Task 2 and Task 3.
- How It Works: Task 3.
- Choose Your Module: Task 3.
- What Can You Build: Task 3.
- Run Your First Test: Task 3.
- Troubleshooting and Footer: Task 3.
- Responsive Behavior and Accessibility: Task 4.
- Verification and acceptance criteria: Task 5.

### Task 1: Prepare Verified Visual Assets

**Files:**
- Create: `Forum/RX480E/00_strategy/rx480e_homepage_signal_lab_hero.webp`
- Create: `Forum/RX480E/00_strategy/rx480e_homepage_project_lighting.webp`
- Create: `Forum/RX480E/00_strategy/rx480e_homepage_project_garage.webp`
- Create: `Forum/RX480E/00_strategy/rx480e_homepage_project_pump.webp`
- Create: `Forum/RX480E/00_strategy/rx480e_logo.png`
- Read: `docs/RX480E/RX480E-1A/QIACHIP_RX480E-1A_Product_Diagram.webp`
- Read: `docs/RX480E/RX480E-4A/QIACHIP_RX480E-4A_Product_Diagram.webp`
- Read: `docs/RX480E/RX480E-4C/QIACHIP_RX480E-4C_Product_Diagram.webp`
- Read: `docs/RX480E/RX480E-868/QIACHIP_RX480E-868_Product_Diagram.webp`

- [ ] **Step 1: Verify source product images exist**

Run:

```powershell
$paths = @(
  'docs/RX480E/RX480E-1A/QIACHIP_RX480E-1A_Product_Diagram.webp',
  'docs/RX480E/RX480E-4A/QIACHIP_RX480E-4A_Product_Diagram.webp',
  'docs/RX480E/RX480E-4C/QIACHIP_RX480E-4C_Product_Diagram.webp',
  'docs/RX480E/RX480E-868/QIACHIP_RX480E-868_Product_Diagram.webp'
)
$paths | ForEach-Object { if (-not (Test-Path $_)) { throw "Missing product image: $_" } }
```

Expected: exit code 0 with no missing-image error.

- [ ] **Step 2: Create scene assets without inventing product hardware**

Generate four raster images with these exact roles:

```text
Hero: dark practical electronics workbench, receiver remote, breadboard, jumper wires,
small lamp in the background, empty high-contrast area on the left for white text,
no branded PCB and no readable labels, 16:9.

Lighting: finished desk-light wireless control scene, visible lamp and remote,
practical maker workbench, no branded PCB, 4:3.

Garage: small garage-door or door-lock demonstration rig controlled by a remote,
safe low-voltage workshop prototype, no branded PCB, 4:3.

Pump: low-voltage miniature water-pump demonstration with a relay/driver stage and
remote control, no mains wiring, no branded PCB, 4:3.
```

Use the real local product diagrams only in HTML overlays and product cards. Do not ask image generation to reproduce RX480E boards.

- [ ] **Step 3: Download the current public RX480E logo**

Run:

```powershell
curl.exe -L 'https://cdn.shopify.com/s/files/1/0996/3657/6551/files/RX480ELOGO512512_f4f85218-7b8b-4872-a77c-7ec13cb142cf.png?v=1784538554&width=240' -o 'Forum/RX480E/00_strategy/rx480e_logo.png'
```

Expected: `rx480e_logo.png` exists and has non-zero length.

- [ ] **Step 4: Inspect every raster asset**

Open all five assets with the local image viewer. Confirm the hero has usable left-side text space, project images show the intended outcomes, and no generated image contains an invented RX480E board.

- [ ] **Step 5: Commit the assets**

```powershell
git add -- 'Forum/RX480E/00_strategy/rx480e_homepage_signal_lab_hero.webp' 'Forum/RX480E/00_strategy/rx480e_homepage_project_lighting.webp' 'Forum/RX480E/00_strategy/rx480e_homepage_project_garage.webp' 'Forum/RX480E/00_strategy/rx480e_homepage_project_pump.webp' 'Forum/RX480E/00_strategy/rx480e_logo.png'
git commit -m "assets: add RX480E homepage reference visuals"
```

### Task 2: Build the Semantic Page and Header

**Files:**
- Create: `Forum/RX480E/00_strategy/rx480e_homepage_signal_lab.html`
- Reference: `Forum/RX480E/00_strategy/rx480e_homepage_redesign_design.md`
- Reference: `Forum/NEXT/rx480e_homepage_ui_comparison_report.md`

- [ ] **Step 1: Write a failing static contract check**

Run before creating the HTML:

```powershell
$html = Get-Content -Raw -Encoding UTF8 'Forum/RX480E/00_strategy/rx480e_homepage_signal_lab.html'
@('Home','Products','Documentation','Forum','Contact Us','Choose a Module','See Project Ideas') |
  ForEach-Object { if ($html -notmatch [regex]::Escape($_)) { throw "Missing required content: $_" } }
```

Expected: FAIL because the HTML file does not exist.

- [ ] **Step 2: Create the document shell and retained storefront header**

Implement:

```html
<body>
  <div class="announcement">RX480E Modules, Guides &amp; DIY Forum</div>
  <header class="site-header">
    <button class="menu-toggle" aria-expanded="false" aria-controls="mobile-menu">
      <span class="sr-only">Open menu</span>
    </button>
    <a class="logo" href="#top"><img src="rx480e_logo.png" alt="RX480E"></a>
    <nav class="desktop-nav" aria-label="Primary">
      <a href="#top">Home</a>
      <a href="#modules">Products</a>
      <a href="/blogs/manuals">Documentation</a>
      <a href="https://rx480e.discourse.group/">Forum</a>
      <a href="/pages/contact">Contact Us</a>
    </nav>
    <div class="header-tools" aria-label="Store tools">
      <button type="button" aria-label="Select country and currency">Japan | USD $</button>
      <button type="button" aria-label="Search"></button>
      <a href="/account" aria-label="Account"></a>
      <a href="/cart" aria-label="Cart"></a>
    </div>
  </header>
  <nav id="mobile-menu" class="mobile-menu" aria-label="Mobile" hidden>
    <a href="#top">Home</a>
    <a href="#modules">Products</a>
    <a href="/blogs/manuals">Documentation</a>
    <a href="https://rx480e.discourse.group/">Forum</a>
    <a href="/pages/contact">Contact Us</a>
  </nav>
  <main id="top">
    <section class="hero" aria-labelledby="hero-title">
      <p class="eyebrow">RX480E WIRELESS CONTROL LAB</p>
      <h1 id="hero-title">Turn a remote signal into something your project can use.</h1>
      <a href="#modules">Choose a Module</a>
      <a href="#projects">See Project Ideas</a>
    </section>
  </main>
</body>
```

Reuse the current Shopify header icon semantics and public SVG paths for menu, search, account, and cart. Keep icon buttons square with stable 44 px touch targets.

- [ ] **Step 3: Implement the mobile-menu behavior**

```javascript
const toggle = document.querySelector('.menu-toggle');
const menu = document.querySelector('#mobile-menu');

toggle.addEventListener('click', () => {
  const open = toggle.getAttribute('aria-expanded') === 'true';
  toggle.setAttribute('aria-expanded', String(!open));
  menu.hidden = open;
});
```

Also close the menu after a mobile-menu link is activated and on `Escape`.

- [ ] **Step 4: Run the static contract check**

Expected: PASS with no missing-content error.

- [ ] **Step 5: Commit the header shell**

```powershell
git add -- 'Forum/RX480E/00_strategy/rx480e_homepage_signal_lab.html'
git commit -m "feat: add RX480E homepage header shell"
```

### Task 3: Implement the Approved Homepage Sections

**Files:**
- Modify: `Forum/RX480E/00_strategy/rx480e_homepage_signal_lab.html`
- Reference: `Forum/RX480E/01_start_here/which_rx480e_model_should_i_choose.md`
- Reference: `Forum/RX480E/01_start_here/first_test_guide.md`

- [ ] **Step 1: Extend the static contract check to section IDs**

Run:

```powershell
$html = Get-Content -Raw -Encoding UTF8 'Forum/RX480E/00_strategy/rx480e_homepage_signal_lab.html'
@('how-it-works','modules','projects','first-test','troubleshooting') |
  ForEach-Object { if ($html -notmatch ('id="' + $_ + '"')) { throw "Missing section: $_" } }
```

Expected: FAIL until all approved sections are present.

- [ ] **Step 2: Add the full-width Signal Lab hero**

Use `rx480e_homepage_signal_lab_hero.webp` as the full-bleed background. Place the approved eyebrow, heading, supporting text, two actions, and three-item fact strip directly over the image. Overlay the existing real RX480E product diagrams on the right without placing the hero copy inside a card.

- [ ] **Step 3: Add How It Works**

Render four stable nodes with directional connectors:

```text
Remote -> RX480E -> MCU / Driver -> Real Device
```

Include the exact boundary statement `Signal output, not load power.`

- [ ] **Step 4: Add four product cards**

Use real product images and these verified summaries:

```text
RX480E-1A: 433.92 MHz, one OUT pin.
RX480E-4A: 433.92 MHz, four outputs; value 8 maps to D3.
RX480E-4C: 433.92 MHz, four outputs; value 8 maps to D0.
RX480E-868: 868 MHz, four D0-D3 pins, receive/transmit behavior.
```

Link cards to `/products/rx480e-1a`, `/products/rx480e-4a`, `/products/rx480e-4c`, and `/products/rx480e-868`. Add `Compare All Models` linking to the verified model-choice forum article.

- [ ] **Step 5: Add project, first-test, and troubleshooting sections**

Use the three scene images for Lighting Control, Garage / Door Control, and Pump / Motor Control. State that a suitable MCU, driver, or relay stage is required for real loads. Add the three first-test steps and the three troubleshooting routes without inventing project counts, success rates, or user activity.

- [ ] **Step 6: Add the complete footer**

Include Products, Documentation, Forum, Contact Us, Shipping / Returns, Privacy Policy, and Terms of Service. Keep the footer compact and utility-focused.

- [ ] **Step 7: Run the section contract check**

Expected: PASS with no missing-section error.

- [ ] **Step 8: Commit the complete content structure**

```powershell
git add -- 'Forum/RX480E/00_strategy/rx480e_homepage_signal_lab.html'
git commit -m "feat: build RX480E homepage content path"
```

### Task 4: Implement Responsive Styling and Accessibility

**Files:**
- Modify: `Forum/RX480E/00_strategy/rx480e_homepage_signal_lab.html`

- [ ] **Step 1: Add stable responsive layout rules**

Use a maximum content width, explicit grid tracks, fixed icon-button sizes, and image aspect ratios. Set breakpoints so product cards render four, two, then one per row, while project cards render three then one per row. Do not use viewport-width font scaling.

- [ ] **Step 2: Add mobile header behavior**

At tablet width, hide the desktop navigation, country selector, search, and account controls; keep the menu button, centered logo, and cart aligned in a three-column header grid. Ensure the menu panel remains inside the viewport.

- [ ] **Step 3: Add interaction and focus states**

Provide visible `:focus-visible` outlines, hover feedback that does not move layout, reduced-motion handling, and minimum 44 px touch targets. Buttons and cards must not use excessive rounding.

- [ ] **Step 4: Add a browser overflow assertion**

In the page's development-only console check, evaluate:

```javascript
document.documentElement.scrollWidth === document.documentElement.clientWidth
```

Expected: `true` at 1440 px and 390 px.

- [ ] **Step 5: Commit responsive and accessibility styling**

```powershell
git add -- 'Forum/RX480E/00_strategy/rx480e_homepage_signal_lab.html'
git commit -m "style: refine RX480E homepage responsiveness"
```

### Task 5: Visual and Functional Verification

**Files:**
- Verify: `Forum/RX480E/00_strategy/rx480e_homepage_signal_lab.html`
- Do not commit temporary screenshots.

- [ ] **Step 1: Run text and structure checks**

```powershell
$html = Get-Content -Raw -Encoding UTF8 'Forum/RX480E/00_strategy/rx480e_homepage_signal_lab.html'
@('Home','Products','Documentation','Forum','Contact Us','how-it-works','modules','projects','first-test','troubleshooting') |
  ForEach-Object { if ($html -notmatch [regex]::Escape($_)) { throw "Missing contract item: $_" } }
if ($html -match 'directly drive|guaranteed|compatible with every') { throw 'Unapproved product claim found' }
```

Expected: PASS.

- [ ] **Step 2: Capture desktop and mobile screenshots**

```powershell
& 'C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe' --headless=new --disable-gpu --hide-scrollbars --window-size=1440,1000 --screenshot="$env:TEMP\rx480e-signal-lab-desktop.png" "file:///D:/WorkFiles/qiachipweb/Forum/RX480E/00_strategy/rx480e_homepage_signal_lab.html"
& 'C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe' --headless=new --disable-gpu --hide-scrollbars --window-size=390,844 --screenshot="$env:TEMP\rx480e-signal-lab-mobile.png" "file:///D:/WorkFiles/qiachipweb/Forum/RX480E/00_strategy/rx480e_homepage_signal_lab.html"
```

Expected: both screenshots are non-blank and show the hero plus a hint of the next section.

- [ ] **Step 3: Inspect screenshots and page behavior**

Check for image failures, text overlap, clipped navigation, horizontal overflow, inconsistent card heights, blank hero areas, and unreadable contrast. Exercise the mobile menu, anchor links, and keyboard focus order in a browser.

- [ ] **Step 4: Run final repository checks**

```powershell
git diff --check
git status --short
```

Expected: no whitespace errors; only intended prototype assets and any unrelated pre-existing user changes are present.

- [ ] **Step 5: Commit verification fixes**

```powershell
git add -- 'Forum/RX480E/00_strategy/rx480e_homepage_signal_lab.html' 'Forum/RX480E/00_strategy/rx480e_homepage_signal_lab_hero.webp' 'Forum/RX480E/00_strategy/rx480e_homepage_project_lighting.webp' 'Forum/RX480E/00_strategy/rx480e_homepage_project_garage.webp' 'Forum/RX480E/00_strategy/rx480e_homepage_project_pump.webp' 'Forum/RX480E/00_strategy/rx480e_logo.png'
git commit -m "fix: complete RX480E homepage reference verification"
```
