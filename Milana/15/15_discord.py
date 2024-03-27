s = []
def f(x):
    return ((not(( 13 <= x <= 38) <= ((10 <= x <= 21) or (18 <= x <= 25)))) <= ((not(a1 <= x <= a2)) <= (not(13 <= x <= 38))))

a = [i / 4 for i in range(10 * 4, 39 * 4 + 1)]

for i in range(len(a)):
    for j in range(len(a)):
       a1 = a[i]
       a2 = a[j]

       if all((f(x) == 1) for x in a):
           s.append(a2-a1)
print(min(s))
