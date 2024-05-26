with open('./27_2945/27B_2945.txt') as f:
    n = int(f.readline())
    a = [int(i) for i in f]

k = 67

osts = [[-1, -1] for _ in range(k)]

osts[0] = [0, 0]

s = 0
for el in a:
    s += el

    if osts[s % k][0] == -1:
        osts[s % k][0] = s
    
    osts[s % k][1] = s

max_s = -1

for ost in range(k):
    if osts[ost][0] != -1 and osts[ost][1] != -1:
        max_s = max(max_s, osts[ost][1] - osts[ost][0])
    
print(max_s)
    