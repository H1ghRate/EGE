from itertools import product as pr

cnt = 1

for word in pr('АКЛОШ', repeat=5):
    word = ''.join(word)
    
    if word == 'ШАЛАШ':
        print(cnt)
        break
    
    cnt += 1
    