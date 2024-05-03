with open("./27/27_2726/27B_2726.txt") as f:
    n = int(f.readline())

    x1 = x2 = 0

    for _ in range(n):
        x = int(f.readline())

        if x % 2 == 0 and x > x2:
            x2 = x
        
        if x % 2 != 0 and x > x1:
            x1 = x

print(x1 + x2)
