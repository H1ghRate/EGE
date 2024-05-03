cnt = 0

with open('./9/9_15321/9_15321.csv') as f:
    for i in f:
        line = sorted(list(map(int, i.split(';'))))

        is_changed = False

        if line[-1] < sum(line[:3]):
            for j in range(4):
                for k in range(j + 1, 4):
                    if (line[j] + line[k]) == (sum(line) - (line[j] + line[k])):
                        cnt += 1
                        print(line[j] + line[k], sum(line) - (line[j] + line[k]))
                        is_changed = True
                        break
                
                if is_changed:
                    break

print(cnt)