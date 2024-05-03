# def f(a, b, c):
#     if a > b or a == c:
#         return 0
    
#     if a == b:
#         return 1
    
#     return f(a + 1, b, c) + f(a + 2, b, c) + f(a * 3, b, c)

f = lambda a, b, c: 0 if a > b or a == c else 1 if a == b else f(a + 1, b, c) + f(a + 2, b, c) + f(a * 3, b, c)

print(f(2, 9, 16) * f(9, 18, 16))

# 325
