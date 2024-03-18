max5 = 0
min_n = 1001
for i in range(51, 1000):
    n = i * '5'
    
    while '55555' in n:
        n = n.replace('55555', '88', 1)
        n = n.replace('888', '55', 1)
    
    if n.count('5') > max5:
        max5 = n.count('5')
        min_n = i

print(min_n)