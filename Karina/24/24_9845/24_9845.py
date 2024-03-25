s = open('24_9845.txt').readline()

s = s.replace('9', '8')

s = s.replace('B', 'A')
s = s.replace('C', 'A')

while '88' in s:
    s = s.replace('88', '8 8')

while 'AA' in s:
    s = s.replace('AA', 'A A')

print(max(len(i) for i in s.split()))
