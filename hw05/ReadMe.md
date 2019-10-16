###Homework 4
=====================
I have included the gpio_test.c file to show the changes I made but I didn't submit the other files used because there were either no changes or the changes were made using instructions.
##Compiler Questions
=====================
1) Target     = app.o in the target to is is expected to output an object file
2) Dependency = app.c in the dependency because that is the file being compiled
3) Command    = -c tells the compiler to compile but not link

##Cross Compiling
=====================
I was successfully able to complete the cross compiler instructions and get the desired output.

##Derek Molloy Modules
=====================
#Part1:
I succesfully completed this part and got the board to say hello and goodbye

#Part2:
I completed this part and had the kernel recieve and readback "hello"

#Part3:
I demonstrated this part using the default pins in class. I have updated the files to use P9_14 as per the assignment. I did have an issue using P9 15 so I used P8 15 instead.

Here is what the kernel printed:
Oct 16 00:14:46 beaglebone kernel: [ 4235.988572] GPIO_TEST: Interrupt! (button state is 1)
Oct 16 00:14:46 beaglebone kernel: [ 4236.113419] GPIO_TEST: Interrupt! (button state is 0)


