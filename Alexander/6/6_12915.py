from turtle import *

def move(x, y):
    our_pos = pos()

    goto(our_pos[0] + m * x, our_pos[1] + m * y)

m = 30

tracer(0)

screensize(2000, 2000)

pendown()

for _ in range(10):
   move(0, 2)
   move(2, 0)
   move(0, 10)
   move(-2, 0)
   move(0, 2)
   move(6, 0)
   move(0, -2)
   move(-2, 0)
   move(0, -10)
   move(2, 0)
   move(0, -2)
   move(-6, 0)

penup()

up()

for x in range(-40, 40):
    for y in range(-40, 40):
        setpos(m * x, m * y)

        dot(5, 'blue')

done()