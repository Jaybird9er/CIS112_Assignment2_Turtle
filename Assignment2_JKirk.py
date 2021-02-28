## initialize turtle screen
import turtle
s = turtle.getscreen()
t = turtle.getturtle()

## adjust turtle start position
# t.penup()
# t.setpos(x=60, y=-60)
# t.pendown()
 
## while length >= 20 then draw = True
draw = True
lineLen = 120
startPos = 1.0
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