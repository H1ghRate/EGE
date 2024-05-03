s = open('./24/24_probnik_yandex4/24_probnik_yandex4.txt').readline()

ABC = 'QWERTYUIOPSDFGHJKLZXCVBNM'

for i in ABC:
    s = s.replace(i, 'A')

max_num = 0

for i in s.split('A'):
    if len(i) == 0:
        continue

    num = int(i)

    if num > max_num and num % 2 == 0:
        max_num = num

print(max_num)
