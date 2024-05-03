with open('./26/26_13101/26_13101.txt') as f:
    n = int(f.readline())

    a = []

    for i in f:
        st, end, wnd = map(int, i.split())

        a.append((st, end, wnd))

a.sort()

times = [[0], [0]]

cnt2 = 0
cnt = 0

for st, end, wnd in a:
    if wnd == 0 and len(times[0]) <= len(times[1]):
        if len(times[0]) < 14:
            times[0].append(times[0][-1] + end)
            continue
        elif times[0][0] <= st:
            times[0].append(times[0][-1] + end)
            times[0].pop(0)
            continue

        if len(times[1]) < 14:
            times[1].append(times[1][-1] + end)
            cnt2 += 1
        elif times[1][0] <= st:
            times[1].append(times[1][-1] + end)
            times[1].pop(0)
            cnt2 += 1
        else:
            cnt += 1    
    elif wnd == 0 and len(times[0]) > len(times[1]):
        if len(times[1]) < 14:
            times[1].append(times[1][-1] + end)
            cnt2 += 1
            continue
        elif times[1][0] <= st:
            times[1].append(times[1][-1] + end)
            times[1].pop(0)
            cnt2 += 1
            continue
        

        if len(times[0]) < 14:
            times[0].append(times[0][-1] + end)
        elif times[0][0] <= st:
            times[0].append(times[0][-1] + end)
            times[0].pop(0)
            
        else:
            cnt += 1

    elif wnd == 1:
        if len(times[0]) < 14:
            times[0].append(times[0][-1] + end)
        elif times[0][0] <= st:
            times[0].append(times[0][-1] + end)
            times[0].pop(0)
        else:
            cnt += 1
    elif wnd == 2:
        if len(times[1]) < 14:
            times[1].append(times[1][-1] + end)
            cnt2 += 1
        elif times[1][0] <= st:
            times[1].append(times[1][-1] + end)
            times[1].pop(0)
            cnt2 += 1
        else:
            cnt += 1
    
print(cnt2, cnt)
