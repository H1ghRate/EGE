from turtle import *
from numpy import arange

m = 10

tracer(0)

screensize(12000, 12000)

left(90)

for _ in range(104):
    forward(m * 50)
    right(288)

up()

for x in arange(-70, 30):
    for y in arange(-70, 30):
        setpos(m * x, m * y)
        dot(5, 'red')

done()
