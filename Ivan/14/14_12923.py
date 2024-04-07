BASE = 25

b = 3 * 3125 ** 9 + 2 * 625 ** 8 - 4 * 625 ** 7 + 3 * 125 ** 6 - 2 * 25 ** 5 - 2024

cnt = 0

while b != 0:
    if b % BASE == 0:
        cnt += 1
    
    b //= BASE

print(cnt)
