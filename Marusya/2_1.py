summa = 0

cnt = 0

while True:
    x = float(input())

    if x == 0:
        break

    summa += x

    cnt += 1

print(summa / cnt)
