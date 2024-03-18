for x in sorted('1234567890qwertyuiopasdfghjklzxcvbnm')[:27]:
    a = int(f'17{x}35', 27) + int(f'{x}742M', 27) + int(f'{x}', 27)**3
    if a % 23 == 0:
        print(a//23)