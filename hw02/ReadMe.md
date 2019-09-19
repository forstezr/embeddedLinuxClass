Part 1:
=================================================================
I completed this assignment.
the four buttons correctly toggle the leds on and off
simply run the progam after connecting the IO (look in file for mapping)

Togglegpio.sh answers:
=================================================================
1. What's the min and max voltage? min -2.14V to max 2.14V
2. What period is it? 238.6ms
3. How close is it to 100ms? It is roughly twice the expected 100ms (I believe the 100ms is only supposed to be the half period)
4. Why do they differ? 100ms specifies the half period.
5. Run htop and see how much processor you are using. ~18%
6. Try different values for the sleep time (2nd argument). What's the shortest period you can get? Make a table of the values you try and the corresponding period and processor usage.

  sTime |   .sh   |   .py   |   .c    |
 ------ |   ---   |   ---   |   --    |
 0.00001| 035.7ms | 600.1us | 288.0us |
 0.0001 | 038.2ms |   3.3ms | 03.20ms |
  0.001 | 055.5ms |  21.3ms | 021.0ms |
  0.1   | 238.6ms | 201.5ms | 201.1ms |
  
7. How stable is the period? Mostly stable with some blips
8. Try launching something like vi. How stable is the period? still mostly stable (not at sleep time (0.00001)
9. Try cleaning up togglegpio.sh and removing unneeded lines. Does it impact the period? not really. It still looks about the same.
10. togglegpio uses bash (first line in file). Try using sh. Is the period shorter? yes just a bit.
11. What's the shortest period you can get? with sh, 26ms

Togglegpio.py answers:
=================================================================
1. What's the min and max voltage? min -2.01V to max 2.05V
2. What period is it? 201.5ms (sleeptime 0.1)
3. How close is it to 100ms? roughly double
4. Why do they differ? 100ms is half the period as defined in the program
5. Run htop and see how much processor you are using. ~3%
6. Try different values for the sleep time (2nd argument). What's the shortest period you can get? Make a table of the values you try and the corresponding period and processor usage.
   See table in first section
7. How stable is the period? pretty stable
8. Try launching something like vi. How stable is the period? no change
9. Try cleaning up togglegpio.sh and removing unneeded lines. Does it impact the period? Not applicable
10. togglegpio uses bash (first line in file). Try using sh. Is the period shorter? Not applicable
11. What's the shortest period you can get? ~600us

Togglegpio.c answers:
=================================================================
1. What's the min and max voltage? -2.009V to 2.046V
2. What period is it? 201.3ms
3. How close is it to 100ms? just over double
4. Why do they differ? 100ms is the sleep time or half period
5. Run htop and see how much processor you are using. ~3.3%
6. Try different values for the sleep time (2nd argument). What's the shortest period you can get? Make a table of the values you try and the corresponding period and processor usage.
   See first table
7. How stable is the period? very stable
8. Try launching something like vi. How stable is the period? still stable
9. Try cleaning up togglegpio.sh and removing unneeded lines. Does it impact the period? Not applicable
10. togglegpio uses bash (first line in file). Try using sh. Is the period shorter? not applicable
11. What's the shortest period you can get? 284.2us

Part 3:
================================================================
I completed this assignment using four buttons to control the directional movement of the cursor and one to clear (shake) the board.
Simply run the program using ./etchAsketh2.py and follow the instructions
please look in the .py file for the button inputs
up    => P9_21
Left  => P9_16
Down  => P9_17
Right => P9_18
Shake => P9_11


## Prof. Yoder's comments

Very well documented.    I added some formatting to your table.  Look at it at
https://github.com/forstezr/embeddedLinuxClass/tree/master/hw02 to see how it looks.

Did the outputs really go to a negative voltate?

Grade:  10/10