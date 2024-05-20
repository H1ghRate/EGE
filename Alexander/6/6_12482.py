from turtle import * 

m = 30

tracer(0)

screensize(2000, 2000)

left(90)

pendown()

for _ in range(4):
    forward(m * 8)

    right(90)

for _ in range(4):  
    left(30)

    forward(m * 6)

    right(30)

    forward(m * 8)
    
    right(150)

    forward(m * 6)

    left(60)

penup()

up()

for x in range(-40, 40):
    for y in range(-40, 40):
        setpos(m * x, m * y)

        dot(5, 'blue')

done()