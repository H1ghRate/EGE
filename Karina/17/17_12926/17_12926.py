a = [int(i) for i in open('./17_12926/17_12926.txt')]

x4 = 0

for x in zip(a, a[1:], a[2:], a[3:]):
    if (abs(x[0]) % 10) == (abs(x[1]) % 10) == (abs(x[2]) % 10) == (abs(x[3]) % 10) and sum(x) > x4:
        x4 = sum(x)

max_elem = max(i for i in a if 10 <= abs(i) < 100)

ans = []

for x in zip(a, a[1:], a[2:], a[3:], a[4:]):
    f1 = sum(1 for i in x if i < x4) == 1

    f2 = (sum(x) % max_elem) == 0

    if f1 and f2:
        ans.append(sum(x))

print(len(ans), min(ans))
