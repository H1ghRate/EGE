with open('./27_yandex7/27A_yandex7.txt') as f:
    k, n = map(int, f.readline().split())

    a = [int(i) for i in f]

ss = float('inf')

def f(a: list, ind: int, s: int) -> int:
    if ind >= n:
        if ind == n:
            global ss

            ss = min(ss, s)

        return

    s += a[ind]
    
    for i in range(1, k + 1):
        f(a, ind + i, s)
    
    return s


print(f(a, 0, 0))
