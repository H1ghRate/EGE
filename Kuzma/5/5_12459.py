def perevod(num10: int, base: int) -> str:
    num_base = ''

    while num10 != 0:
        num_base += str(num10 % base)
        
        num10 //= base
    
    return num_base[::-1]


for n in range(1000, 0, -1):
    r = perevod(n, 4)

    size = len(r)

    if len(r) % 2 == 0:
        r = r[:len(r)//2] + '0' + r[-len(r)//2:]

    if int(r) <= 180:
        print(n)
        break
