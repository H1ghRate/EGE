cnt = 0

for x in open("1.csv"):
    lst = map(int, x.strip().split(";"))
    
    k = 0
    summa = 0
    
    for num in lst:
        k += num == 18
        summa += num
        
    if k == 5 or summa % 18 == 0:
        cnt += 1
        
print(cnt)

# 923 - ans