from turtle import *

m = 60

tracer(0)

screensize(20000, 20000)

left(90)

for _ in range(4):
    forward(8 * m)
    right(90)

for _ in range(4):
    left(30)
    forward(6 * m)
    right(30)
    forward(8 * m)
    right(150)
    forward(6 * m)
    left(60)

up()

for x in range(-50, 50):
    for y in range(-50, 50):
        setpos(x * m, y * m)
        dot(5, 'red')

done()