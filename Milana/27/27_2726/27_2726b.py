with open("./27/27_2727/27B_2727.txt") as f:
    n = int(f.readline())

    x1 = x31 = x31_prev = float('inf')

    for _ in range(n):
        x = int(f.readline())

        if x % 31 == 0 and x < x31:
            x31 = x
        elif x % 31 == 0 and x < x31_prev:
            x31_prev = x
        elif x < x1:
            x1 = x

print(min(x1 * x31, x31 * x31_prev))
