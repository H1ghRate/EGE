from functools import lru_cache

TO_WIN_VALUE = 175
MAX_VALUE = 154
MIN_VALUE = 1
STARTED_VALUE = 19

TO_PLUS = [1]
TO_PRODUCT = [3]


def moves(n):
    variants = []

    elem1, elem2 = n

    for move in TO_PLUS:
        variants.append((elem1 + move, elem2))
        variants.append((elem1, elem2 + move))

    for move in TO_PRODUCT:
        variants.append((elem1 * move, elem2))
        variants.append((elem1, elem2 * move))

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
