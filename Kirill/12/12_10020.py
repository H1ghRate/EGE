max_fives = 0
n_min = 0

for n in range(51, 10000):
    s = n * '5'

    while '55555' in s:
        s = s.replace('55555', '88', 1)
        s = s.replace('888', '55', 1)              

    if s.count('5') > max_fives:
        max_fives = s.count('5')
        n_min = n 

print(n_min)