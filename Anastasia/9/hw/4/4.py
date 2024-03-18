from itertools import product

cnt = 0

with open('4.csv') as f:
    for i in f:
        lst = list(map(int, i.strip().split(';')))
        
        if len(set(lst)) == 5:
            for x in product(lst, repeat=2):
                for y in product(lst, repeat=2):
                    last_elem = sum(lst) - sum(x) - sum(y)
                    if x != y and sum(x) / 2 == sum(y) / 2 == last_elem:
                        cnt += 1
                        
print(cnt)
