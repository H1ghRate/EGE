ABC = sorted('1234567890QWERTYUIOPASDFGHJKLZXCVBNM')

max_x_y = -1
ans = 0

for x in ABC[:22]:
    for y in ABC[:22]:
        x_y = int(x, 22) + int(y, 22)

        if x_y > max_x_y:
            max_x_y = x_y

            n1 = int(f'34256{x}4', 22)
            n2 = int(f'72847{y}3', 22)

            if (n1 + n2) % 125 == 0:
                ans = (n1 + n2) // 125

print(ans)
