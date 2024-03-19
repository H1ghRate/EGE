def f(a: int, c: int) -> int:
    if c > 4:
        return

    global numbers

    if c == 4:
        numbers.add(a)
    
    return f(a + 2, c + 1), f(a * 3, c + 1)

numbers = set()

f(1, 0)

print(len(numbers))
