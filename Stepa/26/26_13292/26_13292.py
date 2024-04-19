with open('26_13292.txt') as f:
    n, k = map(int, f.readline().split())

    details = sorted(int(i) for i in f)[:k]

    for i in range(k - 1):
        if details[i] % 2 == 0:
            continue

        for j in range(i + 1, k):
            if details[j] % 2 == 0:
                details[i], details[j] = details[j], details[i]
                break

    ans = [0, 0]

    for i in range(n):
        if details[i] % 2 == 0:
            ans[0] = i + 2
        else:
            while i + 2 <= k:
                if details[i] % 2 != 0:
                    ans[1] += details[i]

                i += 1
            
            break
    
    print(ans)
