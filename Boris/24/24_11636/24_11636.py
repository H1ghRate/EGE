s = open('./24/24_11636/24_11636.txt').readline()

amount = 0
c_a = s[0] == 'A'
last_elem = s[0]

for i in s[1:]:
    if i == 'A':
        amount += c_a - (last_elem == 'A')

        c_a += 1

    last_elem = i
    
print(amount)
