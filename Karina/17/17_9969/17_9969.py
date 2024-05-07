from itertools import permutations as pr

a = [int(i) for i in open('./17_9969/17_9969.txt')]

max_elem = max(a, key=lambda x: (len(set(str(abs(x)))), x))

ans = []

for x in zip(a, a[1:], a[2:]):
    f1 = f2 = False
    for w, z, t in pr(x, r=3):
        if w >= 0 and ((z < 0 or (int(z ** 0.5) ** 2) != z)) and ((t < 0 or (int(t ** 0.5) ** 2) != t)):
            f1 = (int(w ** 0.5) ** 2) == w
            f2 = (z + t) >= max_elem

        if f1 and f2:
            ans.append(w)
            break

print(len(ans), sum(ans))
 
# from itertools import permutations as pr

# a = [int(i) for i in open('./17_9969/17_9969.txt')]

# max_elem = max(a, key=lambda x: (len(set(str(abs(x)))), x))

# ans = []

# for x, y, z in zip(a, a[1:], a[2:]):
#     d = [(x + y) if z >= 0 and (int(z ** 0.5) ** 2) == z else 0, 
#          (y + z) if x >= 0 and (int(x ** 0.5) ** 2) == x else 0,
#          (x + z) if y >= 0 and (int(y ** 0.5) ** 2) == y else 0]
    
#     if sum(x > 0 for x in d) == 1 and sum(d) >= max_elem:
#         ans.append(x + y + z - sum(d))
    
# print(len(ans), sum(ans))