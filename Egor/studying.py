PRICE_OF_ONE_BOTTLE = 50

CASHBACK_FROM_ONE_BOTTLE = 10

sum_of_coins = int(input('Summa of coins: '))

if (sum_of_coins < 50):
    print('Number of bottles: 0\n')
else:
    print(f'Number of bottles: {sum_of_coins//(PRICE_OF_ONE_BOTTLE - CASHBACK_FROM_ONE_BOTTLE)}\n')
