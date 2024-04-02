from turtle import *
from numpy import arange

m = 50

tracer(0)

screensize(12000, 12000)

left(90)

right(90)

for _ in range(3):
    right(45)
    forward(m * 10)
    right(45)

right(315)
forward(m * 10)

for _ in range(2):
    right(90)
    forward(m * 10)

up()

for x in arange(-70, 30):
    for y in arange(-70, 30):
        setpos(m * x, m * y)
        dot(5, 'red')

done()
