# summa = 0

# with open('./9_13824/9_13824.csv', 'r') as f:
#     ind = 0

#     for i in f:
#         ind += 1

#         a = list(map(int, i.split(';')))

#         b = True

#         for i in range(len(a) - 1):
#             if a[i] % 2 == a[i + 1] % 2:
#                 b = False

#                 break
        
#         if not b:
#             continue

#         s = 0
#         pr = 1
        
#         for i in range(len(a)):
#             b = True

#             for j in range(len(a)):
#                 if i != j and a[i] == a[j]:
#                     b = False
                    
#                     break
                    
#             if b:
#                 s += a[i]
#             else:
#                 pr *= a[i]

#         if (3 * s) >= pr:
#             summa += ind
    
# print(summa)

n = 0
with open('./9_13824/9_13824.csv') as f:
    c = 0
    for s in f:
        s = list(map(int, s.split(';')))
        c += 1
        k = [x for x in s if s.count(x) != 1]
        d = [x for x in s if s.count(x) ==1]
        l = 1
        for i in k:
            l = l*i
        if all(x%2 != y %2 for x,y in zip(s, s[1:])):
            if sum(d)*3 >= l:
                n+= c

                
print(n)