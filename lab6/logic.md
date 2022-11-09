---
title: Logic level translation
---

\newpage

In this lab, we'll practice using circuits for connecting devices that operate at different voltage levels.


## Notes

* In this lab, you will create some breadboard circuits with exposed pins and wires. Please be especially careful not to accidentally create connections that shouldn't be connected (e.g. short circuits). Also, check your work carefully before connecting any breadboard circuit to a board, to avoid damaging the board.
* You will submit your lab work in Gradescope. You will upload screenshots/photos and answer some questions as described in the Gradescope assignment. You do not have to write anything else (e.g. no description of procedure, etc.) 
* Read each subsection of this lab manual in its entirety before you start following the instructions in it. Some instructions are modified by explanations that come afterwards.
* Although you may work with a partner, this collaboration is limited to discussion and comparison. Your partner is not allowed to construct or modify your circuit, log in to your Pi, or run commands or write code on your Pi. Similarly, you are not allowed to do these things for your partner. 
* For your lab report, you must submit data, code, screenshots, and photos from your own experiment. You are not allowed to use your lab partner's data, code, screenshots, or photos.
* For any question in the lab report that is marked "Individual work", you should *not* collaborate with your lab partner or anyone else (even via discussion). You can use your notes, the lab manual, or the lecture slides and video to help you answer these questions.



## Parts

In this experiment, we will use a BJT transistor to switch a digital output on and off with a control signal from a GPIO pin, but with current and supply voltage from the Pi's power rails. You will need:

* A Pi, SD card, and power supply
* Breadboard and jumper cables
* Analog Discovery 2
* 2N3904 BJT NPN transistor. (The label is printed on the flat side of the transistor; you may have to hold the transistor at an angle in order to read it.)
* 2N700 MOSFET transistor. (The label is printed on the flat side of the transistor; you may have to hold the transistor at an angle in order to read it.)
* 1x220Ω, 3x1kΩ, 2x10kΩ, 1x4.7kΩ resistors

\newpage

## Procedure

### Set up the Analog Discovery 2 scope

Throughout this assignment, we will use the Analog Discovery 2 to visualize and compare the signal from a low-voltage device and a high-voltage device.

Connect your Analog Discovery 2 to your computer, and open the Waveforms app. Open the Scope tool. Configure the Scope tool so that:

* both Channel 1 and Channel 2 are enabled
* the vertical range is set up so you can see 0V, 3.3V, and 5V signal levels in the view

![Setting up the Scope tool](images/scope-setup-2ch.png){ width=500px }

Then, connect a GND signal from your Pi to a common GND row on a breadboard, and add:

* any GND wire (black) on the Analog Discovery 2 to GND
* the 1- wire (orange and white striped) on the Analog Discovery 2 to GND
* the 2- wire (blue and white striped) on the Analog Discovery 2 to GND

You will leave these three GND pins connected for the *entire experiment*.

For the rest of this assignment, we will view the low-voltage signal on Channel 1 (orange) and the high-voltage signal on Channel 2 (blue).

\newpage

### Set up the two "signals"

The logic level translation circuits we are using will translate any type of signal: a single on-off signal (digital input or output), a PWM signal, a clock signal for a communication bus, or a data signal for a communication bus. For convenience, we'll set up two PWM signals - one at a high voltage level, one at a low voltage leve - to use throughout. A PWM signal is useful for logic level translation because we can verify that both the HIGH and LOW logic levels are transferred successfully to the new voltage.

First, on your Pi, set up the low-voltage signal. Write a couple of lines of Python code to generate a hardware PWM signal on GPIO12 with a 100ms period and a 60% duty cycle.

Connect the 1+ (orange) pin on the Discovery 2 to GPIO12, run the scope, and verify that the PWM signal you see on CH1 matches the expected parameters. Take a screenshot for your lab report, then disconnect the 1+ pin from your Pi.

Then, on the Discovery 2, set up the high-voltage signal. We will use a PWM signal on W1 with a 100ms period and a 20% duty cycle:

* Click on the Wavegen tool from the Welcome screen
* Make sure that Channel 1 is selected
* Change the Type to Square
* Change the Frequency to 10 Hz (this will automatically change the Period to 100 ms)
* Change the Amplitude to 2.5V and the Offset to 2.5V
* Change the Symmetry (duty cycle) to 20%

![Set up the Wavegen waveform.](images/wavegen-setup.png){ width=500px }

Make sure that the signal that appears in the display has the expected parameters (20ms on time, 100ms period, minimum voltage level 0V, maximum voltage level 5V). Then click Run. You will leave this waveform running for the entire experiment. 

Connect the 2+ (blue) pin on the Discovery 2 to the W1 (yellow) pin on the Discovery 2. Run the scope, and verify that the PWM signal you see on CH2 matches the expected parameters. Take a screenshot for your lab report, then disconnect the 2+ pin from the W1 pin.


---

**Lab report**: Show the scope view with just the low-voltage signal on CH1. 

**Lab report**: Show the scope view with just the high-voltage signal on CH2.

---

### Low to high logic level translation using BJT 

First, we will look at the low-to-high logic level translation circuit using a BJT transistor (2N3904). Be careful about the orientation of this part - for your convenience, here is a pinout diagram:

![Pinout diagram for the BJT and MOSFET transistors used in this lab.](images/transistor-pinout-x2.svg){ width=300px }


You already have part of this circuit set up on your breadboard from last week, but switch out the buzzer and small resistor for a 10kΩ resistor. Then, connect the 1+ (orange) and 2+ (blue) pins on the Discovery 2 to realize the following schematic:

![Low to high logic level translation using BJT - no low-voltage signal.](images/scope-only-bjt.svg){width=400px}

Run the scope and check the display. The CH1 input will be floating (nothing is connected on the low-voltage signal side, so the input will pick up any stray noise in the circuit). The CH2 input will be pulled to 5V as long as the transistor is switched off. Verify that everything looks OK before you continue.

\newpage

Then, you will connect PWM signal on GPIO12 at the point where the low-voltage signal would appear in the circuit. (Recall that we are using this same PWM signal as the low-voltage signal throughout the experiment.)

![Low to high logic level translation using BJT - with low-voltage signal.](images/scope-gpio-bjt.svg){width=400px}

Run the scope tool, and verify that the low-level signal appears on CH1 and a level-shifted version of the same signal appears on CH2. Take a screenshot for your lab report, and a photo of your breadboard (make sure the numbered sticker on the breadboard is visible!)


When you are finished with this circuit, disconnect the parts from your breadboard (except for the GND row including Pi GND, 1-, and 2- wires from the Discovery 2 - leave that connected always.) Put the BJT and the 4.7kΩ resistor back in last week's kit.


---

**Lab report**: Annotate the breadboard photo of the circuit. Label the base, emitter, and collector pins of the transistor. Label each resistor. Also indicate the point where the low-voltage output signal is connected, and where the high-voltage input would be read.

**Lab report**: Show the screenshot of the scope display, with the low-voltage signal appearing on CH1 and a level-shifted version of the same signal on CH2. Does this level shifting circuit translate a 3.3V HIGH to 5V HIGH, and 3.3V LOW to 5V LOW? Explain.

**Lab report**: What type of signal is this level translation circuit suitable for?

---

\newpage


### Low to high logic level translation using MOSFET 

Next, we will construct a similar circuit using a MOSFET. We will use the 2N7000 FET. Review the datasheet for this part. The main parameter of relevance to this circuit is V\_GS(th). Check this value in the datasheet - will the 3.3V low-voltage signal at the gate pin be sufficient to switch the transistor on?

We will construct a similar level shifting circuit using the 2N7000. Be careful about the orientation of this part - for your convenience, here is a pinout diagram:

![Pinout diagram for the BJT and MOSFET transistors used in this lab.](images/transistor-pinout-x2.svg){ width=300px }

Prepare the following circuit on your breadboard:

* Source pin to GND
* Drain pin to 10kΩ series resistor to 5V
* Drain pin to 2+ (blue) scope input
* Gate pin to 1+ (orange) scope input

![Low to high logic level translation using MOSFET - no low-voltage signal.](images/scope-only-fet.svg){width=400px}

Run the scope and check the display. The CH1 input will be floating (nothing is connected on the low-voltage signal side, so the input will pick up any stray noise in the circuit). The CH2 input will be pulled to 5V as long as the transistor is switched off. Verify that everything looks OK before you continue.

\newpage

Then, you will connect PWM signal on GPIO12 at the point where the low-voltage signal would appear in the circuit. (Recall that we are using this same PWM signal as the low-voltage signal throughout the experiment.)

![Low to high logic level translation using MOSFET - with low-voltage signal.](images/scope-with-gpio-fet.svg){width=400px}

Run the scope tool, and verify that the low-level signal appears on CH1 and a level-shifted version of the same signal appears on CH2. Take a screenshot for your lab report, and a photo of your breadboard (make sure the numbered sticker on the breadboard is visible!)


When you are finished with this circuit, disconnect the parts from your breadboard (except for the GND row including Pi GND, 1-, and 2- wires from the Discovery 2 - leave that connected always.) 



---

**Lab report**: Show a screenshot of the 2N7000 datasheet, with V\_GS(th) highlighted. Will the 3.3V low-voltage signal at the gate pin be sufficient to switch the transistor on?

**Lab report**: Annotate the breadboard photo of the circuit. Label the gate, source, and drain pins of the transistor. Also indicate the point where the low-voltage output signal is connected, and where the high-voltage input would be read.

**Lab report**: Show the screenshot of the scope display, with the low-voltage signal appearing on CH1 and a level-shifted version of the same signal on CH2. Does this level shifting circuit translate a 3.3V HIGH to 5V HIGH, and 3.3V LOW to 5V LOW? Explain.

**Lab report**: What type of signal is this level translation circuit suitable for?

---

\newpage

### Bidirectional logic level translation using MOSFET 


The next circuit also uses the 2N7000 MOSFET, but in a bidirectional level shifting configuration. In this configuration,

* The gate pin should be connected to the 3.3V power rail
* The source pin should be "pulled up" to the 3.3V power rail, with a 10kΩ resistor
* The drain pin should be "pulled up" to the 5V power rail, with a 10kΩ resistor

Then, we'll add the scope pins:

* 1+ (orange) representing the low-voltage logic at the source pin
* 2+ (blue) representing the high-voltage logic at the drain pin

![Bidirectional logic level translation using MOSFET - no signal.](images/scope-only-bid.svg){width=400px}


Construct this circuit, on your breadboard. Run the scope and check the display. As long as the transistor is switched off, the CH1 input will be pulled to 3.3V and the CH2 input will be pulled to 5V. Verify the voltage levels and that everything looks OK before you continue.

Then, we'll connect the low-voltage signal from the Pi's GPIO12 pin:

![Bidirectional logic level translation using MOSFET - low-voltage signal driving.](images/scope-with-gpio-bid.svg){width=400px}

Run the scope tool, and verify that the low-level signal appears on CH1 at 3.3V and a level-shifted version of the same signal appears on CH2 at 5V. Take a screenshot for your lab report.

This circuit is a bidirectional logic level shifting circuit, which means that we can apply an output at the low-voltage side and read it on the high-voltage side (as we just did!), or we can apply an output at the high-voltage side and read it on the low-voltage side. Let's try that second setup now.

Disconnect GPIO12 from the circuit. 

\newpage

Verify in the Wavegen tool that the waveform generator is still running and is not stopped. Then, connect it to the high-voltage side of the circuit:

![Bidirectional logic level translation using MOSFET - low-voltage signal driving.](images/scope-with-wavegen-bid.svg){width=400px}

Run the scope tool, and verify that the high-level signal appears on CH2 at 5V and a level-shifted version of the same signal appears on CH1 at 3.3V. Take a screenshot for your lab report.

Also take a photo of your breadboard (make sure the numbered sticker on the breadboard is visible!)

When you are finished with this circuit, disconnect the parts from your breadboard (except for the GND row including Pi GND, 1-, and 2- wires from the Discovery 2 - leave that connected always.) 


---

**Lab report**: In the 2N7000 datasheet, find the Drain-Source Diode Forward Voltage, V\_SD, and also find V\_GS(th). (The former is not specified for the 2N7000, but is specified for the 2N7002 which is a similar transistor in a different package type.) Take screenshots of the datasheet with these portions highlighted. Using these values specifically, explain the sequence of events that occurs and the state of the transistor:

* when either side is "driving" the circuit and the output level is HIGH
* when the low voltage logic is "driving" the circuit and the output level is LOW
* when the high voltage logic is "driving" the circuit and the output level is LOW


**Lab report**: Annotate the breadboard photo of the circuit. Label the gate, source, and drain pins of the transistor. Also indicate the point where the low-voltage I/O signal is connected, and the point where the high-voltage I/O signal is connected.

**Lab report**: Show the screenshot of the scope display, with the low-voltage signal appearing on CH1 and a level-shifted version of the same signal on CH2. Does this level shifting circuit translate a 3.3V HIGH to 5V HIGH, and 3.3V LOW to 5V LOW? Explain.

**Lab report**: Show the screenshot of the scope display, with the high-voltage signal appearing on CH2 and a level-shifted version of the same signal on CH1. Does this level shifting circuit translate a 5V HIGH to 3.3V HIGH, and 5V LOW to 3.3V LOW? Explain.


**Lab report**: What type of signal is this level translation circuit suitable for?

---


\newpage


### High to low logic level translation using a voltage divider 

Finally, we'll consider a simple circuit that uses resistors to shift a high-voltage output to a lower voltage level.

Construct the following circuit on your breadboard.


![High to low logic level translation using voltage divider - no high-voltage signal.](images/scope-only-divider.svg){width=200px}


Run the scope and check the display. Both inputs will be floating at this point, so they'll pick up any noise that happens to appear at the inputs.

In the Wavegen tool, make sure the waveform generator is still running. Then, you will connect PWM signal on W1 at the point where the high-voltage signal would appear in the circuit. (Recall that we are using this same PWM signal from W1 as the high-voltage signal throughout the experiment.)

![High to low logic level translation using voltage divider - with high-voltage signal.](images/scope-wavegen-divider.svg){width=200px}


Run the scope tool, and verify that the high-level signal appears on CH2 at 5V and a level-shifted version of the same signal appears on CH1 at a 3.3V-compatible logic level. Take a screenshot for your lab report. Also take a photo of your breadboard (make sure the numbered sticker on the breadboard is visible!)

Disconnect the W1 pin from your circuit, but leave the rest of it in place.

\newpage

---

**Lab report**: Annotate the breadboard photo of the circuit. Label each resistor. Also label the point where the low-voltage input signal is connected, and the point where the high-voltage output signal is connected.

**Lab report**: Show the voltage divider equation with the relevant values for this circuit. If 5V is applied at the top of the voltage divider, what is the exact voltage level you would expect at the point where the low-voltage input is connected?

**Lab report**: Show the screenshot of the scope display, with the high-voltage signal appearing on CH2 and a level-shifted version of the same signal on CH1. Does this level shifting circuit translate a 5V HIGH to 3.3V HIGH, and 5V LOW to 3.3V LOW? Explain.


**Lab report**: What type of signal is this level translation circuit suitable for?

---


