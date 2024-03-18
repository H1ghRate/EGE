with open("9_12463.csv") as f:
    counter = 0
    for i in f:
        row = list(map(int, i.split(';')))
        
        if len(set(row)) == 5:
            elem4, elem2 = -1, -1
            
            for elem in row:
                if row.count(elem) == 4:
                    elem4 = elem
                if row.count(elem) == 2:
                    elem2 = elem
                    
            if (elem4 != -1) and (elem2 != -1):
                sr_znach = (sum(row) - 4 * elem4 - 2 * elem2) / 3
                
                if sr_znach >= max(elem4, elem2):
                    counter += 1
    print(counter)
