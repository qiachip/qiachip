# RX480E Homepage Redesign Design

> Date: 2026-07-27  
> Status: Approved concept, pending implementation  
> Deliverable: standalone local HTML reference, not a live Shopify theme change

## Purpose

Create a new RX480E homepage reference based on `Forum/NEXT/rx480e_homepage_ui_comparison_report.md` while retaining the current storefront header structure and shopping utilities.

The homepage must help a first-time visitor follow this path:

```text
Understand RX480E
-> choose a model
-> see project possibilities
-> run a first test
-> get troubleshooting help
```

## Scope

- Add one standalone local HTML prototype in `Forum/RX480E/00_strategy/`.
- Keep the existing `shopify_homepage_preview.html` unchanged for comparison.
- Reuse verified product facts and existing real RX480E product images.
- Include responsive desktop and mobile layouts.
- Do not modify Shopify, Discourse, MkDocs, product records, prices, inventory, or public documentation.

## Header

Retain the current live storefront structure from `https://rx480e.com/`:

- RX480E logo and current visual proportion.
- Desktop navigation, in the current order:
  - Home
  - Products
  - Documentation
  - Forum
  - Contact Us
- Desktop utilities:
  - country and currency selector
  - search
  - account
  - cart
- Mobile header:
  - menu icon on the left
  - centered RX480E logo
  - cart on the right

Retain the announcement bar structure but replace the immature-community message with:

`RX480E Modules, Guides & DIY Forum`

The prototype must prevent the horizontal overflow visible on the current 390 px mobile homepage.

## Visual Direction

Use the approved `Signal Lab` direction:

- A dark, low-saturation electronics workbench hero.
- Real RX480E module images remain the primary product evidence.
- Signal green is used for the signal path, primary actions, and small technical accents.
- Warm off-white and light gray sections provide contrast below the hero.
- The page should feel like a practical electronics lab, not a cyberpunk interface or a generic marketplace.
- Cards use restrained borders, a maximum 8 px corner radius, consistent image ratios, and limited shadows.
- Typography uses a compact technical sans-serif for interface and body copy, with a restrained display face only where it improves brand recognition.

## Hero

Use a full-width workbench image as the background, with text directly over the left side and a real RX480E module composition on the right.

- Eyebrow: `RX480E WIRELESS CONTROL LAB`
- Heading: `Turn a remote signal into something your project can use.`
- Supporting copy: `433 MHz and 868 MHz modules for receiving, decoding, and routing wireless signals into your circuit.`
- Primary action: `Choose a Module`
- Secondary action: `See Project Ideas`
- Fact strip:
  - `433 / 868 MHz`
  - `1 or 4 outputs`
  - `Signal-level outputs`

The hero must not claim that RX480E can directly power motors, locks, pumps, relay coils, or mains devices.

## Homepage Sections

### 1. How It Works

Show a clear signal path:

```text
Remote -> RX480E -> MCU / Driver -> Real Device
```

Add a persistent boundary statement: `Signal output, not load power.` The diagram must keep the driver or MCU stage visible rather than implying a direct connection to a real load.

### 2. Choose Your Module

Show four consistent product cards:

- RX480E-1A
- RX480E-4A
- RX480E-4C
- RX480E-868

Each card has a fixed location for model, frequency, output count, use direction, real product image, and detail link. RX480E-4A and RX480E-4C must explicitly state that their pin mappings differ. End the section with `Compare All Models`.

No unverified price, inventory, compatibility, or performance claim is shown.

### 3. What Can You Build?

Show three outcome-led project scenes:

- Lighting Control
- Garage / Door Control
- Pump / Motor Control

Scene images communicate the final project category. Exact product appearance is represented only with existing real RX480E images, not generated module artwork. Each card explains that a driver, relay module, or MCU is required where appropriate.

### 4. Run Your First Test

Use a three-step sequence:

1. Power and pair the module.
2. Press one remote button.
3. Check whether the expected output pin changes.

The section links to the Start Here first-test guide and explicitly avoids using a final high-current load for the first test.

### 5. Troubleshooting

Use a full-width dark band with three common routes:

- No output
- Wrong pin or mode
- Short range

The primary action opens the forum troubleshooting area. The section is an entry point, not an embedded FAQ.

### 6. Footer

Retain the storefront role of the footer and include:

- Products
- Documentation
- Forum
- Contact Us
- Shipping / Returns
- Privacy Policy
- Terms of Service

## Interaction

- Desktop navigation and utility icons have visible hover and keyboard-focus states.
- The mobile menu opens and closes without resizing or shifting the header.
- Hero and section actions use real or planned destinations already identified in project materials.
- Anchor links scroll to the relevant section.
- Product and project cards have restrained hover feedback.
- No carousel, auto-playing media, filter UI, account simulation, cart simulation, or fabricated activity counter is included.

## Assets

- Reuse existing RX480E product diagrams from `docs/RX480E/`.
- Reuse the current public RX480E logo as a local asset in the prototype.
- Create or source a workbench background and three project-scene images without altering the appearance of any RX480E module.
- Keep generated or illustrative scene imagery visually subordinate to the real product images.
- Use familiar interface icons from a maintained icon library or the Shopify-style icon set; do not hand-draw replacement icons when an established icon exists.

## Responsive Behavior

- Primary desktop reference: 1440 px wide.
- Primary mobile reference: 390 px wide.
- Navigation collapses at tablet width.
- Product cards move from four columns to two columns and then one column.
- Project cards move from three columns to one column.
- The hero keeps the next section partially visible on common desktop and mobile viewports.
- Text and controls must not overflow, overlap, or create horizontal page scrolling.

## Accessibility

- Use semantic landmarks and heading order.
- Give all controls accessible names.
- Provide descriptive alt text for product images and concise alt text for project scenes.
- Maintain visible keyboard focus and sufficient color contrast.
- Respect reduced-motion preferences.
- Keep touch targets at least 44 px high on mobile.

## Acceptance Criteria

1. The current live navigation labels, order, logo role, and storefront utilities are represented.
2. The six homepage sections appear in the approved order.
3. A first-time visitor can answer what RX480E does, which model direction fits, what can be built, how to run the first test, and where to troubleshoot.
4. Existing real product images render correctly and no generated image misrepresents an RX480E module.
5. Product facts match existing project sources and do not imply direct high-current load control.
6. The page is usable without horizontal overflow at 1440 px and 390 px widths.
7. Navigation, mobile menu, anchor links, and primary actions are keyboard-accessible.
8. The prototype is self-contained enough to open locally and does not change any external system.

## Verification

- Inspect the prototype at 1440 x 1000 and 390 x 844.
- Capture desktop and mobile screenshots.
- Check the rendered page for horizontal overflow, blank images, text overlap, and broken links.
- Exercise the mobile menu, anchor links, and keyboard focus order.
- Compare all displayed product facts against the existing RX480E source documents before completion.
