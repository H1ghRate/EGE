from turtle import *
from numpy import arange

m = 250

tracer(0)

screensize(12000, 12000)

left(90)

for _ in range(10):
    right(120)
    forward(m * 10)

for _ in range(7):
    forward(m * 15)
    right(90)

for _ in range(5):
    right(60)
    forward(m * 20)
    right(30)

up()

for x in arange(-70, 30):
    for y in arange(-70, 30):
        setpos(m * x, m * y)
        dot(5, 'red')

done()
