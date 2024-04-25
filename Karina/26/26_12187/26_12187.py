with open('./26/26_12187/26_12187.txt') as f:
    k = int(f.readline())

    n = int(f.readline())

    sizes = [int(i) for i in f.readline().split()]

    cells = []

    for size in sizes:
        cells.append((size, -1))
    
    a = []

    for _ in range(n):
        weight, st, end = map(int, f.readline().split())

        a.append((weight, st, end))

a.sort(key=lambda x: (x[1], x[0], x[2]))

cnt = 0

last_cell = 0

last_elem = ()

for weight, st, end in a:
    if st <= 24 * 60:
        for i in range(len(cells)):
            size, last_time = cells[i]

            if size >= weight and st > last_time:
                cells[i] = (size, end)
                cnt += 1

                last_cell = i + 1
                last_elem = (weight, st, end)

                break

weight, st, end = last_elem

for i in range(len(cells) - 1, -1, -1):
    size, last_time = cells[i]

    if size >= weight and st > last_time:
        cells[i] = (size, end)

        last_cell = max(last_cell, i + 1)

        break
    
print(cnt, last_cell)
