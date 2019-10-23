# Homework 6 Questions

1. Where does Julia Cartwright work?

    National Instruments

2. What is PREEMT_RT? Hint: Google it.

    PREEMT_RT is a version of linux that aims to make all IRQs bounded. Also known as a hardened version of Linux.

3. What is mixed criticality?

    Mixed criticality is when both software and hardware can create interrupts of different priority on the same processor.

4. How can drivers misbehave?

    Drivers can misbehave if they disable IRQs because this prevents other interrupts from being serviced.

5. What is Δ in Figure 1?

    The time it takes from the beginning of an external event to the time it takes the event to be serviced (real time task executes)

6. What is Cyclictest[2]?

    Test used to characterize the delta, takes a time stamp, then sleeps some duration, then takes another time stamp. The difference between the actual time slept and the duration time slept is delta.

7. What is plotted in Figure 2?

    The result of the cyclictest with sleep duration on the x axis and delta on the y axis comparing mainline vs preemt_rt.

8. What is dispatch latency? Scheduling latency?

    Dispatch latency  : Time it takes from the hardware event occuring to the interrupt dispatch occuring.
    Scheduling latency: Amount of time it takes from the time the scheduler is made aware until the task is given to the CPU to be executed.

9. What is mainline?

    Mainline is the current stable version of the Linux kernel.

10. What is keeping the External event in Figure 3 from starting?

    A low priority interrupt that is long running.

11. Why can the External event in Figure 4 start sooner?

    The external event in figure 4 can start earlier because the interrupt handlers are threaded so the interrupts are handled in threads allowing other interrupts to be handled.

# Homework 6 PREEMPT_RT

## Cyclictest without RT and no load

real	1m40.301s
user	0m0.602s
sys	    0m3.171s

## Cyclictest without RT and load

real	1m40.554s
user	0m2.673s
sys	    0m8.704s

Linux beaglebone 5.4.0-rc2-bone1 #1 PREEMPT Tue Oct 8 15:25:09 EDT 2019 armv7l GNU/Linux

## Cyclictest with RT and no Load

real	1m45.604s
user	0m0.641s
sys   	0m4.029s

## Cyclictest with RT and Load

real	1m45.538s
user	0m1.249s
sys	    0m7.096s

# Plots

## Unloaded

![histogramUnloaded](https://github.com/forstezr/embeddedLinuxClass/blob/master/hw06/unloaded.jpg?raw=true "Unloaded histogram")

The plots are relatively similar however the rt version is bounded and doesn't have "noise" as the sleep duration increases.

## Loaded

![histogramloaded](https://github.com/forstezr/embeddedLinuxClass/blob/master/hw06/loaded.png?raw=true "loaded histogram")

These plots are also similar, I used make and make clean as a load. It looks to me like rt is still bounded.

## Prof. Yoder's comments
Looks good.  

Late: -1
Grade:  9/10

Project Wiki is not started 