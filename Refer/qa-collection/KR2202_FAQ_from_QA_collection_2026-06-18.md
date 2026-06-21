# KR2202 QA Collection Bilingual Translation / KR2202 QA 收集表双语翻译版

> The Chinese text below is a faithful translation of the collected source content.
> For abbreviated rows, the translation follows the exact excerpt shown in the source table and does not expand the text.
> Optimized answers are based on the KR2202 online instruction manual and use manual terminology where possible.

## Source / 来源

- **Based on:** User-provided KR2202 QA collection table
- **Manual reference:** https://qiachip.github.io/qiachip/KR2202/QIACHIP_KR2202/
- **Original format:** ID / Question / Answer
- **Prepared date:** 2026-06-18
- **Purpose:** Provide bilingual translation and optimized bilingual answers for reference and manual drafting.

## Frequently Asked Questions / 常见问题

### 1. 遥控兼容性与配对 / Remote Compatibility and Pairing

#### Q1 (Source ID 38): KR2202 可以使用非 QIACHIP 遥控器吗？

**Question 中文翻译：**

在设置一款新的无线遥控器时，型号为“QIACHIP Funkschalter 220V 230V Funkfernbedienung Garagentor Schalter 2 Kanäl 433MHz RF 10A Drahtloser Relais Empfänger mit 4 Sender für Motor,...”

**Answer 中文翻译：**

所描述的型号对应 KR2202（AC 110V 220V 433MHz RF Remote Control Switch 2-CH Relay Receiver）。要进行设置，你需要选择其中一种工作模式，将遥控器与接收器配对。请确保使用 QIACHIP 品牌遥控器，因为不保证与其他品牌兼容。

**Approved standard answer 中文：**

该产品对应 QIACHIP KR2202，即 AC 110V / 220V、433.92MHz RF、2-CH Relay Receiver。设置时请先选择需要的 Operation mode：Momentary mode、Toggle mode 或 Latching mode，然后通过 receiver 上的 Learning button 进行配对。

KR2202 的工作模式建议搭配 QIACHIP brand remote controls（transmitters）和 QIACHIP receiver / wireless remote control switch 使用；其他品牌 transmitter 的编码方式可能不同，兼容性不保证。设置 Momentary mode 或 Toggle mode 时，遥控器至少需要 2 个按键；设置 Latching mode 时，遥控器至少需要 3 个按键。

**Approved standard answer English:**

The described product corresponds to the QIACHIP KR2202, an AC 110V / 220V, 433.92MHz RF, 2-CH relay receiver. To configure it, first select the required operation mode: Momentary mode, Toggle mode, or Latching mode. Then pair the transmitter with the receiver using the receiver's Learning button.

For reliable operation, use QIACHIP brand remote controls (transmitters) with the QIACHIP receiver / wireless remote control switch. Compatibility with transmitters from other brands is not guaranteed because the RF coding method may differ. Momentary mode and Toggle mode require a remote control with at least two buttons; Latching mode requires a remote control with at least three buttons.

**Original question:**

> When setting up a new radio remote control "Model: QIACHIP Funkschalter 220V 230V Funkfernbedienung Garagentor Schalter 2 Kanäl 433MHz RF 10A Drahtloser Relais Empfänger mit 4 Sender für Motor,..."

**Original answer:**

> The model described corresponds to the KR2202 (AC 110V 220V 433MHz RF Remote Control Switch 2-CH Relay Receiver). To set it up, you need to pair the remote control with the receiver by selecting one of the working modes. Ensure you are using QIACHIP brand remote controls, as compatibility with other brands is not guaranteed.

#### Q2 (Source ID 22): 3 键 UP / STOP / DOWN 遥控器在 toggle mode 下为什么不工作？

**Question 中文翻译：**

你好，它不工作。我想要 toggle mode。我有一个 3 键遥控器：UP、STOP 和 DOWN。STOP 键完全没有功能。当 relay 1 被激活并且我按下……

**Answer 中文翻译：**

他可能需要第三种模式（interlock），但他设置成了第二种模式（self-lock）。我让他更改模式，并告诉了他具体步骤和注意事项。他一直说他照做了，但仍然无法解决问题……

**Approved standard answer 中文：**

如果你希望 UP / STOP / DOWN 分别实现“上行 / 停止 / 下行”这类电机控制逻辑，Toggle mode 通常不是最合适的模式。根据 KR2202 说明书，Toggle mode 的逻辑是：按一次 remote control button，对应 relay on；再次按同一按钮，对应 relay off。

对于 3 键遥控器，更接近的模式是 Latching mode：按 A 时 relay A on；按 B 时 relay B on，同时 relay A off；按 C 时当前已激活的 relay off。设置 Latching mode 时，remote control 至少需要 3 个按键。建议先 reset receiver，再按 Latching mode 的步骤重新配对，并确认每一步都等到 indicator light flash / off / on 后再按下一个按键。

**Approved standard answer English:**

If you want the UP / STOP / DOWN buttons to work as motor direction and stop commands, Toggle mode is usually not the correct operation mode. According to the KR2202 manual, Toggle mode works as follows: press a remote control button once and the corresponding relay turns on; press the same button again and the corresponding relay turns off.

For a 3-button transmitter, Latching mode is normally the better match. In Latching mode, pressing button A turns relay A on; pressing button B turns relay B on while relay A turns off; pressing button C turns off the currently activated relay. Latching mode requires a remote control with at least three buttons. Reset the receiver if necessary, then set Latching mode again and wait for the indicator light to flash / turn off / turn on at each step before pressing the next button.

**Original question (source table excerpt):**

> Hello, it does not work. I want toggle mode. I have a remote control with 3 buttons: UP, STOP and DOWN. The STOP button has no function at all. When relay 1 is activated and I press...

**Original answer (source table excerpt):**

> He probably needs the third mode (interlock), but he set the second mode (self-lock). I asked him to change the mode and told him the specific steps and precautions. He kept saying he did it but still couldn't solve the problem...

#### Q3 (Source ID 28): 可以让一个遥控器控制 Relay 1，另一个遥控器控制 Relay 2 吗？

**Question 中文翻译：**

你好，我在 Amazon 上买了一个 2-channel remote control receiver（型号 KR2202）。我收到了接收器和 2 个遥控器。但我想让一个遥控器激活 relay 1，另一个遥控器激活 relay 2。我该怎么做？

**Answer 中文翻译：**

你好，
双通道接收器有工作模式：两个继电器必须分别分配给不同的按钮。
例如，Toggle mode：
按接收器上的学习键 2 次。等待 3 秒；
按遥控器上的“A”键。等待 3 秒。
然后按“B”键来分配第二个继电器，依此类推。

**Approved standard answer 中文：**

可以的，KR2202 是 2-CH relay receiver，两个 relay channel 需要在同一次 mode setting 流程中分别绑定到两个不同的 transmitter button。以 Toggle mode 为例：先按 receiver 上的 Learning button 2 次，indicator light 熄灭后进入 setting state；按第一个遥控器上用于控制 Relay 1 的按钮，等待 indicator light flash 后再次熄灭；再按第二个遥控器上用于控制 Relay 2 的按钮，indicator light flash 后点亮，表示 Toggle mode 设置完成。

如果已经配错，先按 Learning button 8 次执行 Reset function。Reset 后，所有已配对的 transmitters 都会被清除，需要重新设置工作模式和配对按钮。

**Approved standard answer English:**

Yes, the KR2202 is a 2-CH relay receiver, so the two relay channels must be assigned to two different transmitter buttons during the same mode-setting sequence. For example, in Toggle mode, click the Learning button on the receiver twice. When the indicator light turns off, the receiver enters the setting state. Press the button on the first remote that you want to use for Relay 1, then wait for the indicator light to flash and turn off again. Press the button on the second remote that you want to use for Relay 2. When the indicator light flashes and then turns on, Toggle mode has been set successfully.

If the buttons were assigned incorrectly, click the Learning button 8 times to perform the Reset function. After reset, all paired transmitters will be cleared, and the operation mode and transmitter buttons must be paired again.

**Original question:**

> Hello, I bought a 2-channel remote control receiver (model KR2202) on Amazon. I received the receiver and 2 remotes. But I would like one remote to activate relay 1 and the other remote to activate relay 2. How can I do that?

**Original answer:**

> Hello,
> The dual-channel receiver has working modes: the two relays must be assigned to different buttons respectively.
> For example, Toggle mode:
> Press the learning button twice (on the receiver). Wait 3 seconds;
> Press the "A" button on the remote. Wait 3 seconds.
> Then press the "B" button to assign the second relay, etc.

#### Q4 (Source ID 48): 可以自定义遥控器按键标签吗？

**Question 中文翻译：**

是否有办法“自定义”这些遥控器，例如我希望按钮写成 up/down、in/out，或者带箭头？

**Answer 中文翻译：**

所提供的文档没有提到遥控器按键标签的自定义选项。对于实体遥控器，你通常需要购买带有这些标签的特定型号。不过，由于 KR2202 允许你在配对过程中将遥控器上的任意按键分配给特定继电器功能，因此你可以在逻辑上分配按键，使其与你想要的动作匹配（例如，将“UP”键分配给 Relay 1，将“DOWN”键分配给 Relay 2）。

**Approved standard answer 中文：**

我们有多种标签供你选择，如果你需要自定义，那么需要有一定的起订数量

**Approved standard answer English:**

We offer a variety of labels for you to choose from. If you require customization, there is a minimum order quantity.

**Original question:**

> Is there a way to "customize" the remotes, for example if i wanted the buttons to say up/down, in/out or have arrows?

**Original answer:**

> The provided documentation does not mention customization options for remote control button labels. For physical remote controls, you would typically need to purchase a specific model with those labels. However, since the KR2202 allows you to assign any button on the remote to a specific relay function during the pairing process, you can logically assign the buttons to match your desired actions (e.g., assigning an "UP" button to Relay 1 and a "DOWN" button to Relay 2).

#### Q5 (Source ID 49): 如何让 A 控制 Relay 1、B 控制 Relay 2，并且都用 momentary mode？

**Question 中文翻译：**

我怎样才能让 button a 控制 relay 1，让 button b 控制 relay 2，而且两者都在 momentary mode？我在尝试做一个电机双向控制。

**Answer 中文翻译：**

你好，只需按照下面的步骤进行配对。
按学习键 1 次（在接收器上）。等待 3 秒；
按遥控器上的“A”键。等待 3 秒。
按“B”键……

**Approved standard answer 中文：**

可以。设置 Momentary mode 时，请按以下流程操作：按 receiver 上的 Learning button 1 次，indicator light 熄灭后进入 setting state；按 remote control 上的 A 键一次，等待 indicator light flash 后熄灭；再按同一遥控器上的 B 键一次，indicator light flash 后点亮，表示 Momentary mode 设置成功。

在 Momentary mode 下，按住 remote control button 时，对应 relay on；松开按钮后，对应 relay off。用于电机双向控制时，请确认接线符合 KR2202 的 Wiring diagram for AC motors 或 Wiring diagram for DC motors，并确保正反转电路不会同时导通。负载不得超过 Rated Load Max 1100W。

**Approved standard answer English:**

Yes. To set Momentary mode, click the Learning button on the receiver once. When the indicator light turns off, the receiver enters the setting state. Press button A on the remote control once and wait for the indicator light to flash and turn off. Then press button B on the same remote control once. When the indicator light flashes and then turns on, Momentary mode has been set successfully.

In Momentary mode, the corresponding relay turns on only while the remote control button is pressed and held. When the button is released, the relay turns off. For two-direction motor control, make sure the wiring follows the KR2202 Wiring diagram for AC motors or Wiring diagram for DC motors, and ensure that the forward and reverse circuits cannot be energized at the same time. The load must not exceed the Rated Load: Max 1100W.

**Original question:**

> How do i get button a to control relay 1 and button b to control relay 2 both in momentary mode? Trying to do a motor in 2 directions.

**Original answer (source table excerpt):**

> Hello, simply follow the steps below to pair them.
> Press the learning button 1 times (on the receiver). Wait 3 seconds;
> Press the "A" button on the remote control. Wait 3 seconds.
> Press the "B" button...

### 2. 电机、门机与闸机控制 / Motor, Door, and Gate Control

#### Q6 (Source ID 26): 一台遥控器可以控制一台双向电机或两台单向电机吗？

**Question 中文翻译：**

这台接收器是安装在一个地方，用同一个遥控器先打开一扇车库门，然后再打开另一扇门。我想用一个遥控器配置两个不同的电机，可以吗？

**Answer 中文翻译：**

你好，你的电机是单向的还是可反转的？
套装中包含的接收器可以连接一台可反转电机，或者连接两台单向电机。

**Approved standard answer 中文：**

KR2202 是 2-CH relay receiver，带有 NO（Normally open terminal）、COM（Common terminal）和 NC（Normally closed terminal）relay terminals。它可以用于一台可正反转电机，也可以用于两个单向负载 / 单向电机，前提是接线方式与电机控制需求匹配。

如果控制一台可反转电机，请按说明书中的 Wiring diagram for AC motors 或 Wiring diagram for DC motors 接线，并确保电机本身或外部控制电路具备限位和互锁保护。如果控制两台单向电机，需要分别确认每台电机的 voltage、current 和 starting current，且总应用不能超过 KR2202 的 Rated Load Max 1100W。

**Approved standard answer English:**

The KR2202 is a 2-CH relay receiver with NO (Normally open terminal), COM (Common terminal), and NC (Normally closed terminal) relay contacts. It can be used for one reversible motor or for two one-direction loads / one-direction motors, provided that the wiring matches the required motor-control logic.

For a reversible motor, follow the KR2202 Wiring diagram for AC motors or Wiring diagram for DC motors, and make sure the motor or external control circuit includes proper limit and interlock protection. For two one-direction motors, verify each motor's voltage, current, and starting current. The application must remain within the KR2202 Rated Load: Max 1100W.

**Original question:**

> This receiver is for installing in one place to open one garage door and then another, with the same remote. I want to configure two different motors with a single remote, is that possible?

**Original answer:**

> Hello, are your motors unidirectional or reversible?
> The receiver included in the kit can be connected to one reversible motor or to two unidirectional motors.

#### Q7 (Source ID 55): 可以用 KR2202 做闸机开 / 关控制吗？

**Question 中文翻译：**

尊敬的先生 / 女士：
我从你们那里买了一个用于闸机控制的继电器，并且有一个关于接线和配置的问题。
我想让遥控器的 button A 打开闸门，button B 关闭闸门，而且两者都使用 momentary mode。这可以吗？

**Answer 中文翻译：**

你好！
你希望使用发射器上的两个按钮，以 Momentary mode 控制两扇独立的门，是这样吗？
首先，KR2202 是一个 dry contact 模块。如果你的门控制系统是……

**Approved standard answer 中文：**

可以，但要看 gate controller 的控制输入类型。KR2202 的 relay output 是通过 NO / COM / NC terminals 提供的 dry contact relay output。如果你的门机或闸机控制器支持 dry contact input（例如独立的 OPEN / CLOSE / STOP 端子），可以用 KR2202 的两个 relay channel 分别触发 open 和 close 命令。

如果你希望 button A 打开、button B 关闭，并且只在按住时动作，建议使用 Momentary mode：按住对应 remote control button 时 relay on，松开后 relay off。接线前必须 disconnect power，并按照门机控制器说明书确认 COM / NO 接法。不要把 KR2202 直接接到不支持 dry contact input 的控制端子上。

**Approved standard answer English:**

Yes, but it depends on the input type of the gate controller. The KR2202 provides dry contact relay output through the NO / COM / NC terminals. If your gate controller supports dry contact input terminals, such as separate OPEN / CLOSE / STOP inputs, the two relay channels of the KR2202 can be used to trigger the open and close commands.

If you want button A to open and button B to close, and you want the command to be active only while the button is pressed, use Momentary mode. In Momentary mode, the corresponding relay turns on while the remote control button is held and turns off when the button is released. Disconnect power before wiring, and confirm the COM / NO wiring according to the gate controller manual. Do not connect the KR2202 directly to terminals that are not designed for dry contact input.

**Original question:**

> Dear Sir/Madam,
> I bought a relay for gate control from you and have a question about connection and configuration.
> I want button A of the remote control to open the gate and button B to close it, both in momentary mode. Is that possible?

**Original answer (source table excerpt):**

> Hello!
> You wish to use the two buttons on the transmitter to control two separate doors in Momentary mode, is that correct?
> Firstly, the KR2202 is a dry contact module. If your door control system is ...

#### Q8 (Source ID 46): KR2202 适合控制卷帘门吗？

**Question 中文翻译：**

它适合打开和关闭车库卷帘门吗？

**Answer 中文翻译：**

是的，KR2202 接收器适合控制 AC 电机（例如车库卷帘门），这在其“Wiring diagram for AC motors”中有说明。在这种应用中，建议将接收器设置为 Momentary mode（如果你的电机控制器负责处理限位），或者设置为 Latching mode（button A 打开 / relay A 导通，button B 关闭 / relay B 导通并且 relay A 断开），并确保分别使用至少 2 键或 3 键遥控器。

**Approved standard answer 中文：**

KR2202 可以用于控制符合规格的 AC motor 应用，包括部分 garage shutter / roller shutter 场景。说明书中提供了 Wiring diagram for AC motors，输入电源为 AC 85V-250V，Rated Load 为 Max 1100W。

如果卷帘门控制器或电机系统已经带有限位保护，通常建议使用 Momentary mode，让 relay 只在按住按钮时导通。如果需要两个方向互锁，可考虑 Latching mode：button A 对应 relay A on，button B 对应 relay B on 且 relay A off，button C 关闭当前激活的 relay。接线时必须确保 L / N wires must not be reversed，并避免靠近强电磁干扰源。

**Approved standard answer English:**

The KR2202 can be used for compatible AC motor applications, including some garage shutter / roller shutter systems. The manual provides a Wiring diagram for AC motors. The input power is AC 85V-250V, and the Rated Load is Max 1100W.

If the shutter motor or motor controller already has limit protection, Momentary mode is usually recommended so that the relay is energized only while the button is held. If two-direction interlocking is required, Latching mode may be used: button A turns relay A on, button B turns relay B on while relay A turns off, and button C turns off the currently activated relay. During wiring, L and N wires must not be reversed, and the receiver should be kept away from strong electromagnetic interference sources.

**Original question:**

> Is it suitable for opening and closing the garage shutter?

**Original answer:**

> Yes, the KR2202 receiver is suitable for controlling AC motors (such as garage shutters) as indicated in its "Wiring diagram for AC motors". In this application, it is recommended to set the receiver to Momentary mode (if your motor controller handles the limits) or Latching mode (where button A opens/relay A is on, and button B closes/relay B is on and relay A is off), ensuring you use a remote with at least 2 or 3 buttons respectively.

#### Q9 (Source ID 47): 可以接 selector switch 控制电机方向吗？

**Question 中文翻译：**

它可以连接一个用于电机运动的 selector switch 吗？

**Answer 中文翻译：**

文档没有提供连接实体 selector switch 的具体说明。KR2202 设计为通过 433.92MHz RF 遥控器（发射器）进行无线控制。不过，你可以通过将接收器配置为 Momentary mode 或 Latching mode，使用遥控器按钮来选择电机的运动方向。

**Approved standard answer 中文：**

KR2202 本身没有专用的 wired selector switch input。它的控制方式是通过 433.92MHz RF transmitter 向 receiver 发送信号，再由 receiver 控制 relay contacts（NO / COM / NC）。因此，不能把普通 selector switch 当作遥控输入直接接到 KR2202 上。

如果你的电机控制器支持 dry contact command input，可以让 KR2202 的 relay output 代替或并联到外部控制输入，用 remote control button 实现方向选择。具体能否连接 selector switch，要以电机控制器的接线说明为准，而不是直接改动 KR2202 的 Learning button 或内部电路。

**Approved standard answer English:**

The KR2202 does not provide a dedicated wired selector-switch input. It is designed to receive commands from a 433.92MHz RF transmitter and then switch the relay contacts (NO / COM / NC) on the receiver. Therefore, a standard selector switch cannot be connected directly to the KR2202 as a remote input.

If your motor controller supports dry contact command inputs, the KR2202 relay output can be used to replace or parallel an external control input, allowing the remote control buttons to select motor direction. Whether a physical selector switch can also be used depends on the wiring design of the motor controller. Do not modify or wire into the KR2202 Learning button or internal circuit for this purpose.

**Original question:**

> Can it be connected to a selector switch for motor movement?

**Original answer:**

> The documentation does not provide specific instructions for connecting a physical selector switch. The KR2202 is designed to be controlled wirelessly via a 433.92MHz RF remote control (transmitter). You can, however, use the remote control buttons to select the motor's movement direction by configuring the receiver into Momentary mode or Latching mode.

### 3. 接线、负载与安全 / Wiring, Load, and Safety

#### Q10 (Source ID 23): 220V 接线端子和线径安全吗？

**Question 中文翻译：**

继电器端子排太小了，不符合国外电缆标准；用于 220V 是不安全的。
另外：
输入到闸机的电缆必须至少是 0.75mm²。
然后开关里使用的是“很小”的端子。低压可以，……

**Answer 中文翻译：**

KR2202 的最大额定负载为 1100W，输入电压为 AC 85V-250V。请确保你的接线符合当地针对所用具体负载和电压的电气安全标准。请注意，L 和 N 线不能接反。

**Approved standard answer 中文：**

KR2202 的 Electrical characteristics 标注为 Input voltage AC 85V-250V、Rated Load Max 1100W。用于 AC 220V / 230V 场景时，接线必须符合当地 electrical safety standards 和线径要求，并由具备资质的人员安装。

如果现场要求输入电缆至少 0.75mm²，而 receiver terminal block 无法安全夹紧该线径，不应强行接入。应使用符合规范的 junction box、端子排、端子转换件或其他合规接线方式。接线前必须 disconnect power；L（Live wire）和 N（Neutral wire）must not be reversed；所有导线都必须可靠固定，避免松动、过热或短路。

**Approved standard answer English:**

The KR2202 electrical characteristics specify Input voltage: AC 85V-250V and Rated Load: Max 1100W. For AC 220V / 230V applications, wiring must comply with local electrical safety standards and conductor-size requirements, and installation should be performed by a qualified person.

If the installation requires input cables of at least 0.75mm² and the receiver terminal block cannot securely clamp that conductor size, do not force the wire into the terminal. Use a compliant junction box, terminal block, terminal adapter, or other approved wiring method. Disconnect power before wiring. L (Live wire) and N (Neutral wire) must not be reversed. All conductors must be securely fixed to prevent looseness, overheating, or short circuit.

**Original question:**

> The relay terminal blocks are too small and do not meet foreign cable standards; it is unsafe for 220V.
> Also:
> Input cables to the gate must be at least 0.75mm².
> Then the "small" terminals in the switch are used. Low voltage is OK,...

**Original answer:**

> The KR2202 has a maximum rated load of 1100W and an input voltage of AC 85V-250V. Please ensure your wiring complies with local electrical safety standards for the specific load and voltage used. Note that L and N wires must not be reversed.

#### Q11 (Source ID 30): 负载接上后为什么会出问题？

**Question 中文翻译：**

你好，我买了你们的无线开关来控制一个泳池盖。空载时，按遥控器按钮工作正常，但当我接上负载时……

**Answer 中文翻译：**

请检查你的接线和负载规格。根据说明书，AC 电机的接线图要求将 live wire（L）和 neutral wire（N）连接到输入端，并将 AC 电机连接到 NO 和 COM 端子。请确保负载不超过最大 1100W 额定负载，并且 L 和 N 线没有接反。同时，避免靠近金属物体、大型电子设备或可能在带负载情况下造成干扰的电磁场。

**Approved standard answer 中文：**

如果空载时 receiver 和 transmitter 工作正常，但接入 pool cover motor 或其他负载后异常，通常需要重点检查 wiring、load rating 和 motor starting current。KR2202 的 Input power 为 AC 85V-250V，Rated Load 为 Max 1100W。AC motor 应按说明书中的 Wiring diagram for AC motors 接线：L / N 接输入端，负载通过 NO / COM relay terminals 控制；L and N wires must not be reversed。

还需要确认电机的运行功率和启动电流没有超过 relay contact 能力。电机类负载启动瞬间电流通常高于正常运行电流，即使额定功率看起来不高，也可能导致 relay 触点或电源侧异常。安装时避免 receiver 靠近金属物体、大型电子设备、电机强电磁场或其他 interference sources。如仍异常，应由具备资质的电工检查实际接线和负载参数。

**Approved standard answer English:**

If the receiver and transmitter work correctly with no load, but the system fails when the pool cover motor or another load is connected, check the wiring, load rating, and motor starting current first. The KR2202 input power is AC 85V-250V, and the Rated Load is Max 1100W. For an AC motor, follow the Wiring diagram for AC motors: connect L / N to the input power terminals, and switch the load through the NO / COM relay terminals. L and N wires must not be reversed.

Also verify that the motor running power and starting current do not exceed the relay contact capacity. Motor loads often draw a starting current higher than their normal running current, so a motor can overload the relay even when its rated running power appears acceptable. Keep the receiver away from metal objects, large electronic equipment, strong electromagnetic fields from motors, and other interference sources. If the issue continues, have a qualified electrician check the actual wiring and load specifications.

**Original question:**

> Hello, I bought your radio switch to control a pool cover. When unloaded, pressing the remote button works fine, but when I connect the load...

**Original answer:**

> Please check your wiring and load specifications. According to the manual, the wiring diagram for AC motors requires connecting the live wire (L) and neutral wire (N) to the input, and the AC motor to the NO and COM terminals. Ensure the load does not exceed the Max 1100W rated load, and that the L and N wires are not reversed. Also, avoid proximity to metal objects, large electronic equipment, or electromagnetic fields that could cause interference under load.

## Topic Summary / 主题归纳

- **Remote pairing and working modes / 遥控配对与工作模式**
- **Motor, garage shutter, and gate control / 电机、卷帘门与闸机控制**
- **Wiring, load rating, and electrical safety / 接线、负载与电气安全**
