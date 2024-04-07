s = open('./24_11954/24_11954.txt').readline()

l_min = 1543965436456

idx = []

for i in range(len(s)):
    if s[i] == 'X':
        idx.append(i)

    if s[i] == 'Y':
        idx = [i + 1]
    
    while len(idx) >= 500:
        l_min = min(l_min, i - idx[0] + 1)

        idx = idx[1:]

print(l_min)
