f = [0] * 3500
for i in range(3000, 3500):
    f[i] = i

for x in range(-100, 100):
    for i in range(2999, 0, -1):
        f[i] = i + x + f[i + 2]
        if i == 2984:
            break
    if f[2984] - f[2988] == 5916:
        print(x)
        break
