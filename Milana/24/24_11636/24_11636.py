s = open('./24_11636/24_11636.txt').readline()

ans = curr = 0

last_elem = s[0]

for i in s[1:]:
    if i == 'A':
        ans += curr - (last_elem == 'A')

        curr += 1

    last_elem = i

print(ans)
