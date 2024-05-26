with open('./26_9793.txt') as f:
    n = int(f.readline())

    a = []

    for i in range(1, n + 1):
        sh, ok = map(int, f.readline().split())

        a.append((sh, 'sh', i))

        a.append((ok, 'ok', i))
    
a.sort(key=lambda x: x[0])

used = []
lenta = [0] * n
last_ind = 0

for time, key, ind in a:
    if ind in used:
        continue

    if key == 'sh':
        for i in range(n):
            if lenta[i] == 0:
                lenta[i] = ind
                last_ind = ind

                used.append(ind)

                break
    elif key == 'ok':
        for i in range(n - 1, -1, -1):
            if lenta[i] == 0:
                lenta[i] = ind
                last_ind = ind

                used.append(ind)

                break

print(last_ind, lenta.index(last_ind))
