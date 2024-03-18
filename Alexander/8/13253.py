from collections import defaultdict
from itertools import product as pr

words = defaultdict(int)

for syms in pr('КОНЕЦ', repeat=5):
    word = ''.join(syms)
    words[word] += 1

for syms in pr('ДРАКОН', repeat=5):
    word = ''.join(syms)
    words[word] += 1

print('Counter:', sum(i == 1 for i in words.values()))
