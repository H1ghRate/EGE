name = '2344367'

i = 0

cnt = 0

while i < len(name):
    if int(name[i]) % 2 == 0:
        cnt += 1
    
    i += 1

print(cnt)
