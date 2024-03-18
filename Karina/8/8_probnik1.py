from itertools import product as pr

cnt = 0

for word in pr('АКЛОШ', repeat=5):
    word = ''.join(word)

    cnt += 1

    if word == 'ШАЛАШ':
        print(cnt)
        break
