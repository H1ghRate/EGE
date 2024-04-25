from functools import lru_cache

TO_WIN_VALUE = 189
MAX_VALUE = 183
MIN_VALUE = 1
STARTED_VALUE = 5

def moves(n):
    variants = []

    elem1, elem2 = n

    variants.append((elem1 + elem2, elem2))
    variants.append((elem1, elem2 + elem1))

    variants.append((max(elem1, elem2), max(elem1, elem2)))
    
    return variants


@lru_cache(None)
def game(n):
    if sum(n) >= TO_WIN_VALUE:
        return 'W'
    if any(game(m) == 'W' for m in moves(n)):
        return 'B1'
    if all(game(m) == 'B1' for m in moves(n)):
        return 'L1'
    if any(game(m) == 'L1' for m in moves(n)):
        return 'B2'
    if all(game(m) == 'B1' or game(m) == 'B2' for m in moves(n)):
        return 'L2'
    if any(game(m) == 'L2' for m in moves(n)):
        return 'B3'


for s in range(MAX_VALUE, MIN_VALUE - 1, -1):
    print(s, ':', game((STARTED_VALUE, s)))
