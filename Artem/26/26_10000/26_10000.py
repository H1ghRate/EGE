with open('26_10000.txt') as f:
    n, k = map(int, f.readline().split())

    disks = []

    for i in f.readline().split():
        disk_size = int(i)
        
        disks.append(disk_size)

    imp_files = []

    simple_files = []

    for _ in range(n):
        file_size, imp = map(int, f.readline().split())
        
        if imp == 1:
            simple_files.append(file_size)
        else:
            imp_files.append(file_size)

imp_files.sort(reverse=True)
simple_files.sort(reverse=True)

cssf = 0

max_space = -1

for i in range(k):
    s = 0

    while len(imp_files) != 0 and s + imp_files[-1] <= disks[i]:
        s += imp_files.pop()
    
    while len(simple_files) != 0 and s + simple_files[-1] <= disks[i]:
        s += simple_files.pop()
        cssf += 1
    
    max_space = max(max_space, disks[i] - s)

print(cssf, max_space)
