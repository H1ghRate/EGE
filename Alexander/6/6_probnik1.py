from turtle import *
from time import sleep

m = 5

tracer(0)

screensize(2000, 2000)

left(90)

for i in range(104):
    forward(m * 50)
    right(288)
up()

for x in range(-20, 20):
    for y in range(-20, 20):
        setpos(x * m, y * m)
        dot(5, 'red')

done()