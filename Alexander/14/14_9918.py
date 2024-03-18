nums = set()

for x in range(10, 67):
    for y in range(x):
        num1 = 7 * 67 ** 4 + 3 * 67 ** 3 + x * 67 ** 2 + 67 + y
        num2 = 4 * x ** 3 + 9 * x ** 2 + y * x + 6

        nums.add(num1 + num2)

print(len(nums))
