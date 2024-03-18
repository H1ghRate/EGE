with open('9_probnik2.csv', 'r') as f:
    curr_line = 0
    max_line = 0
    
    for i in f:
        lst = list(map(int, i.split(';')))
        
        lst3 = [i for i in lst if lst.count(i) == 3]
        
        lst1 = [i for i in lst if lst.count(i) == 1]
    
        if len(lst3) == 3 and len(lst1) == 4 and (lst3[0] > (sum(lst) / 7)):
            max_line = curr_line

        curr_line += 1

print(max_line)
        