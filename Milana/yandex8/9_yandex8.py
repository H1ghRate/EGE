# Доступны файлы для чтения: 9.csv, 9.ods, 9.xls, 9.xlsx
with open('9.csv') as f:
  cnt = 0
  
  for ind, i in enumerate(f, 1):
    a = list(map(int, i.split(';')))

    x2 = [i for i in a if a.count(i) == 2]

    x3 = [i for i in a if a.count(i) == 3]

    x1 = [i for i in a if a.count(i) == 1]

    if len(x2) // 2 == 1 and len(x3) // 3 == 1 and len(x1) == 3:
      if x3[0] > x2[0]:
        cnt += 1

    if cnt == 3:
      print(ind)
    
      break
