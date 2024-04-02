from turtle import *
from numpy import arange

m = 50

tracer(0)

screensize(12000, 12000)

for _ in range(2):
    forward(m * 7)
    right(90)
    forward(m * 18)
    right(90)


forward(m * (-2))
right(90)
forward(m * 9)
left(90)

for _ in range(2):
    forward(m * 8)
    right(90)
    forward(m * 6)
    right(90)

up()

for x in arange(-70, 30):
    for y in arange(-70, 30):
        setpos(m * x, m * y)
        dot(5, 'red')

done()
