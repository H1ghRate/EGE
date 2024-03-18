with open('24.txt') as f:
    s = f.readline()

cnt = k = 0
last = s[0]
for i in s[1:]:
    if i == 'A':
        cnt += k - (last == 'A')
        k += 1

    last = i

print(cnt)
