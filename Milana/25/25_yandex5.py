from fnmatch import fnmatch

cnt = 0
max_n = 0

for i in range(400000003323, 5 * 10 ** 11, 12300):
    if fnmatch(str(i), '4?8?15?16?23'):
        cnt += 1
        max_n = max(max_n, i)

print(cnt, max_n)

