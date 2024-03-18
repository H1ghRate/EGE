f = [0] * 7000

for n in range(1, 6 + 1):
    f[n] = n

for n in range(7, 6200):
    f[n] = 2 * n + 3 + f[n - 1]

print(f[6188] - f[6185])
