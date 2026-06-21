---
comments: true
---

# QIACHIP KR1201MINI-V03 ( KR1201 Series ) Instruction Manual DC 3.3V-24V 433MHz RF Remote Control Module Receiver

![QIACHIP KR1201MINI-V03 Product Diagram.webp](QIACHIP_KR1201MINI-V03_Product_Diagram.webp){ width="50%" .center loading="lazy" }

> Version: V1.0
> 
> Last Updated: 2026-3-27
> 
> Model: KR1201MINI-V03 ( KR1201 Series )

## Product Size

![QIACHIP KR1201MINI-V03 Size Figure.webp](QIACHIP_KR1201MINI-V03_Size_Figure.webp){ width="68%" .center loading="lazy" }

- Receiver Length (L) x Width (W) x Height (H): 31mm x 14mm x 7mm

## Component Description

![QIACHIP KR1201MINI-V03 Component Description Figure.webp](QIACHIP_KR1201MINI-V03_Component_Description_Figure.webp){ width="50%" .center loading="lazy" }

<div style="display: flex; flex-wrap: wrap; justify-content: space-around;">
  <ul style="flex: 1 1 45%; margin-right: 1%;">
    <li>1: Antenna</li>
    <li>2: Learning button</li>
    <li>3: Indicator light</li>
    <li>NO: Normally open terminal</li>
  </ul>
  <ul style="flex: 1 1 45%; margin-left: 1%;">
    <li>COM: Common terminal</li>
    <li>NC: Normally closed terminal</li>
    <li>DC+: Positive Input terminal</li>
    <li>DC-: Negative Input terminal</li>
  </ul>
</div>

## Wiring Diagram

Disconnect power before wiring.

### Figure 1

![QIACHIP KR1201MINI-V03 Wiring Diagram 1.webp](QIACHIP_KR1201MINI-V03_Wiring_Diagram_1.webp){ width="68%" .center loading="lazy" }

Figure 1: Wiring diagram for LED Lamp

- Load: LED Lamp
- Input Power: DC 3.3V-24V Max: 1A

### Figure 2

![QIACHIP KR1201MINI-V03 Wiring Diagram 2.webp](QIACHIP_KR1201MINI-V03_Wiring_Diagram_2.webp){ width="68%" .center loading="lazy" }

Figure 2: Wiring diagram for Button switch

- Load: LED Lamp
- Input Power: DC 3.3V-24V Max: 1A

## Function description and setting method

**(1) Momentary mode; (2) Toggle mode; (3) Latching mode; (4) Delay mode; (5) Reset function.**

- **When you use the third working mode, a remote control with at least two buttons is required.**
- **When pairing a second remote, you don't need to press the button on the receiver 8 times again to reset it.**
- **Once the receiver and transmitter are paired and a working mode is selected, the receiver will retain this mode even if powered off and on again.**
- **The following working modes require the use of QIACHIP brand remote controls (transmitters) and controllers (receivers/wireless remote control switches). Compatibility with other brands is not guaranteed.**

### (1) Momentary mode

In this mode:

- Press and hold the remote control button (such as A), and the corresponding relay on the receiver will turn on.
- Release the remote control button (such as A), and the corresponding relay on the receiver will turn off.

### How to set momentary mode

**Step 1**

Click the learning button of the receiver once. The indicator light on the receiver will turn on, and the receiver will enter the setting state.

**Step 2**

Press the button on the remote control (such as A) once. The indicator light on the receiver will flash and then will turn off. The momentary mode will be set successfully.

### (2) Toggle mode

In this mode:

- Press the remote control button (such as A), and the corresponding relay on the receiver will turn on.
- Press the remote control button (such as A) again, and the corresponding relay on the receiver will turn off.

### How to set toggle mode

**Step 1**

Click the learning button of the receiver twice. The indicator light on the receiver will turn on, and the receiver will enter the setting state.

**Step 2**

Press the button on the remote control (such as A) once. The indicator light on the receiver will flash and then will turn off. The toggle mode will be set successfully.

### (3) Latching mode

In this mode:

- Press the remote control button (such as A), and the receiver's relay will turn on.
- Press the remote control button (such as B), and the receiver's relay will turn off.

### How to set latching mode

**Step 1**

Click the learning button of the receiver three times. The indicator light on the receiver will turn on, and the receiver will enter the setting state.

**Step 2**

Press the button on the remote control (such as A) once. The indicator light on the receiver will flash and then will turn on.

**Step 3**

After the indicator light turns on, press another button (such as B) on the same remote control. The indicator light on the receiver will flash and then turn off. The latching mode will be set successfully.

### (4) Delay mode

In this mode:

- Press the remote control button (such as A), and the corresponding relay of the receiver will enter delay mode.

### How to set delay mode

**Step 1**

Click the learning button of the receiver 4 times. The indicator light on the receiver will turn on, and the receiver will enter the setting state.

(Press the receiver button **4 times**: The corresponding relay will close after a 5-second delay);

(Press the receiver button **5 times**: The corresponding relay will close after a 10-second delay);

(Press the receiver button **6 times**: The corresponding relay will close after a 15-second delay);

(Press the receiver button **7 times**: The corresponding relay will close after a 20-second delay).

**Step 2**

Press the button on the remote control (such as A) once. The indicator light on the receiver will flash and then turn off. The delay mode will be set successfully.

### (5) Reset function

- When the KR1201MINI-V03 receiver is reset, all paired transmitters will be unpaired and will no longer be able to control the receiver.

### How to reset

Click the learning button on the receiver 8 times. The indicator light will flash and then will turn off. The reset will be complete.

## Electrical characteristics

| Parameter | Value |
| --- | --- |
| Input voltage | DC 3.3V-24V |
| RF frequency | 433.92MHz |
| Relay max contact current |  1A |
| Quiescent Current | 5.0mA ~ 5.5mA |
| Receiver sensitivity | -100dBM |
| Operation mode | Momentary mode/Toggle mode/Latching mode/Delay mode |
| Working temperature | -20~80°C |
| Size | 31x14x7mm |

## Warning

- The positive and negative terminal wires must not be reversed.
- When using wireless electronic devices, avoid proximity to metal objects, large electronic equipment, electromagnetic fields, and other sources of strong interference.
