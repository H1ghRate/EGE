s = open('./24_11241/24_11241.txt').readline()

s = s.replace('B', 'A')

s = s.replace('C', 'A')

s = s.replace('D', 'A')

s = s.split('A')

print(max(len(i) for i in s))
