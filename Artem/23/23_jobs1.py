b = set()

def f(n, c=0):
    if c == 13:
        b.add(n)
        return

    f(n * 6, c + 1), f(n // 2, c + 1)

f(1024)
print(len(b))