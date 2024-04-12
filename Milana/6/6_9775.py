from turtle import *

m = 50

tracer(0)

screensize(8000, 8000)

left(90)

for i in range(2):
    forward(m * 13)
    right(90)
    forward(m * 20)
    right(90)


forward(m * 8)
right(90)
back(m * 3)
left(90)

for i in range(2):
    forward(m * 16)
    right(90)
    forward(m * 8)
    right(90)

up()

for x in range(-50, 50):
    for y in range(-50, 50):
        setpos(x * m, y * m)
        dot(5, 'red')

done()
