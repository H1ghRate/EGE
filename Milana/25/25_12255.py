from fnmatch import fnmatch

for i in range(98591 * 9, 10 ** 12, 985910):
    if fnmatch(str(i), '12?3*456??9'):
        print(i, i // 98591)