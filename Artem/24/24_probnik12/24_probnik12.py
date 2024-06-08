with open('./24_probnik12/24_probnik12.txt') as f:
    s = f.readline()

G = 'AEIOUY'

st = end = 2

c_ccg = 0

l_min = len(s) + 1

for i in range(2, len(s)):
    end += 1

    c_ccg += (s[i - 2] not in G and s[i - 1] not in G and s[i] in G)

    while c_ccg > 500:
        c_ccg -= (s[st - 2] not in G and s[st - 1] not in G and s[st] in G)

        st += 1

    while st < len(s) and not (s[st - 2] not in G and s[st - 1] not in G and s[st] in G):
        st += 1
    
    if c_ccg >= 500:
        l_min = min(l_min, end - st)

print(l_min + 2)
