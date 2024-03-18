def is_four_digit_num(n):
    return 1000 <= abs(n) <= 9999

def square_of_sum(a, b):
    return (a + b) ** 2


lst = [int(i) for i in open('17_9840.txt')]

max_elem = max(i for i in lst if is_four_digit_num(i) and abs(i) % 100 == 39)
max_elem *= max_elem

cnt = 0
max_sum = -200001

for x, y in zip(lst, lst[1:]):
    cnd1 = is_four_digit_num(x) and not is_four_digit_num(y) and (square_of_sum(x, y) <= max_elem)
    
    cnd2 = is_four_digit_num(y) and not is_four_digit_num(x) and (square_of_sum(x, y) <= max_elem)
    
    if cnd1 or cnd2:
        cnt += 1
        max_sum = max(max_sum, x + y)
        
print(f'Counter: {cnt}\nMaximumal summa: {max_sum}')
