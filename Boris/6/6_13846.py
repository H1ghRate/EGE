from turtle import *

def move(x, y):
    p = pos()

    goto(p + (x, y))

m = 30

tracer(0)

screensize(2000, 2000)

for _ in range(10):
    move(6 * m, 15 * m)

    move(-5 * m, -5 * m)

    setpos(2 * m, 2 * m)

    move(-1 * m, -10 * m)

up()

for x in range(-50, 50):
    for y in range(-50, 50):
        setpos(x * m, y * m)
        dot(5, 'red')

done()
