with open('./24/24_jobs1/24_jobs1.txt') as f:
    s = f.readline()

l = l_max = 0

t = ''

for i in range(0, len(s), 2):
    word = s[i] + s[i + 1]

    if any(word == needed for needed in ['XM', 'NF', 'EO']):
        l += 1
        t += word
    else:
        l_max = max(l_max, l * 2)

        if (l_max == 104):
            print(t)
            break

        t = ''

        l = 0

print(l_max)
# 90
