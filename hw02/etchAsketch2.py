#!/usr/bin/env python3
#Zachary Forster CM1646
#ECE434 HW2

import Adafruit_BBIO.GPIO as GPIO
import time

GPIO.cleanup()


def printBoard():
    #Print board
    print("====" * int(length) + "====")
    for row in board:
        print("|  ", end = "")
        for col in row:
            print(col + "   ", end = "")
        print("|\n")
    print("====" * int(length) + "====")
    
def shake(x,y, length, height):
    print("Clearing the board...")
    newBoard = [[" "] * length for i in range(height)]
    newBoard[y][x] = "X"
    return newBoard



def call(channel):
    if GPIO.input(channel):
        global cursorX
        global cursorY
        global board

        if channel == "P9_21":
            if cursorY != 0:
                cursorY -= 1
        elif channel == "P9_16":
            if cursorX != 0:
                cursorX -= 1
        elif channel == "P9_17":
            if cursorY != int(height)-1:
                cursorY += 1
        elif channel == "P9_18":
            if cursorX != int(length)-1:
                cursorX += 1
        elif channel == "P9_11":
            board = shake(cursorX, cursorY, int(length), int(height))
            
        board[cursorY][cursorX] = "X"
        printBoard()
            
    
    
def main():
    global cursorX
    global cursorY
    global length
    global height
    global board
    
    print("Board length? ")
    length = input()
    print("Board height? ")
    height = input()
    
    print(length + " X " + height + " Board Loading...")
    #print("Please use the following controls to move the cursor (hit enter each time)\nw (up)\ns (down)\na (left)\nd (right)\nr (shake)\nx (exit)")
    
    board = [[" "] *int(length) for i in range(int(height))]
    board[0][0] = "X"
    cursorX = 0
    cursorY = 0
    
    printBoard()
    
    GPIO.setup("P9_21", GPIO.IN)
    GPIO.setup("P9_11", GPIO.IN)
    GPIO.setup("P9_17", GPIO.IN)
    GPIO.setup("P9_18", GPIO.IN)
    GPIO.setup("P9_16", GPIO.IN)
        
    GPIO.add_event_detect("P9_21", GPIO.BOTH, callback = call, bouncetime = 400)
    GPIO.add_event_detect("P9_16", GPIO.BOTH, callback = call, bouncetime = 400)
    GPIO.add_event_detect("P9_17", GPIO.BOTH, callback = call, bouncetime = 400)
    GPIO.add_event_detect("P9_18", GPIO.BOTH, callback = call, bouncetime = 400)
    GPIO.add_event_detect("P9_11", GPIO.BOTH, callback = call, bouncetime = 400)
    
    try:
        while True:
            continue
    except KeyboardInterrupt:
        print("Thanks for playing!")
        GPIO.cleanup()

        
if __name__ == "__main__":
    main()