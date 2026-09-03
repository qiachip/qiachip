---
comments: true
---

# QIACHIP RX480E-1A Instruction Manual DC 2V-5V 433MHz RF Decoding Wireless Receiver Module

![QIACHIP RX480E-1A Product Diagram.webp](QIACHIP_RX480E-1A_Product_Diagram.webp){ width="50%" .center loading="lazy" }

> Version: V1.0
> 

> Last Updated: 2026-07-13
> 

> Model: RX480E-1A
> 

## Product Size

![QIACHIP RX480E-1A Size Figure.webp](QIACHIP_RX480E-1A_Size_Figure.webp){ width="68%" .center loading="lazy" }

- Receiver Length (L) x Width (W) x Height (H): 14.55mm x 12.86mm x 1mm
- Receiver Pin header pitch: 2.5 mm

## Component Description

![QIACHIP RX480E-1A Component Description Figure.webp](QIACHIP_RX480E-1A_Component_Description_Figure.webp){ width="50%" .center loading="lazy" }

<div style="display: flex; flex-wrap: wrap; justify-content: space-around;">
  <ul style="flex: 1 1 45%; margin-right: 1%;">
    <li>1: Indicator light</li>
    <li>2: ANT (Antenna Pin)</li>
    <li>3: GND (Power Ground Pin)</li>
  </ul>
  <ul style="flex: 1 1 45%; margin-left: 1%;">
    <li>4: VCC (Power Input Pin)</li>
    <li>5: OUT (Level Output Pin)</li>
    <li>6: KEY (External Key Input Pin)</li>
  </ul>
</div>

## Wiring Diagram

**When using the RX480E-1A receiver module, an external switch/button must be connected in order to pair the working mode.**

### Figure 1

![QIACHIP RX480E-1A Wiring Diagram 1.webp](QIACHIP_RX480E-1A_Wiring_Diagram_1.webp){ width="50%" .center loading="lazy" }

Figure 1: Wiring diagram for LED light

- Load: LED light
- Input Power: DC 2V-5V

### Figure 2

![QIACHIP RX480E-1A Wiring Diagram 2.webp](QIACHIP_RX480E-1A_Wiring_Diagram_2.webp){ width="50%" .center loading="lazy" }

Figure 2: Wiring diagram for 5V relay

- Load: 5V relay
- Input Power: DC 2V-5V

## Function description and setting method

**(1) Momentary mode; (2) Toggle mode; (3) Latching mode; (4) Reset function; (5) Power-On Auto-Engagement.**

- **Once the receiving module and transmitter are paired and a working mode is set, the receiving module will keep this mode even after power off and power on again.**
- **The following working modes require the use of QIACHIP brand remote controls (transmitters) and controllers (receiving modules/wireless remote control switches). Compatibility with other brands is not guaranteed.**
- **All of the following modes require an external switch/button to be connected to the RX480E-1A receiver module before use.**

### (1) Momentary mode

In this mode:

- Press and hold the button on the transmitter: the output pin of the receiving module outputs a high level and stays high while the button is held down.
- Release the button: the corresponding output pin of the receiving module switches back to a low level.

### How to set momentary mode

**Step 1**

After connecting the external learning button, Click the external learning button connected to the receiving module four times. The LED indicator on the receiving module will flash four times, then stay on, and the receiving module will enter the pairing state.

**Step 2**

Press the button on the transmitter to be paired. The LED indicator on the receiving module will flash and then turn off, indicating that the momentary mode has been set successfully.

### (2) Toggle mode

In this mode:

- Press the matched button on the transmitter: the output pin of the receiving module outputs high level and remains unchanged.
- Press the same button again: the corresponding output pin of the receiving module switches to low level.

### How to set toggle mode

**Step 1**

After connecting the external learning button, Click the external learning button connected to the receiving module twice. The LED indicator on the receiving module will flash twice, then stay on, and the receiving module will enter the pairing state.

**Step 2**

Press any button on the transmitter to be paired. The LED indicator on the receiving module will flash continuously and then turn off, indicating that the toggle mode has been set successfully.

### (3) Latching mode

In this mode:

- The two buttons on the transmitter control the output pin of the receiving module to output high level and low level respectively.
- The first configured button can only control the output pin to output high level, and the second configured button can only control the output pin to output low level.

### How to set latching mode

**Step 1**

After connecting the external learning button, Click the external learning button connected to the receiving module three times. The LED indicator on the receiving module will flash three times, then stay on, and the receiving module will enter the pairing state.

**Step 2**

Press one button on the transmitter to be paired. The LED indicator on the receiving module will flash and then stay on.

**Step 3**

Press another button on the transmitter to be paired. The LED indicator on the receiving module will flash continuously and then turn off, indicating that the latching mode has been set successfully.

### (4) Reset function

When the RX480E-1A receiver module is reset, all paired transmitters will be unpaired and will no longer be able to control the receiver module.

### How to reset

After connecting the external learning button, click the external learning button connected to the receiving module 8 times. The indicator light will flash 8 times and then turn off. The reset will be complete.

### (5) Power-On Auto-Engagement

- After the module is powered off and then powered on again, its output pin directly outputs high level.

### How to set Power-On Auto-Engagement

After connecting an external learning button, press the learning button 6 times. The indicator on the receiving module flashes and then turns off, and the output pin of the receiving module outputs high level.

## Antenna Size

### General Application Type

For general applications, you can directly use the market-standard specifications for the antenna. Details of the 433MHz antenna are as follows:

![QIACHIP RX480E-1A Antenna Size Figure 1.webp](QIACHIP_RX480E-1A_Antenna_Size_Figure_1.webp){ width="50%" .center loading="lazy" }

- Wire length at the soldering end: 10mm
- Total straight length of the antenna wire: 170mm
- Number of winding turns: 9 turns

---

### Special Enhanced Type

If a longer communication distance is required and the general application type antenna cannot meet the demand, an enhanced type antenna can be used to improve the receiving distance.
Details of the 433MHz antenna are as follows:

![QIACHIP RX480E-1A Antenna Size Figure 2.webp](QIACHIP_RX480E-1A_Antenna_Size_Figure_2.webp){ width="50%" .center loading="lazy" }

- Antenna core diameter (including outer sheath): 1.0 mm
- Antenna core diameter (excluding outer sheath): 0.35 mm
- Wire length at the soldering end: 12 mm
- Antenna winding diameter (excluding outer sheath): 3.0 mm
- Number of winding turns: 26 turns
- Winding length: 36 mm

---

## Electrical characteristics

| Parameter | Value |
| --- | --- |
| Input voltage | DC 2.0V-5.0V |
| RF frequency | 433.92MHz |
| Power Consumption | 4.5-6.6mA |
| Receiver sensitivity | -111dBm |
| Working temperature | -10~60℃ |
| Size | 14.55x12.86x1mm |

## NOTE

1. This product is a CMOS device. Please take anti-static precautions during storage, transportation and operation.
2. Ensure proper grounding when using the device.
3. RF devices are voltage-sensitive. If the power supply is unstable or has significant ripple, add filtering at the power input terminal to ensure the supply voltage does not exceed the product’s maximum operating voltage.

## Frequently Asked Questions (Q&A)

**Question 1:** Does RX480E-1A have a Learning button on the module?

**Answer:**

No. RX480E-1A has no Learning button on the module. It has a KEY pin instead.

Connect an external switch or button to the KEY pin before use. All pairing and mode settings use this external button. Without it, you cannot pair a remote control or set a working mode.

**Question 2:** How to set Power-On Auto-Engagement on RX480E-1A?

**Answer:**

Connect an external button to the KEY pin first. Then press the external button 6 times. The indicator on the module flashes and then turns off. The setting is complete.

After this setting, the output pin outputs a high level directly every time the module is powered on.

**Question 3:** Can the RX480E-1A output drive a load directly? How to connect the output to an external transistor or relay?

**Answer:**

We do not recommend connecting the RX480E-1A output to a load directly. It provides a high-level signal, and the maximum output current is 10 mA.

The output needs a transistor to increase the current before driving a relay, motor, or other load. This wiring requires basic circuit design knowledge. You can also follow our wiring diagram directly.

![QIACHIP RX480E-1A 5V relay wiring diagram](QIACHIP_RX480E-1A_Wiring_Diagram_2.webp){ width="68%" .center loading="lazy" }

**Question 4:** Do I need to pair the transmitter and receiver again after a long power outage?

**Answer:**

No. Once the transmitter and receiver are paired, they do not need to be paired again after a power outage.

**Question 5:** Is the RX480E-1A output a high-level or low-level output?

**Answer:**

The RX480E-1A output is a high-level output.

If you need low-level output, add a transistor inverting circuit after the output. This wiring requires basic circuit design knowledge.

**Question 6:** Is Momentary mode the factory default output mode for RX480E-1A?

**Answer:**

No. RX480E-1A has no factory default mode. Connect an external button to the KEY pin, then choose the mode you need. You can find the pairing steps in the Function description and setting method section above.

**Question 7:** Does the RX480E-1A receiver support EV1527 encoding? Can it pair with other EV1527 remote controls?

**Answer:**

Yes. The RX480E-1A receiver uses EV1527 learning code. Pair the remote control and receiver once before use.

We recommend QIACHIP remotes. We do not guarantee pairing compatibility with other-brand remotes.
