from itertools import permutations as pr

cnt = 0

for i in pr('КАБИНЕТ', r=7):
    s = ''.join(i)

    if s[-1] not in 'АИЕ':
        cnt += 1

print(cnt)
