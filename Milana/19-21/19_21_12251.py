from functools import lru_cache

TO_WIN_VALUE = 117
MAX_VALUE = 4000
MIN_VALUE = 116

TO_PLUS = [7]
TO_PRODUCT = [3]


def moves(n):
    variants = []

    for move in TO_PLUS:
        variants.append(n - move)

    for move in TO_PRODUCT:
        variants.append(n // move)

    return variants


a = ['W'] * 116 + [0] * 11000



for s in range(MIN_VALUE, MAX_VALUE + 1):
    if s < TO_WIN_VALUE:
        a[s] = 'W'
    elif any(a[m] == 'W' for m in moves(s)):
        a[s] = 'B1'
    elif any(a[m] == 'B1' for m in moves(s)):
        a[s] = 'L1'
    elif any(a[m] == 'L1' for m in moves(s)):
        a[s] = 'B2'
    elif all(a[m] == 'B1' or a[m] == 'B2' for m in moves(s)):
        a[s] = 'L2'
    elif any(a[m] == 'L2' for m in moves(s)):
        a[s] = 'B3'

    if a[s] == 'B2':
        print(s, ':', a[s])
    
    