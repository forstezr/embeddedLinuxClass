### Homework 8

# Blink an LED

I was able to blink the user3 LED with the provided code

I then modified the code to write to P9_31 and hooked it up to a scope

![BlinkLED](https://github.com/forstezr/embeddedLinuxClass/blob/master/hw08/scope_2.png?raw=true "Blinking an LED")

Using make will start the program and make stop will end the program. make start will also start the program. There was a decent amount of jitter and the signal wasn't really stable.
Additionally, the fastest frequency was about 12.5MHz (period of 80ns)

# PWM Generator

I was able to run this and see the signal on P9_31.

![PWMGen](https://github.com/forstezr/embeddedLinuxClass/blob/master/hw08/scope_3.png?raw=true "PWM Generaion")

The signal is pretty stable and the standard deviation is about 15ns or 66MHz. There wasn't a lot of jitter.

# Controlling PWM Frequency

I was able to run this program and see the various signals on the different output pins.

![ControlPWM](https://github.com/forstezr/embeddedLinuxClass/blob/master/hw08/scope_5.png?raw=true "Controlling PWM")

The output pins are P9_28,29,30,31. The highest frequency I was able to see was 327kHz. There was no jitter and the pwm-test worked when I ran it.

# Reading an Input at Regular Intervals

I ran this program and can clearly see the 30ns (on avg) delay between the input signal and output signal.

![ReadingInput](https://github.com/forstezr/embeddedLinuxClass/blob/master/hw08/scope_6.png?raw=true "Reading Input")


## Prof. Yoder's comments

Looks like a good start, but not finished. 
Don't forget to answer the questions for each part and update your scope_4.png.

## Prof. Yoder's new comments
Looks good.  

Late: -1
Grade:  9/10