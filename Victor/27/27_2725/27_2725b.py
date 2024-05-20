with open('./27_2725/27B_2725.txt') as f:
    n = int(f.readline())

    osts = [0] * 69

    for _ in range(n):
        x = int(f.readline())

        osts[x % 69] += 1
    
cnt = 0

for ost in osts:
    cnt += ost * (ost - 1) // 2

print(cnt)
