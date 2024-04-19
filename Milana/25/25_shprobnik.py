from fnmatch import fnmatch

cnt = 0

for i in range(8, 680_001, 8):
    if fnmatch(str(i), '1*2*'):
        cnt += 1

print(cnt)
