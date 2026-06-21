# Product FAQ



[TOC]

## **General FAQ**

??? question "Pairing Multiple Remotes"
    **Q**: I purchased a kit with two remotes, but it seems to only pair with one remote at a time. When I pair the second remote, the first one stops working. What is the correct procedure to pair both remotes?

    **A**: When pairing an additional remote, do not reset the receiver first. Pair the first remote, then repeat the pairing operation for the second remote. Pressing the learning button 8 times usually resets the receiver and clears the paired remotes.

??? question "Mode Retention After Power Loss"
    **Q**: If I've paired my transmitter and receiver and set a specific working mode, will the receiver remember this mode if it loses power?

    **A**: Yes, generally, once a QIACHIP receiver and transmitter are paired and a working mode, such as momentary, toggle, latching, or delay mode, is set, the receiver will retain these settings after power loss. After power is restored, it should remember the last configured working mode and paired transmitters.

??? question "Compatibility with Other Brands"
    **Q**: Can I use remote controls or receivers from other brands with QIACHIP products?

    **A**: For reliable operation and to ensure all features and working modes function as intended, it is strongly recommended to use QIACHIP brand remote controls (transmitters) with QIACHIP controllers (receivers/wireless remote control switches). While some third-party remotes or receivers might seem to work, compatibility is not guaranteed, and you may experience issues with pairing, range, or functionality of specific modes.

??? question "Momentary Mode Signal Range"
    **Q**: What happens in momentary mode if the remote moves out of signal range while the button is being held?

    **A**: In momentary mode, moving the remote out of signal range is equivalent to releasing the remote button. The relay will turn off when the receiver no longer receives the signal.

??? question "AC and DC Power Supply"
    **Q**: Can a DC receiver module be connected directly to AC power?

    **A**: No. A DC receiver module must not be connected directly to AC power. Use a suitable DC power supply for DC receiver modules. If your application requires AC 110V or AC 220V control, choose a relay receiver designed for that AC voltage.

??? question "NO / NC / COM Terminals"
    **Q**: What do NO, NC, and COM mean on a relay receiver?

    **A**: COM is the common terminal, NO is the normally open terminal, and NC is the normally closed terminal. NO is open before the relay is activated and closes after activation. NC is closed before the relay is activated and opens after activation.

??? question "Using the Same Power Supply"
    **Q**: Can the receiver and the load use the same power supply?

    **A**: They can use the same power supply only if the voltage and current ratings match the requirements of both the receiver and the load. If the voltage is incorrect or the current is insufficient, the device may not work properly or may be damaged.

??? question "Remote-Control Distance"
    **Q**: What affects the remote-control distance?

    **A**: The actual remote-control distance depends on the remote model, antenna, installation environment, obstacles, and interference. Claimed long-range distances may be much lower in real-world use.

??? question "External Antenna"
    **Q**: Can an external antenna be connected to improve range?

    **A**: Some receiver modules have an antenna that can be replaced or adjusted for testing. The replacement antenna must match the required specifications. If the antenna impedance or design is not suitable, the distance may not improve and the module may perform poorly.


## **KR1201A**

??? question "1. Does KR1201A support momentary mode?"
    **A**: Yes. KR1201A supports momentary mode. In momentary mode, the relay is activated only while the remote button is pressed. When the button is released, the relay turns off.

    KR1201A also supports other working modes, such as self-locking mode and interlocking mode. Select the mode according to your application.

??? question "2. Which mode should I use if I want to reduce battery consumption?"
    **A**: The receiver consumes a small amount of power while in standby as long as it is connected to power. Momentary mode can reduce the active working time, which may help extend battery life in some applications.

    For longer operating time, use a suitable large-capacity battery or a stable 12V DC power supply.

??? question "3. Does toggle mode need to be set again after power loss?"
    **A**: No. If KR1201A has been set to toggle mode, the receiver will remember this mode after power loss. It does not need to be paired or programmed again after power is restored.

??? question "4. Can two remote controls use the same working mode, such as delay mode or toggle mode?"
    **A**: Yes. Multiple remote controls can be paired with the same receiver and used with the same working mode, such as delay mode or toggle mode.

??? question "5. Can KR1201A reverse a DC motor?"
    **A**: No. KR1201A is a single-channel relay receiver. It supports simple on/off control and cannot reverse a DC motor directly.

    Reversing a DC motor requires switching the positive and negative terminals of the motor, which normally requires at least a two-channel relay controller or a dedicated motor controller.

??? question "6. Can button B be used to reverse a motor?"
    **A**: Not with KR1201A alone. KR1201A is a single-channel controller and cannot provide forward and reverse motor control.

    For motor forward and reverse control, use a suitable two-channel controller, such as a controller designed for DC motor or linear actuator control.

??? question "7. Can KR1201A control a servo motor?"
    **A**: KR1201A is not designed for precise servo motor control. Servo motors usually require signal-based control from a suitable servo controller or programmable controller.

    If you only need simple motor forward and reverse operation, use a suitable motor controller instead of KR1201A.

??? question "8. Can two KR1201A receivers be used to control a DC motor left and right?"
    **A**: KR1201A is not the recommended solution for DC motor direction control. For left and right, forward and reverse, or polarity-changing motor control, use a two-channel receiver or a dedicated motor controller.

??? question "9. Can KR1201A control AC 220V home appliances?"
    **A**: KR1201A itself is a 12V DC receiver module. Do not power the module directly with AC 220V.

    If you need to control AC 220V appliances, use a relay module designed for AC 220V applications, or use KR1201A only in a properly isolated control circuit designed by a qualified person.

??? question "10. Can a 5V version work with a 3.7V Li-ion / 18650 battery?"
    **A**: A 5V-rated receiver is designed to operate at 5V. A 3.7V Li-ion battery, such as an 18650 cell, is lower than the rated voltage.

    It may cause unstable operation, reduced remote-control distance, or failure to work. For stable performance, use a proper 5V power source for a 5V receiver.

??? question "11. What battery should be used for KR1201A?"
    **A**: Use a suitable 12V power source for KR1201A. A 12V lithium battery can provide better power capacity than ordinary AA batteries.

    Ordinary AA batteries may work if they provide the required voltage, but they usually have lower capacity and may run out quickly. If the device stops working, check whether the battery is drained or whether the receiver has been damaged.

??? question "12. Can a 9V battery power KR1201A?"
    **A**: No. KR1201A is designed for 12V DC power. A 9V battery may light the indicator but may not provide enough voltage for the relay to work correctly.

    Use a proper 12V power source within the specified operating range.

??? question "13. Can two devices be connected using NO and NC?"
    **A**: Yes, the NO and NC terminals can be used according to the relay logic. NO is normally open, and NC is normally closed.

    For example, one load can be connected through NO and another load through NC, so one load is on while the other is off. Make sure the wiring matches the load type and power supply, and avoid short circuits.

??? question "14. Can the negative line be connected to COM for triggering?"
    **A**: In many wiring diagrams, the positive line is connected to COM. However, if you understand the relay principle, the negative line can also be connected to COM in some DC circuits.

    The key rule is that the circuit must not create a short circuit before or after relay triggering.

??? question "15. Can KR1201A control two LED lights so that one is on while the other is off?"
    **A**: Yes, this can be done by using the NO and NC contacts of the relay.

    One LED can be connected through the NO terminal, and the other LED can be connected through the NC terminal. When the relay changes state, one LED turns on and the other turns off.

    For more complex multi-load control, a multi-channel relay receiver is recommended.

??? question "16. How do I reset KR1201A?"
    **A**: For QIACHIP KR1201A, reset is usually performed by pressing the learning button on the receiver 8 times.

    After reset, previously paired remote controls and mode settings may be cleared. Pair the remote controls and set the working mode again after reset.

??? question "17. Does KR1201A have memory storage, such as EEPROM?"
    **A**: Yes. KR1201A has storage memory for paired remote controls and mode settings.

    The module can store up to 20 remote controls.

??? question "18. Can KR1201A be used for access control or automatic residential gates?"
    **A**: KR1201A can provide dry contact control and may be used in some access-control applications.

    Whether it can be used for an automatic residential gate depends on the gate controller's working principle, input requirements, and voltage. For AC 220V systems or higher-power applications, choose a suitable relay receiver designed for that system.


## **KR2202**

!!! note "Keywords"
    Remote control, Programming, Frequency adjustment, Multiple transmitter pairing, Momentary mode, Power interruption, Application scenarios, Simultaneous key press, Battery replacement, Video demonstration

??? question "1. 🔌 Wiring Method"
    **Q**: How did you wire this?

    **A**: I'm glad you asked. Since many people have the same question, I made a detailed video using motor control to demonstrate the working principle.
    
    !!! video
        [How to wire KR2202](https://www.youtube.com/watch?v=o7SbTBAeAIU)
    
    If you still have doubts, feel free to ask. I hope it helps!

??? question "2. 🔋 Power Loss and Reprogramming"
    **Q**: Thanks for the video. I'm wondering, if the electronic board loses power, do I need to reprogram the remote control, or will it work with the last programming?

    **A**: Usually, these devices keep their code and paired remotes even after a power cut. However, a concern is that they may default to the "on" state. If power is restored, it could turn on your heater and pose a fire risk. Also, for remotes with rolling codes, if the battery dies, you'll need to reprogram. The remote starts with a zero code, while the receiver expects a higher rolled - code, causing a mismatch until re - learning. Each battery change requires re - learning the remote!

??? question "3. 📡 Frequency Adjustment"
    **Q**: Hi! I've got the KR2402 working with DC 6 - 30V, but I'm having frequency issues. Can I change the frequency, and how? Thanks.

    **A**: What kind of problems are you facing? If the frequency of the KR2402 changes, the paired remote control (transmitter) must also change its frequency.

??? question "4. 📱 Multiple Remote Pairing"
    **Q**: In momentary mode, can I program multiple transmitters to channels A & B, or is it one transmitter per channel?

    **A**: You can pair multiple transmitters with the receiver. Note: When adding multiple remotes, you don't need to press the receiver's button 8 times before each pairing. Pressing it 8 times resets the receiver and clears all paired remotes.

??? question "5. ⚙️ Automatic Control"
    **Q**: How can the remote (transmitter) work automatically, like for automatic on/off of a submersible pump motor?

    **A**: I'm glad you asked. As many have the same question, I made a video demonstrating the principle using motor control.
    
    !!! video
        [How to automate KR2202](https://www.youtube.com/watch?v=o7SbTBAeAIU)
    
    If you still have questions, ask away. I hope it's useful!

??? question "6. 💡 LED Light Control"
    **Q**: Can it be used with DC to turn on an LED light indoors when it's dark?

    **A**: Yes, if you use the 12V kit.

??? question "7. 🔄 Application Scenarios"
    **Q**: Is it only for LEDs? For pump motor switching, are there design changes needed? Any commercial plans?

    **A**: It's not limited to LEDs. LED control is just a demonstration. You can apply it to other devices.

??? question "8. 🎮 Simultaneous Key Press"
    **Q**: What happens if I press both keys simultaneously in momentary mode? Will only one work, or will both LEDs light up? I need only one channel active at a time to protect the engine.

    **A**: If you press both buttons on the remote at the same time, the receiver won't activate, and neither channel will have an output.

??? question "9. 🔀 Mixed Mode"
    **Q**: Can I use a single remote to control one switch in momentary mode and another in toggle mode?

    **A**: I'm glad you brought this up. Let me confirm: You have two switches and one remote, and you want to control them in different modes, right? In theory, it's possible, but not recommended. Unless the switches are far apart, the remote's signal may interfere with both when activating one. Using two remotes is a better option to avoid interference. I hope this clears your doubt. Share your feedback later!

??? question "10. 🔄 Reset Settings"
    **Q**: Do I need to reset the remote control repeatedly, or will it work with a one - time setup?

    **A**: Check out our new video:
    
    !!! video
        [How to use KR2202 - Updated Guide](https://www.youtube.com/watch?v=EQyKgdRzZOE)
    
    The issue you mentioned doesn't happen in this video. You might have used the wrong method, or our old video didn't explain clearly. Watch the new one, try again, and give us feedback. Thanks!