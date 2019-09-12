#!/usr/bin/env python3
#//////////////////////////////////////
#Zachary Forster CM1646
#Python3 etch-a-sketch program
#09/11/2019
#//////////////////////////////////////

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

print("Board length? ")
length = input()
print("Board height? ")
height = input()

print(length + " X " + height + " Board Loading...")
print("Please use the following controls to move the cursor (hit enter each time)\nw (up)\ns (down)\na (left)\nd (right)\nr (shake)\nx (exit)")

board = [[" "] *int(length) for i in range(int(height))]
board[0][0] = "X"
cursorX = 0
cursorY = 0

printBoard()

#Begin Game loop
while(True):
    ch = input()
    #move cursor within bounds of board
    if ch == "w":
        if cursorY != 0:
            cursorY -= 1
    elif ch == "a":
        if cursorX != 0:
            cursorX -= 1
    elif ch == "s":
        if cursorY != int(height)-1:
            cursorY += 1
    elif ch == "d":
        if cursorX != int(length)-1:
            cursorX += 1
    elif ch == "r":
        board = shake(cursorX, cursorY, int(length), int(height))
    elif ch == "x":
        break
    #draw cursor
    board[cursorY][cursorX] = "X"
    printBoard()


print("Thanks for playing!")


