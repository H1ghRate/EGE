with open('./24_7624/24_7624.txt') as f:
    s = f.readline()

l0 = l = 1

for x, y in zip(s, s[1:]):
    if x in 'XYZ' and y in 'XYZ':
        l = max(l, l0)
        l0 = 1
    else:
        l0 += 1
    
print(l)
