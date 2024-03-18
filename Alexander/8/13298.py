from itertools import product as pr

cnt = 1
k = 1

for syms in pr(sorted('привычка'), repeat=5):
    word = ''.join(syms)
    if k % 5 == 0:
        k += 1
        continue
    if len(set(word)) == 5 and all(sym not in 'ыаи' for sym in word):
        print('Word:', word, '\nCounter:', cnt)
        break
    cnt += 1
    k += 1
