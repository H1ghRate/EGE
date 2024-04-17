cnt = 0

a = int(input())

if a != -1:
    b = int(input())

    if b != -1:
        while (c := int(input())) != -1:
            if b > a and b > c:
                cnt += 1
            
            a, b = b, c
            
print(cnt)
