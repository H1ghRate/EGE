from itertools import permutations

ABC = '01234567'

cnt = 0

for word in permutations(ABC, r=6):
    word = ''.join(word)

    if (word[0] != '0' and '3' not in word):
        for i in ABC:
            word = word.replace(i, str(int(i) % 2))
            
        if '00' in word:
            cnt += 1

print(cnt)