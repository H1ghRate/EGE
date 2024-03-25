def f(s):
    l_pc = l_csgo = l_max = 0

    ch = False

    for x in range(0, len(s) - 1, 2):
        xy = (s[x] + s[x + 1])
        if xy == 'PC' and not ch:
            l_pc += 1
        if xy == 'CS' and not ch:
            ch = True
        elif xy == 'GO' and ch:
            l_csgo += 1
            ch = False
        else:
            l_max = max(l_max, l_pc * 2 + l_csgo * 4)

            ch = False
            l_pc = 0
            l_csgo = 0
    
    return l_max

s = open('24_9552.txt').readline()

print(f(s))
