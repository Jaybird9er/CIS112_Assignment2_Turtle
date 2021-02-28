""" 
Author: Jamey Kirk
Title: Assignment2_Turtle
Date: 02/28/2021
Description: use turtle to draw polygons
"""

## initialize turtle screen
import turtle
s = turtle.getscreen()
t = turtle.getturtle()
 
## while length >= 20 then draw = True
draw = True
lineLen = 120
startPos = 1.0
## absVal is value difference each time turtle x and y cordinates change
## adding it to the startPos after each loop guarantees that startPos will always be larger
absVal = 14.142135623730951
xPos = 0
yPos = 0
while draw:
    t.lt(90)
    t.fd(lineLen)
    if lineLen >= 20:
        if abs(t.pos()) < startPos:
            xPos -= 10
            yPos += 10
            t.penup()
            t.setpos(x=xPos, y=yPos)
            t.pendown()
            lineLen -= 20
            startPos += absVal
    else:
        draw = False

#window remains open
turtle.exitonclick()