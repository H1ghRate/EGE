with open('./26/26_9756/26_9756.txt') as f:
    n = int(f.readline())

    requests = []
    
    for info in f:
        st, end = map(int, info.split())

        requests.append((st, end))
    
requests.sort(key=lambda x: x[1])

cnt = 0
latest_time = 0

last_time = 0
last_start = 0

for st, end in requests:
    if st >= last_time:
        last_start = last_time

        last_time = end
        
        cnt += 1

for st, end in requests:
    if st >= last_start:
        latest_time = max(latest_time, end)

print(cnt, latest_time)
