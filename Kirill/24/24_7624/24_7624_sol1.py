with open('./24_7624/24_7624.txt') as f:
    s = f.readline()

s = s.replace('Y', 'X').replace('Z', 'X')

while 'XX' in s:
    s = s.replace('XX', 'X X')

print(max(len(i) for i in s.split()))
