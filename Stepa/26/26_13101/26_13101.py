with open('26_13101.txt') as f:
    n = int(f.readline())

    a = []

    for i in f:
        st, end, wnd = map(int, i.split())

        a.append((st, end, wnd))

a.sort()

times = [[0], [0]]

cnt2 = 0

for st, end, wnd in a:
    if (wnd == 0 or wnd == 1) and len(times[0]) < 14:
        times[0].append(times[0][-1] + end)
        continue
    elif len(times[0]) >= 14 and times[0][0] <= st:
        times[0].append(times[0][-1] + end)
        times[0].pop(0)
        continue

    if wnd == 2 and len(times[1]) < 14:
        times[1].append(times[1][-1] + end)
        cnt2 += 1
    elif len(times[1]) >= 14 and times[1][0] <= st:
        times[1].append(times[1][-1] + end)
        times[1].pop(0)
        cnt2 += 1
    
print(cnt2)
