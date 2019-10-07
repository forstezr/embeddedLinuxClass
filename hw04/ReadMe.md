Part1:
================================
See attached memory map diagram

Part2:
================================
I was able to map "P9 23" and "P9 24" to user2 and user3 LEDs on the board. They correctly turn on and off.
Simply run the toggleLED.c after compiling it and press the buttons to see it work. Make sure to set the pin congif correctly.

Part3:
================================
I modified part 1 to toggle "P9 23" and measured it on a scope.
My fastest period was about 360ns which was significantly faster than the 288us measured using the c file from hw02.
Additionally, my program does run faster with no usleep.
To run this just set the pin config for P9 23 to gpio output and then run togglePin.c after compiling it.

Part4:
================================
I was able to run through the instructions for using the lcd screen and complete them.
To see these please fo to /exercises/displays/ili9341/fb/ and run the corresponding functions as in the instructions.

## Images to display from test
![memory map](https://github.com/forstezr/embeddedLinuxClass/blob/master/hw04/IMG_20191001_121421.jpg?raw=true "Memory Map")

![Boris Normal](https://github.com/forstezr/embeddedLinuxClass/blob/master/hw04/IMG_20191001_120651.jpg?raw=true "Boris Normal")

![Boris Rotated](https://github.com/forstezr/embeddedLinuxClass/blob/master/hw04/IMG_20191001_120754.jpg?raw=true "Boris Rotated")

![Movie Normal](https://github.com/forstezr/embeddedLinuxClass/blob/master/hw04/IMG_20191001_123414.jpg?raw=true "Movie Normal")

![Movie Rotated](https://github.com/forstezr/embeddedLinuxClass/blob/master/hw04/IMG_20191001_123523.jpg?raw=true "Movie Rotated")

![Text Screen](https://github.com/forstezr/embeddedLinuxClass/blob/master/hw04/IMG_20191001_123721.jpg?raw=true "Text on Screen")


## Prof. Yoder's comments

Very good.  Nice pictures.
Done early +2

Grade:  12/10