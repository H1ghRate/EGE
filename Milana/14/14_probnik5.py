max_product = 1

for x in range(1, 100):
    for y in range(1, 100):
        b = 5 ** 50 + 5 ** 30 - 5 ** x - y - 5 ** y - x

        if b > 0:
            c_zero = 0

            while b:
                c_zero += b % 5 == 0
                
                b //= 5

            if c_zero == 10:
                max_product = max(max_product, x * y)

print(max_product)
