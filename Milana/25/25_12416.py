from fnmatch import fnmatch

for i in range(2 * 7777, 10 ** 10 + 1, 2 * 7777):
    if fnmatch(str(i), '12*567?') and i % 2 == 0:
        print(i, i // 7777)
