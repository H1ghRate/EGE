LEN_ROAD = 109

v=int(input())

t=int(input())

dist = (abs(v) * t) % LEN_ROAD

if (dist == 0):
    print(0)
elif (v >= 0):
    print(dist)
else:
    print(LEN_ROAD - dist)
