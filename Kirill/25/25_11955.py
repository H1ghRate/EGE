from fnmatch import fnmatch

for i in range(133 * 8, 10 ** 10 + 1, 133 * 10):
    s = str(i)

    if fnmatch(s, '1?2157*4'):
        d = s[1]
        n = s[6:-1]

        f1 = int(d) % 2 == 0

        f2 = all(int(j) % 2 != 0 for j in n)

        if f1 and f2:
            print(i, i // 133)