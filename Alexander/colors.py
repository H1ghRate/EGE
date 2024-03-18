clr1 = input('Color 1: ')
clr2 = input('Color 2: ')

colors = ['blue', 'red', 'yellow']

if any(clr1 == i for i in colors) and any(clr1 == i for i in colors) and\
    clr1 == clr2:
    print('Mixed color:', clr1)
elif clr1.lower() == colors[0] and clr2.lower() == colors[1] or\
    clr1.lower() == colors[1] and clr2.lower() == colors[0]:
        print('Mixed color: purple')
elif clr1.lower() == colors[2] and clr2.lower() == colors[0] or\
clr1.lower() == colors[0] and clr2.lower() == colors[2]:
    print('Mixed color: green')
elif clr1.lower() == colors[2] and clr2.lower() == colors[1] or\
clr1.lower() == colors[1] and clr2.lower() == colors[2]:
    print('Mixed color: orange')
else:
    print('Undefined colors!')
