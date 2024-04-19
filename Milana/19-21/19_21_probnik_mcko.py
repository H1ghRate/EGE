from functools import lru_cache

TO_WIN_VALUE = 436
MAX_VALUE = 435
MIN_VALUE = 1

TO_PLUS = [3]
TO_PRODUCT = [7]


def moves(n):
    variants = []

    for move in TO_PLUS:
        variants.append(n + move)

    for move in TO_PRODUCT:
        variants.append(n * move)

    return variants


@lru_cache(None)
def game(n):
    if n >= TO_WIN_VALUE:
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
    print(s, ':', game(s))
