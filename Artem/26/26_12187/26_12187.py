from collections import defaultdict

with open('26_12187.txt') as f:
    k, n = int(f.readline()), int(f.readline())

    spaces = defaultdict(list)

    for i, space in enumerate(f.readline().split(), 1):
        spaces[i] = [int(space), 0]

    users = defaultdict(list)

    for _ in range(n):
        size, st, end = map(int, f.readline().split())

        users[st].append((size, end))

served = 0

for i in range(1440):
    curr_users = users[i]

    curr_users.sort()

    for size, end in curr_users:
        for j in range(1, k + 1):
            space, last_time = spaces[j]

            if i >= (last_time + 1) and space >= size:
                spaces[j][1] = end

                served += 1

                break

print(served)
