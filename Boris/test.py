print('Creating positive tests.')
n = int(input('n = '))
if n != 0:
    i = int(input('i = '))

    for j in range(i, n + i):
        with open(f'./func_tests/data/pos_0{j}_in', 'w') as f:
            s = input(f'pos_0{j}_in: ') + '\n'
            
            f.write(s)
        with open(f'./func_tests/data/pos_0{j}_out', 'w') as f:
            s = input(f'pos_0{j}_out: ') + '\n'
            
            f.write(s)
    
    print('All inputed positive cases are created.')

print('Creating negative tests.')
n = int(input('n = '))

if n != 0:
    i = int(input('i = '))

    for j in range(i, n + i):
        with open(f'./func_tests/data/neg_0{j}_in', 'w') as f:
            s = input(f'neg_0{j}_in: ') + '\n'
            
            f.write(s)
        with open(f'./func_tests/data/neg_0{j}_out', 'w') as f:
            s = input(f'neg_0{j}_out: ') + '\n'
            
            f.write(s)
    
    print('All inputed negavite cases are created.')
