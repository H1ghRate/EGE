s = open('./24/24_15339/24_15339.txt').readline()

s = s.replace('B', 'A')
s = s.replace('C', 'A')

s = s.replace('7', '6')
s = s.replace('8', '6')
s = s.replace('9', '6')

while 'AA' in s:
    s = s.replace('AA', 'A A')

while '66' in s:
    s = s.replace('66', '6 6')

print(max(len(i) for i in s.split()))
