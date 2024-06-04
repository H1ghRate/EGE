from functools import reduce

for i in range(1, 10 ** 6):
    s_d = sum(map(int, str(i)))

    pr_d = reduce(lambda res, curr: res * curr, [int(j) for j in str(i)])

    ans = ''.join([str(j) for j in sorted((s_d, pr_d))])

    if ans ==  '3522050':
        print(i)
        break
