from fnmatch import fnmatch

summa = cnt = 0

for i in range(5364, 10 ** 12, 14900):
    if fnmatch(str(i), '1*28?64'):
        cnt += 1
        summa += i

print(cnt, summa / cnt)
