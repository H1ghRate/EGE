with open('example3.txt') as f:
    n = int(f.readline())
    a = [int(i) for i in f]
    pref_a = [0] * (n + 1)
    for i in range(n):
        pref_a[i + 1] = a[i] + pref_a[i]
    sums = [float('inf')] * 10
    mx = float('-inf')
    for i in range(n + 1):
        s = (pref_a[i] - pref_a[0])
        mx = max(mx, s - sums[s % 10])
        sums[s % 10] = min(sums[s % 10], s)

    print(mx)
#48430

with open('example3.txt') as f:
     n = int(f.readline())
     a = [int(i) for i in f]
     mx = float('-inf')
     for i in range(n):
         s = a[i]
         for j in range(i + 1, n):
             s += a[j]
             if s % 10 == 0:
                 if s > mx:
                     mx = s
                     print(i, j)
     print(mx)

