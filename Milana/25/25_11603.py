from fnmatch import fnmatch

summa = 0

cnt = 0

for i in range(5364, 10 ** 12 + 1, 14900):
    if fnmatch(str(i), '1*28?64'):
        summa += i
        cnt += 1

print(cnt, summa / cnt)
