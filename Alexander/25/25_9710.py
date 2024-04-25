from fnmatch import fnmatch

a = []

for i in range(1000001268, 10**10, 2023):
    if fnmatch(str(i), '1*1'):
       a.append(i)

a.sort(key=lambda x: sum(map(int, str(x))))

for i in a[-5:]:
    print(i // 2023)
