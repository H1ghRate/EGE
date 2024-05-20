with open('./27_2724/27B_2724.txt') as f:
    n = int(f.readline())

    osts = [0] * 131

    for _ in range(n):
        x = int(f.readline())

        osts[x % 131] += 1
     
cnt = 0

for ost1 in range(131):
    for ost2 in range(ost1, 131):
        if (ost1 + ost2) % 131 == 0:
            if (ost1 == ost2):
                cnt += osts[ost1] * (osts[ost1] - 1) // 2
            else:
                cnt += osts[ost1] * osts[ost2]

print(cnt)

cnt = osts[0] * (osts[0] - 1) // 2

for ost in range(1, 65 + 1):
    cnt += osts[ost] * osts[131 - ost]

print(cnt)
