from turtle import *

tracer(0)

m = 30

screensize(2000, 2000)

left(90)

pendown()

for _ in range(2):
    forward(m * 10)
    right(90)
    forward(m * 18)
    right(90)

penup()

forward(m * 5)
right(90)
forward(m * 14)
left(90)

pendown()

for _ in range(2):
    forward(m * 17)
    right(90)
    forward(m * 7)
    right(90)

up()

for i in range(-50, 50):
    for j in range(-50, 50):
        setpos(m * i, m * j)
        dot(5, 'purple')

done()