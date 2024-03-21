s = open('24_9845.txt').readline()

s = s.replace('B', 'A').replace('C', 'A').replace('9', '8')

while 'AA' in s:
    s = s.replace('AA', 'A A')

while '88' in s:
    s = s.replace('88', '8 8')

print(max(len(l) for l in s.split()))
