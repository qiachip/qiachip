# KR1201A FAQ Draft for Manual Update

## Source

- **Based on:** `Refer/youtube-comments/KR1201A_youtube_comment_questions_2026-06-09.md`
- **Original platform:** YouTube comments
- **Video title:** How to use remote control switch, DC12V, wireless relay switch 1Ch rf 433Mhz, KR1201 by QIACHIP
- **Video URL:** https://www.youtube.com/watch?v=ah2Llv7Pp2w&t=1s
- **Prepared date:** 2026-06-09
- **Purpose:** This draft rewrites selected customer questions and QIACHIP replies into clean FAQ-style Q&A entries for possible insertion into the KR1201A user manual.

## Notes Before Inserting into the Manual

- This is a draft for documentation editing, not the original comment archive.
- The wording below is normalized for a product manual.
- Before inserting into the official KR1201A manual, verify the electrical specifications against the latest product data.
- Product documentation under `docs/` should remain in English.

## Recommended FAQ Section Draft

### FAQ

#### Q1: Does KR1201A support momentary mode?

**A:** Yes. KR1201A supports momentary mode. In momentary mode, the relay is activated only while the remote button is pressed. When the button is released, the relay turns off.

KR1201A also supports other working modes, such as self-locking mode and interlocking mode. Select the mode according to your application.

#### Q2: What happens in momentary mode if the remote moves out of signal range while the button is being held?

**A:** In momentary mode, moving the remote out of signal range is equivalent to releasing the remote button. The relay will turn off when the receiver no longer receives the signal.

#### Q3: Which mode should I use if I want to reduce battery consumption?

**A:** The receiver consumes a small amount of power while in standby as long as it is connected to power. Momentary mode can reduce the active working time, which may help extend battery life in some applications.

For longer operating time, use a suitable large-capacity battery or a stable 12V DC power supply.

#### Q4: Will KR1201A lose the paired remote controls or working mode after power loss?

**A:** No. KR1201A has memory function. After the remote controls and working mode are correctly paired and set, they will not be lost when the power is disconnected.

After power is restored, the receiver can continue working with the previously saved remote controls and mode, unless the receiver has been reset.

#### Q5: Does toggle mode need to be set again after power loss?

**A:** No. If KR1201A has been set to toggle mode, the receiver will remember this mode after power loss. It does not need to be paired or programmed again after power is restored.

#### Q6: Can one KR1201A receiver be paired with more than one remote control?

**A:** Yes. One KR1201A receiver can be paired with multiple remote controls. Pair the first remote control, then repeat the pairing operation for the additional remote controls.

The paired remote controls can operate the same receiver independently.

#### Q7: Can two remote controls use the same working mode, such as delay mode or toggle mode?

**A:** Yes. Multiple remote controls can be paired with the same receiver and used with the same working mode, such as delay mode or toggle mode.

#### Q8: Can KR1201A reverse a DC motor?

**A:** No. KR1201A is a single-channel relay receiver. It supports simple on/off control and cannot reverse a DC motor directly.

Reversing a DC motor requires switching the positive and negative terminals of the motor, which normally requires at least a two-channel relay controller or a dedicated motor controller.

#### Q9: Can button B be used to reverse a motor?

**A:** Not with KR1201A alone. KR1201A is a single-channel controller and cannot provide forward and reverse motor control.

For motor forward and reverse control, use a suitable two-channel controller, such as a controller designed for DC motor or linear actuator control.

#### Q10: Can KR1201A control a servo motor?

**A:** KR1201A is not designed for precise servo motor control. Servo motors usually require signal-based control from a suitable servo controller or programmable controller.

If you only need simple motor forward and reverse operation, use a suitable motor controller instead of KR1201A.

#### Q11: Can two KR1201A receivers be used to control a DC motor left and right?

**A:** KR1201A is not the recommended solution for DC motor direction control. For left and right, forward and reverse, or polarity-changing motor control, use a two-channel receiver or a dedicated motor controller.

#### Q12: Can KR1201A be powered by AC power?

**A:** No. KR1201A is a DC relay receiver and must not be connected directly to AC power.

Use a suitable DC power supply for KR1201A. If your application requires AC 110V or AC 220V control, choose a relay receiver designed for that AC voltage.

#### Q13: Can KR1201A control AC 220V home appliances?

**A:** KR1201A itself is a 12V DC receiver module. Do not power the module directly with AC 220V.

If you need to control AC 220V appliances, use a relay module designed for AC 220V applications, or use KR1201A only in a properly isolated control circuit designed by a qualified person.

#### Q14: Can KR1201A and the load use the same power supply?

**A:** They can use the same power supply only if the voltage and current ratings match the requirements of both the receiver and the load.

Check that:

- the receiver input voltage matches the power supply;
- the load voltage matches the same power supply;
- the power supply output current is sufficient for the receiver and load together.

If the voltage is incorrect or the current is insufficient, the device may not work properly or may be damaged.

#### Q15: Can a 5V version work with a 3.7V Li-ion / 18650 battery?

**A:** A 5V-rated receiver is designed to operate at 5V. A 3.7V Li-ion battery, such as an 18650 cell, is lower than the rated voltage.

It may cause unstable operation, reduced remote-control distance, or failure to work. For stable performance, use a proper 5V power source for a 5V receiver.

#### Q16: What battery should be used for KR1201A?

**A:** Use a suitable 12V power source for KR1201A. A 12V lithium battery can provide better power capacity than ordinary AA batteries.

Ordinary AA batteries may work if they provide the required voltage, but they usually have lower capacity and may run out quickly. If the device stops working, check whether the battery is drained or whether the receiver has been damaged.

#### Q17: Can a 9V battery power KR1201A?

**A:** No. KR1201A is designed for 12V DC power. A 9V battery may light the indicator but may not provide enough voltage for the relay to work correctly.

Use a proper 12V power source within the specified operating range.

#### Q18: Can two devices be connected using NO and NC?

**A:** Yes, the NO and NC terminals can be used according to the relay logic. NO is normally open, and NC is normally closed.

For example, one load can be connected through NO and another load through NC, so one load is on while the other is off. Make sure the wiring matches the load type and power supply, and avoid short circuits.

#### Q19: Can the negative line be connected to COM for triggering?

**A:** In many wiring diagrams, the positive line is connected to COM. However, if you understand the relay principle, the negative line can also be connected to COM in some DC circuits.

The key rule is that the circuit must not create a short circuit before or after relay triggering.

#### Q20: Can KR1201A control two LED lights so that one is on while the other is off?

**A:** Yes, this can be done by using the NO and NC contacts of the relay.

One LED can be connected through the NO terminal, and the other LED can be connected through the NC terminal. When the relay changes state, one LED turns on and the other turns off.

For more complex multi-load control, a multi-channel relay receiver is recommended.

#### Q21: What is the maximum remote-control distance?

**A:** The actual remote-control distance depends on the remote model, antenna, installation environment, obstacles, and interference.

Some remotes may claim very long ranges, such as 2 miles or 3 km, but real-world performance can be much lower. In practical road-like testing, the distance may be around 1 km or less depending on conditions.

#### Q22: Can an external antenna be connected?

**A:** KR1201A has an antenna on the module. The antenna can be replaced for testing, but the replacement antenna must match the required specifications.

If the antenna impedance or design is not suitable, the distance may not improve and the module may perform poorly.

#### Q23: How do I reset KR1201A?

**A:** For QIACHIP KR1201A, reset is usually performed by pressing the learning button on the receiver 8 times.

After reset, previously paired remote controls and mode settings may be cleared. Pair the remote controls and set the working mode again after reset.

#### Q24: What should I do if the receiver does not reset after pressing the learning button 8 times?

**A:** First confirm that the product is a QIACHIP KR1201A receiver. Reset methods may differ between brands or product versions.

If pressing 8 times does not work, possible reset methods on some products may include:

- pressing the learning button a different number of times;
- long-pressing the learning button for several seconds.

If you are not sure, contact the seller or check the manual for the exact product version.

#### Q25: Does KR1201A have memory storage, such as EEPROM?

**A:** Yes. KR1201A has storage memory for paired remote controls and mode settings.

The module can store multiple remote controls. Based on QIACHIP's reply in the YouTube comments, this module can store up to 20 remote controls.

#### Q26: Can KR1201A be used for access control or automatic residential gates?

**A:** KR1201A can provide dry contact control and may be used in some access-control applications.

Whether it can be used for an automatic residential gate depends on the gate controller's working principle, input requirements, and voltage. For AC 220V systems or higher-power applications, choose a suitable relay receiver designed for that system.

## Suggested Manual Placement

This FAQ section can be considered for placement near the end of the KR1201A manual, after the wiring diagrams and working mode instructions.

Recommended section title:

```markdown
## Frequently Asked Questions
```

## Topics That May Need Separate Manual Sections

Some questions appear repeatedly and may deserve more than a FAQ entry:

1. **Working mode memory after power loss** — add a note near the mode-setting section.
2. **Multiple remote pairing** — add a short step-by-step pairing example.
3. **DC motor reverse control limitation** — add a warning that KR1201A is not for motor direction control.
4. **AC power limitation** — add a warning that KR1201A must not be connected directly to AC power.
5. **Power supply requirements** — clarify the correct input voltage and battery recommendations.
6. **NO / NC / COM examples** — add one practical example for controlling two LED loads in opposite states.
