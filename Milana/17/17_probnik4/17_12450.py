f = [int(i) for i in open('17_probnik4/17_12450.txt')]

c = 0
max_summa = 0

min_element = min(i for i in f if abs(i) % 52 ==0)

for xs in zip(f, f[1:], f[2:]):
    f1 = sum(abs(i) % 113 for i in xs)

    if f1 == min_element:
        c += 1

        max_summa = max(max_summa, sum(xs))
        
print(c, max_summa)