s = 7 * 5**123 + 6 * 5**111 - 5 * 25**50 + 4 * 125**30 - 3 * 5**10

cnt = 0
while s:
    cnt += (s % 5) == 4

    s //= 5

print(cnt)