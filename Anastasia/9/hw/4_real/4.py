from itertools import combinations

cnt = 0

with open('4.csv') as f:
    for i in f:
        lst = list(map(int, i.strip().split(';')))  # array of elems in row
        
        if len(set(lst)) == 5:
            pairs = [i for i in combinations(lst, r=2)]  # array of all pairs in lst
            
            for i in range(len(pairs)):
                for j in range(i + 1, len(pairs)):
                    last_elem = sum(lst) - (sum(pairs[i]) + sum(pairs[j]))  # value of last_elem
                    
                    if sum(pairs[i]) / 2 == sum(pairs[j]) / 2 == last_elem:  # condition check
                        cnt += 1
                        
                        
print(cnt)
