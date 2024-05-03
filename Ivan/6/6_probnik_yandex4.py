from turtle import *

m = 200

tracer(0)

screensize(2000, 2000)

for _ in range(36):
    forward(m * 1)
    right(36)

forward(m * 4)
right(90)

for _ in range(8):
    forward(m * 6)
    right(90)

up()

for i in range(-60, 60):
    for j in range(-60, 60):
        setpos(m * i, m * j)
        dot(5, 'red')

done()
