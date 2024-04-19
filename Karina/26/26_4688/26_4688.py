from collections import defaultdict

with open('./26_4688.txt') as f:
    n = int(f.readline())

    homes = defaultdict(list)

    p_g = defaultdict(list)

    for info in f:
        home, podъezd = map(int, info.split())

        homes[home].append(podъezd)
    
    for home in homes:
        ps = homes[home]

        if len(ps) < 3:
            continue

        for p in ps:
            for i in [p - 1, p + 1]:
                if i in ps:
                    continue

                left = right = 0

                pf = i - 1

                while pf > 0 and pf in ps:
                    left += 1
                    pf -= 1

                pf = i + 1

                while pf <= max(ps) and pf in ps:
                    right += 1
                    pf += 1
                
                if (right + left) >= 3:
                    p_g[home].append(i)

print(sum(1 for i in p_g if len(p_g[i]) != 0))

print(min(p_g[max(p_g.keys())]))
