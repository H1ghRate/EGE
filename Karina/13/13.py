##bit1, bit2, bit3, bit4 = map(int, input().split())
##
##print(f'{bin(bit1)[2:]}.{bin(bit2)[2:]}.{bin(bit3)[2:]}.{bin(bit4)[2:]}')

cnt = 0

summa = 0

for j in range(0, 8):
    t = bin(j)[2:]
    
    s = t.count('0') + 3 - len(t)
    
    for i in range(0, 32):
        n = bin(i)[2:]

        
        
        if (s + n.count('0') + 5 - len(n)) <5:
            cnt += 1
            print(t, n, '+')
        else:
            print(t, n, '-')

    summa += cnt
    
    cnt = 0
    
        

print(summa)
