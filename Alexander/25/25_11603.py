from fnmatch import fnmatch

cnt = 0
summa = 0

for i in range(5364, 10 ** 12 + 1, 14900):
    if fnmatch(str(i), '1*28?64'):
        summa += i
        cnt += 1

print(cnt, summa / cnt)


# for i in range(536, 10 ** 5, 596):
#     print(i)
