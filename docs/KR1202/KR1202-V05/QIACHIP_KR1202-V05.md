---
comments: true
---

# QIACHIP KR1202-V05 ( KR1202 Series ) Instruction Manual DC 5V-60V 433MHz RF Wireless Motor Control Module Relay Receiver

![QIACHIP KR1202-V05 Product Diagram.webp](QIACHIP_KR1202-V05_Product_Diagram.webp){ width="50%" .center loading="lazy" }

> Version: V1.0
> 

> Last Updated: 2026-01-20
> 

> Model: KR1202-V05 ( KR1202 Series )
> 

## Product Size

![QIACHIP KR1202-V05 Size Figure.webp](QIACHIP_KR1202-V05_Size_Figure.webp){ width="68%" .center loading="lazy" }

- Receiver Length (L) x Width (W) x Height (H): 68mm x 48mm x 16mm
- Housing Length (L) x Width (W) x Height (H): 75mm x 54mm x 25mm
- Receiver hole horizontal spacing: 60mm; Vertical spacing: 42mm; Hole Diameter: Ø4mm

## Component Description

![QIACHIP KR1202-V05 Component Description Figure.webp](QIACHIP_KR1202-V05_Component_Description_Figure.webp){ width="50%" .center loading="lazy" }

<div style="display: flex; flex-wrap: wrap; justify-content: space-around;">
  <ul style="flex: 1 1 45%; margin-right: 1%;">
    <li>1: Learning button</li>
    <li>2: Antenna</li>
    <li>3: Indicator light</li>
  </ul>
  <ul style="flex: 1 1 45%; margin-left: 1%;">
    <li>Input GND : Negative input terminal</li>
    <li>Input +V: Positive input terminal</li>
    <li>Output M1: Motor control terminal 1</li>
    <li>Output M2: Motor control terminal 2</li>
  </ul>
</div>

## Wiring Diagram

Disconnect power before wiring.

### Figure 1

![QIACHIP KR1202-V05 Wiring Diagram.webp](QIACHIP_KR1202-V05_Wiring_Diagram.webp){ width="50%" .center loading="lazy" }

Figure 1: Wiring diagram for DC motors

- Load: DC motors
- Input Power: DC 5V-60V

---

## Function description and setting method

**(1) Momentary mode; (2) Toggle mode; (3) Latching mode; (4) Reset function.**

**NOTE**

- **This product requires a remote control with at least two buttons. For the third mode, a remote control with at least three buttons is required.**
- **M1 and M2 are independent motor control terminals with no fixed forward/reverse assignment. Their actual function is determined by your external wiring configuration.**
- **When pairing a second remote, you don't need to press the button on the receiver 8 times again to reset it.**
- **Once the receiver and transmitter are paired and a working mode is selected, the receiver will retain this mode even if powered off and on again.**
- **The following working modes require the use of QIACHIP brand remote controls (transmitters) and controllers (receivers). Compatibility with other brands is not guaranteed.**

### (1) Momentary mode

In this mode: 

- Press and hold the remote control button (such as A) to rotate the motor forward; release the remote control button to stop.
- Press and hold the remote control button (such as B) to rotate the motor backward; release the remote control button to stop.

### How to set momentary mode

**Step 1**

Click the learning button of the receiver once. The indicator light on the receiver will turn off, and the receiver will enter the setting state.

**Step 2**

Press the button on the remote control (such as A) once. The indicator light on the receiver will flash and then will turn off.

**Step 3**

After the indicator light turns off, press another button (such as B) on the same remote control. The indicator light on the receiver will flash and then turn on. The momentary mode will be set successfully.

### (2) Toggle mode

In this mode: 

- Press the remote control button (such as A), and the motor rotates forward. Press button A again, and the motor stops.
- Press the remote control button (such as B), and the motor rotates backward. Press button B again, and the motor stops.

### How to set toggle mode

**Step 1**

Click the learning button of the receiver twice. The indicator light on the receiver will turn off, and the receiver will enter the setting state.

**Step 2**

Press the button on the remote control (such as A) once. The indicator light on the receiver will flash and then will turn off.

**Step 3**

After the indicator light turns off, press another button (such as B) on the same remote control. The indicator light on the receiver will flash and then turn on. The Toggle mode will be set successfully.

### (3) Latching mode

In this mode:

- Press the remote control button (such as A), and the receiver's relay will turn on.
- Press the remote control button (such as B), and the receiver's relay will turn off.

### How to set latching mode

**Step 1**

Click the learning button of the receiver three times. The indicator light on the receiver will turn off, and the receiver will enter the setting state.

**Step 2**

Press the button on the remote control (such as A) once. The indicator light on the receiver will flash and then will turn off.

**Step 3**

After the indicator light turns off, press another button (such as B) on the same remote control. The indicator light on the receiver will flash and then will turn off.

**Step 4**

After the indicator light turns off, press another button (such as C) on the same remote control. The indicator light on the receiver will flash and then turn on. The latching mode will be set successfully.

### (4) Reset function

- When the KR1202-V05 receiver is reset, all paired transmitters will be unpaired and will no longer be able to control the receiver.

### How to reset

Click the learning button on the receiver 8 times. The indicator light will flash and then will turn on. The reset will be complete.

## Electrical characteristics

| Parameter | Value |
| --- | --- |
| Input voltage | DC 5V-60V |
| RF frequency | 433.92MHz |
| Relay max contact current | 10A |
| Rated Load | Max 600W  |
| Receiver sensitivity | -97dBm |
| Operation mode | Momentary mode/Toggle mode/Latching mode |
| Working temperature | -20℃~+80℃ |
| Size | 68x48x16mm |

## Warning

- The positive and negative terminal wires must not be reversed.
- When using wireless electronic devices, avoid proximity to metal objects, large electronic equipment, electromagnetic fields, and other sources of strong interference.
