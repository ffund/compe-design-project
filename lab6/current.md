# Driving current

In this lab, we'll practice using a GPIO pin to switch a load on and off with a transistor circuit. 

## Notes

* In this lab, you will create some breadboard circuits with exposed pins and wires. Please be especially careful not to accidentally create connections that shouldn't be connected (e.g. short circuits). Also, check your work carefully before connecting any breadboard circuit to a board, to avoid damaging the board.
* Read each subsection of this lab manual in its entirety before you start following the instructions in it. Some instructions are modified by explanations that come afterwards.
* Although you may work with a partner, this collaboration is limited to discussion. Your partner is not allowed to construct or modify your circuit, log in to your Pi, or run commands or write code on your Pi. Similarly, you are not allowed to do these things for your partner. (You *are* encouraged to collaborate by screen-sharing or showing video of your circuit to debug and discuss problems together.)
* For your lab report, you must submit data, code, and screenshots from your own experiment. You are not allowed to use your lab partner's data, code, or screenshots.
* For any question in the lab report that is marked "Individual work", you should *not* collaborate with your lab partner or anyone else (even via discussion). You can use your notes, the lab manual, or the lecture slides and video to help you answer these questions.



## Parts

In this experiment, we will use a BJT transistor to switch a digital output on and off with a control signal from a GPIO pin, but with current and supply voltage from the Pi's power rails. You will need:

* A Pi, SD card, and power supply
* Breadboard and jumper cables
* Digital multimeter
* 2N3904 BJT NPN transistor. You may have to hold the transistor at an angle in order to read the label.
* 5mm white LED with ~25mA maximum current rating and ~3V forward voltage.
* Active buzzer. This part has the driver circuitry inside , so you don't need a PWM signal to drive it (as with the passive piezo buzzers we've demonstrated before). Note that this part is polarized - there is a small **+** marking on the top to indicate the positive side.
* 220Ω and 4.7kΩ resistors

\newpage

## Driving current using a transistor

First, we'll work with a basic LED circuit.

![Identify base, collector, and emitter pins for your transistor, then connect it as pictured.](images/orientation-2N3904-2N2222.pdf){ width=100% }

Use the diagram from the datasheet (also shown here) to identify the base, collector, and emitter pins on your transistor. Then, place it in your breadboard and add resistors and an LED as follows:

* 220Ω resistor in series with the collector pin
* 4.7kΩ resistor in series with the base pin
* Negative side (short leg) of LED in series with the 220Ω resistor 

Finally, connect it to your board as pictured - 

* GND to the emitter pin of the transistor
* 5V supply to the positive side (long leg) of LED. 
* Any available GPIO pin to the 4.7kΩ resistor

Configure the GPIO pin as output HIGH (as in Lab 2), and watch the LED turn on. 



### Voltage and current measurement


Use your digital multimeter to measure the voltage:

* across the LED
* across the base and emitter pins of the transistor
* across the base and collector pins of the transistor
* across the base resistor
* across the collector resistor

while the LED is switched on. Save these values for your lab report.

\newpage


To measure current using a digital multimeter, you must:

* break the circuit
* set the dial on the multimeter to current mode, and move the red probe to the current terminal
* put the multimeter in series with your circuit

Be very careful *not* to put the multimeter in parallel with any part of your circuit when it is in current mode - this will create a short circuit, and can break your multimeter and/or your Pi.


Use your multimeter to measure current 

* between the 5V supply pin and the positive side of the LED
* between the GPIO pin and the base resistor


while the LED is switched on. Save these values for your lab report.

**Lab report**: Draw a diagram of the circuit, similar to the schematic shown above. On the diagram, indicate the voltage drop across each component: $V_{LED}$, $V_{BE}$, $V_{CE}$, $V_{R_B}$, $V_{R_C}$. Also indicate the current in each branch, $I_B$ and $I_C$.

**Lab report**: Compute the current *gain* in this circuit.

**Lab report**: Take a screenshot of the part of the datasheet that describes the expected $V_{BE}$, $V_{CE}$, $h_{FE}$ for this transistor. Annotate the screenshot to circle the most appropriate values for your experiment (since these vary with the current in the circuit.) Are your measured values within the expected range?


**Lab report** (individual work): Which resistor is primarily responsible for limiting the current flowing through the LED? Which resistor is primarily responsible for limiting the current from the GPIO pin? 

**Lab report** (individual work): What is the benefit of this circuit with the transistor, compared to the circuit in Lab 2 where the LED and a current-limiting resistor were connected directly to a GPIO pin? 

**Lab report** (individual work): Suppose you were to replace the 4.7kΩ resistor with a 10kΩ resistor. What would change in the circuit? Draw a diagram of the circuit, and indicate the *estimated* voltage drop across each component: $V_{LED}$, $V_{BE}$, $V_{CE}$, $V_{R_B}$, $V_{R_C}$. Also indicate the *estimated* current in each branch, $I_B$ and $I_C$, and the current *gain* in this circuit.

**Lab report** (individual work): Can you keep the LED brightly lit while making the base current arbitrarily small (for example, a few µA)? Explain.

\newpage

### Buzzer circuit

Replace the LED in your schematic with the 5V buzzer. (Make sure to note the polarity of the buzzer!)

![5V buzzer circuit. This is an active buzzer, meaning that it contains internal circuitry to drive the buzzer; it doesn't need an external PWM signal.](images/buzzer_bb.pdf)

Verify that you can turn the buzzer on and off by writing HIGH or LOW to the GPIO output.

Then, remove the wire that connects the 5V supply pin to the positive leg of the buzzer. Instead, connect the 3.3V supply pin to the positive leg of the buzzer. Try to turn the buzzer on and off by writing HIGH or LOW to the GPIO output.

**Lab report** (individual work): The 5V buzzer can't be driven reliably at 3.3V. But with this transistor circuit, we can use a 3.3V GPIO pin to switch it on and off. How? Explain.


