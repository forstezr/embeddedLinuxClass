#!/usr/bin/env python3
#Zachary Forster CM1646
#ECE434 HW3

import Adafruit_BBIO.GPIO as GPIO
from Adafruit_BBIO.Encoder import RotaryEncoder, eQEP2b, eQEP1
import time
from subprocess import call
import smbus

#Run setup script
GPIO.cleanup()
call("./etchAsketchSetup.sh")

#declare rotary encoders
myEncoderR = RotaryEncoder(eQEP2b)
myEncoderR.setAbsolute()
myEncoderR.enable()

myEncoderL = RotaryEncoder(eQEP1)
myEncoderL.setAbsolute()
myEncoderL.enable()

bus = smbus.SMBus(1)  # Use i2c bus 1
matrix = 0x70         # Use address 0x70

#setup the 8x8 led display
bus.write_byte_data(matrix, 0x21, 0)   # Start oscillator (p10)
bus.write_byte_data(matrix, 0x81, 0)   # Disp on, blink off (p11)
bus.write_byte_data(matrix, 0xe7, 0)   # Full brightness (page 15)

#Green byte then red byte in left to right columbs
display = [0, 0, 0, 0, 0, 0, 0, 0,
    0, 0, 0, 0, 0, 0, 0, 0]


def printBoard():
    #Print board onto 8x8 led matrix
    for c in range(int(height)):
        #map the board to the led display coordinates
        word = ""
        for r in range(int(length)):
            if(board[r][c] == 1):
                word += "1"
            else:
                word+= "0"
        display[c*2] = int(word, 2)
    bus.write_i2c_block_data(matrix, 0, display)
    
def shake(x,y, length, height):
    print("Clearing the board...")
    newBoard = [[0] * length for i in range(height)]
    newBoard[y][x] = 1
    return newBoard



def call(channel):
    #interrupt handling for the shake button
    if GPIO.input(channel):
        global cursorX
        global cursorY
        global board
        if channel == "P9_11":
            board = shake(cursorX, cursorY, int(length), int(height))
        printBoard()
            
    
    
def main():
    global cursorX
    global cursorY
    global length
    global height
    global board
    
    #board set at 8x8 for led matrix
    length = "8"
    height = "8"
    
    print(length + " X " + height + " Board Loading...")
    board = [[0]*int(length) for i in range(int(height))]
    board[0][0] = 1
    cursorX = 0
    cursorY = 0
    old_posL = 0
    old_posR = 0
    
    #Draw initial board
    printBoard()
    
    
    #Shake button
    GPIO.setup("P9_11", GPIO.IN)
    GPIO.add_event_detect("P9_11", GPIO.BOTH, callback = call, bouncetime = 250)
    
    try:
        while True:
            #Game loop
            cur_positionL = myEncoderL.position
            cur_positionR = myEncoderR.position
            #print(str(cur_positionL) + " | "+ str(cur_positionR) + " | "+str(cursorX)+" | "+str(cursorY))
            #update cursor position
            if cur_positionL > old_posL:
                if cursorY != 0:
                    cursorY -= 1
            elif cur_positionL < old_posL:
                if cursorY != int(height)-1:
                    cursorY += 1
            if cur_positionR > old_posR:
                if cursorX != 0:
                    cursorX -= 1
            elif cur_positionR < old_posR:
                if cursorX != int(length)-1:
                    cursorX += 1
            
            #Draw on new cursor
            board[cursorY][cursorX] = 1
            old_posL = cur_positionL
            old_posR = cur_positionR
            printBoard()
            time.sleep(0.4) #refresh rate
    except KeyboardInterrupt:
        print("Thanks for playing!")
        GPIO.cleanup()

        
if __name__ == "__main__":
    main()