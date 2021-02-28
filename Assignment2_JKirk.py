import turtle
s = turtle.getscreen()
t = turtle.getturtle()

t.penup()
#t.setpos(x=60, y=-60)
t.pendown()
while True:
    t.lt(90)
    t.fd(120)
    if abs(turtle.pos())<1:
        break

#window remains open
turtle.exitonclick()