s = open('./24_11636.txt').readline()

l = 0
k = 0
last_elem = s[0]

for i in s[1:]:
    if i == 'A':
        k += l - (last_elem == 'A')
        
        l += 1
    
    last_elem = i

print(k)
