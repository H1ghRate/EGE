with open('./27_2729/27B_2729.txt') as f:
    n = int(f.readline())

    osts = [[1e16] * 3 for _ in range(11)]

    for _ in range(n):
        x = int(f.readline())

        osts[x % 11] = sorted(osts[x % 11] + [x])[:3]

min_s = 1e16

print(osts)

for o1 in range(11):
    for o2 in range(o1, 11):
        for o3 in range(o2, 11):
            s = 1e16
            if (o1 + o2 + o3) % 11 == 0:
                if o1 != o2 != o3:
                    s = osts[o1][0] + osts[o2][0] + osts[o3][0]
                if o1 == o2 and o1 != o3 and o2 != o3:
                    s = osts[o1][0] + osts[o1][1] + osts[o3][0]
                if o2 == o3 and o2 != o1 and o3 != o1:
                    s = osts[o2][0] + osts[o2][1] + osts[o1][0]
                if o1 == o3 and o1 != o2 and o3 != o2:
                    s = osts[o1][0] + osts[o1][1] + osts[o2][0]
                if o1 == o2 == o3:
                    s = osts[o1][0] + osts[o1][1] + osts[o1][2]

            min_s = min(min_s, s)

print(min_s)
