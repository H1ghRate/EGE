from itertools import permutations as pr

b = set()

for i in pr('ПРОСТО', r=6):
    s = ''.join(i)
    
    if all(x != y for x, y in zip(s, s[1:])):
        b.add(s)

print(len(b))
