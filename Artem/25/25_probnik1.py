from fnmatch import fnmatch
from progress.bar import Bar

n = 0
summa = 0

for i in range(128140, 10**10 + 1, 596):
    if fnmatch(str(i), '1*28?64'):
        n += 1
        summa += i
    elif int(str(i)[0]) >= 2:
        i = 10 ** (len(str(i)) + 1)
        if i % 596 != 0:
            i += 596 - i % 596


print(n, summa / n)
