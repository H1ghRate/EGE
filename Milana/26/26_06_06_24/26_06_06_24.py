with open('26_06_06_24.txt') as f:
    k = int(f.readline())
    m = int(f.readline())
    n = int(f.readline())

    reviews = []

    for review in f:
        time, vagon, mesto = map(int, review.split())

        reviews.append((time, vagon, mesto))

reviews.sort()

vagons = {i: [] for i in range(1, k + 1)}

cnt = 0
last_review = 0

for time, vagon, mesto in reviews:
    if 1 <= mesto <= m and mesto not in vagons[vagon]:
        vagons[vagon].append(mesto)
        last_review = vagon + mesto
    else:
        ind = 1
        
        while ind <= k and len(vagons[ind]) == m:
            ind += 1

        if (ind == (k + 1)):
            continue

        cnt += 1

        for i in range(1, m + 1):
            if i not in vagons[ind]:
                vagons[ind].append(i)
                last_review = ind + i
                break

print(cnt, last_review)
