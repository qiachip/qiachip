# FLC Broad Customer Question Merge Report

## 1. Purpose

This report merges classified FLC customer questions by core function. It is the first-level question bank for later customer-service QA work.

This stage identifies the customer's main question only. It does not analyze causes or write answers. A failed speed, a speed that is too fast, identical speeds, and incorrect speed order all belong to one broad issue: the fan speeds do not match expectations. Detailed symptoms will be analyzed when answers are written.

## 2. Scope and Limits

- The report covers 42 classified IDs. One record may appear under more than one topic.
- Questions from different models may share the same customer intent. This does not mean the models have identical specifications, wiring, or functions.
- Current public manuals cover only `FLC05-E110V` and `FLC05-E220V`.
- Technical facts for `FLC-110V`, `FLC-220V`, and `FLC06-E110V` need later confirmation.
- This report does not change the source Excel file or publish content to the public FAQ.

---

## 3. Fan Speed

**Source IDs:** ID6, ID29, ID85, ID88, ID90, ID93, ID100, ID102, ID108, ID109, ID110, ID118, ID128, ID133, ID138, ID140, ID151, ID154

**Models:** `FLC06-E110V`, `FLC-220V`

**Merge logic:**

The detailed symptoms include one speed not working, LOW being too fast, all three speeds being the same, incorrect speed order, and little difference between speeds. The shared customer intent is that the three fan speeds do not work as expected after installing the controller. At this stage, all these symptoms are merged into one broad speed-mismatch question.

**Merged question:**

Why do the LOW, MED, and HI fan speeds not match expectations after installing the FLC fan controller?

**Later analysis focus:**

- Separate a failed speed, identical speeds, incorrect speed order, and all speeds being too fast.
- Check the fan motor type and whether the original and controller capacitors match.
- Confirm the correct sources for `FLC06-E110V` and `FLC-220V`. Do not apply the FLC05 manual automatically.

---

## 4. Remote Control

**Source IDs:** ID87, ID124, ID129, ID134, ID138

**Models:** `FLC-220V`

**Merge logic:**

These records include incorrect button control, a STOP button that does not work, an unresponsive remote, and a light button that also controls the fan. The shared issue is that remote buttons do not control the expected functions.

**Merged question:**

Why do the FLC remote buttons not control the fan and light as expected?

**Later analysis focus:**

- Separate incorrect button mapping, one failed button, and a fully unresponsive remote.
- Check whether the problem began during installation, after pairing again, or after normal use.
- Confirm the pairing method and button definitions for the exact model.

---

## 5. Light Control

**Source IDs:** ID87, ID91, ID111, ID120, ID128

**Models:** `FLC-220V`

**Merge logic:**

These records include a light that cannot turn on or off, random flashing, a light that fails while the fan runs, and a light and fan that cannot work independently. The shared customer intent is that light control does not work as expected.

**Merged question:**

Why does the light not work as expected after installing the FLC controller?

**Later analysis focus:**

- Separate no light, failure to turn off, flashing, and incorrect fan-light interaction.
- Check the light type, wiring, and light-control limits of the exact controller.
- Keep the timeline when the problem began after normal use.

---

## 6. Buzzer

**Source IDs:** ID56, ID92, ID98, ID133

**Models:** `FLC05-E220V`, `FLC-220V`

**Merge logic:**

These questions include an unexpected number of beeps, beeping after the buzzer was disabled, and failure to enable or disable the buzzer. The shared issue is that the buzzer sound or buzzer setting does not work as expected.

**Merged question:**

Why does the FLC controller beep differently than expected, or why can the buzzer not be disabled?

**Later analysis focus:**

- Separate startup beeps, button beeps, and pairing-operation beeps.
- Check `FLC05-E220V` and the unconfirmed `FLC-220V` instructions separately.
- Do not publish the customer's method of physically removing the buzzer as a standard solution.

---

## 7. Size and Installation Space

**Source IDs:** ID103, ID114, ID132, ID135, ID141

**Models:** `FLC-220V`

**Merge logic:**

These customers could not easily fit the receiver or internal board inside the fan canopy, base, or original receiver space. The shared intent is to confirm whether the receiver will fit before purchase.

**Merged question:**

Will the FLC receiver fit inside my ceiling fan canopy or existing receiver space?

**Later analysis focus:**

- Collect the exact length, width, and height for each model.
- Tell customers to measure the available fan space before purchase.
- Do not treat cutting the housing or placing the receiver inside the ceiling as a standard installation method.

---

## 8. Compatibility

**Source IDs:** ID21, ID105, ID123

**Models:** `FLC-220V`

**Merge logic:**

These questions involve motor and capacitor specifications, fan-reverse control, and light dimming. The shared customer intent is to confirm whether the FLC controller supports the existing fan, light, or required function.

**Merged question:**

Is the FLC controller compatible with my ceiling fan, motor, light, and required functions?

**Later analysis focus:**

- Check AC or DC motor type, running capacitor, fan reverse, and light dimming separately.
- Every compatibility answer must name the exact controller model and use a supported source.
- Mark unsupported compatibility claims as `pending confirmation`.

---

## 9. Noise

**Source IDs:** ID97, ID115

**Models:** `FLC-220V`

**Merge logic:**

Both records report clear operating noise or humming after installation. This stage does not decide whether the sound comes from the fan motor, receiver, or another part. Both records remain under one broad noise question.

**Merged question:**

Why does the fan or receiver make a noticeable noise after installing the FLC controller?

**Later analysis focus:**

- Confirm the noise source, the affected speed, and when the noise begins.
- Separate mechanical fan noise, motor humming, and receiver sound.
- Check whether the noise appears with a speed or compatibility problem.

---

## 10. Behavior After Power Returns

**Source IDs:** ID99

**Models:** `FLC-220V`

**Merge logic:** Keep as a standalone topic. It has one main source and should not be forced into another function issue.

**Merged question:**

Why are the fan and light states different after power returns following an outage?

**Later analysis focus:**

- Separate pairing memory, working-mode memory, and load on/off state.
- Use the manual only after the exact model is confirmed.

---

## 11. Problems After Long-Term Use

**Source IDs:** ID86

**Models:** `FLC-220V`

**Merge logic:** Keep as a standalone topic. Its key value is the timeline: the product worked for a long time before the symptoms began.

**Merged question:**

Why do the light and fan-speed functions become abnormal after the FLC controller has been used for a long time?

**Later analysis focus:**

- Keep the timeline of almost three years before failure.
- Analyze light flashing and the small difference between MED and HI separately later.
- Leave room for aging or product failure in the later answer.

---

## 12. Product Improvement Suggestions

**Source IDs:** ID84

**Models:** `FLC-220V`

**Merge logic:** Keep as standalone internal product feedback. It is not recommended as a public customer FAQ.

**Merged question:**

How could the FLC controller improve its installation size, wire length, connectors, and remote design?

**Later analysis focus:**

- Separate installation space, output-wire length, connectors, and remote build quality into product feedback items.
- Cross-reference the size and short-wire topics without creating duplicate public FAQs.

---

## 13. Short Output Wires

**Source IDs:** ID89

**Models:** `FLC-220V`

**Merge logic:** Keep as a standalone topic. The customer could not reach the fan motor terminal with the supplied output wire.

**Merged question:**

What should I do if the FLC receiver output wire is too short to reach the fan motor terminal?

**Later analysis focus:**

- Confirm the supplied wire length and allowed installation method for the exact model.
- Any later answer about wiring or extending a wire needs a clear safety boundary.

---

## 14. French Instructions

**Source IDs:** ID135

**Models:** `FLC-220V`

**Merge logic:** Keep as a standalone topic. The source also reports a size problem, which is already indexed under Size and Installation Space.

**Merged question:**

Are French instructions available for the FLC controller, and will the receiver fit inside my ceiling fan?

**Later analysis focus:**

- Confirm whether French installation instructions are available.
- Use the size topic for installation-space analysis.
- The original record also reports a short circuit and a tripped fuse. Review that part separately as a safety issue.

---

## 15. Pending Classification

The following eight records are not in the approved broad topics. A later review must decide whether to add a topic, merge them into an existing topic, or remove them from the public FAQ set.

| ID | Model | Question summary | Initial handling suggestion |
| --- | --- | --- | --- |
| 10 | `FLC-110V` | Asks about the safe ambient temperature and use with a fireplace fan installed at the bottom of a fireplace enclosure. | Confirm fit and safety limits. |
| 39 | `FLC-220V` | The controller melted after six months and left a deep burn mark. | Safety incident; do not convert directly into a normal FAQ. |
| 94 | `FLC-220V` | A replacement receiver works, but the original light-dimming function is lost. | Consider merging into Compatibility. |
| 116 | `FLC-220V` | The controller became fully unresponsive after three months. The light and fan cannot be controlled. | Consider a full-product-failure topic. |
| 119 | `FLC-220V` | The controller stopped working, and the light cannot turn on. | Consider merging into full product failure. |
| 121 | `FLC-220V` | Same melted-controller and burn-mark wording as ID39. | Check whether this is a duplicate safety incident. Do not convert directly into a normal FAQ. |
| 136 | `FLC-220V` | Light status affects the fan, the motor keeps turning slowly, and the receiver rattles internally. | Control issue and possible product fault need classification. |
| 142 | `FLC05-E220V` | Asks whether a named fan-light model, LED rating, and existing wiring are compatible. | Consider merging into Compatibility after checking the manual. |

## 16. Recommended Next Stage

1. Review whether the merged questions match real customer wording.
2. Classify the eight pending records and lock the final question list.
3. Read the manual for each exact model and research causes and answers for each question.
4. Approve the Chinese answers before preparing short customer-facing English QA.
