cnt = 0

for a in range(1, 11_111 + 1):
    cnt += all((a % x == 0) <= (x == a) or (x == 1) for x in range(1, 11112))

print(cnt)
 