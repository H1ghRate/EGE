s = open('24/24_11813/24_11813.txt').readline()

VOWELS = 'EYUIOA'

s = ['1' if i in VOWELS else '0' for i in s]

l0 = l_max = 1

last_sym = s[0]

for i in s[1:]:
    if i != last_sym:
        l0 += 1
    else:
        l_max = max(l0, l_max)

        l0 = 1

    last_sym = i

print(l_max)
