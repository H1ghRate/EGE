# Доступен файл для чтения: 17.txt
with open('17.txt') as f:
  a = [int(i) for i in f]

x_max = max(i for i in a if 10 ** 4 <= i < 10 ** 5 and i % 100 == 17)

cnt = 0
min_s = max(a) * 3 + 1

for xs in zip(a, a[1:], a[2:]):
  f1 = any(abs(i) % 100 == 17 for i in xs)

  x_sum = sum(abs(i) for i in xs)

  f2 = x_sum <= x_max

  if f1 and f2:
    cnt += 1
    min_s = min(min_s, sum(xs))

print(cnt, min_s)
