s = open('./24_12410/24_12410.txt').readline()

st = end = 1

l_max = 0

errors = 0

for i in range(1, len(s)):
    errors += (s[end - 1] + s[end]) != ''.join(sorted(s[end - 1] + s[end]))

    while errors > 1e5:
        errors -= (s[st - 1] + s[st]) != ''.join(sorted(s[st - 1] + s[st]))

        st += 1

    end += 1

    if errors == 1e5:
        l_max = max(l_max, end - st)

print(l_max + 1)
