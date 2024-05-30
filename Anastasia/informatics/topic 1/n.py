ind = int(input())

nech = (ind // 2)
ch = (ind // 2 - (ind % 2 == 0))

n = ind * 45 + 9 * 60 + nech * 5 + ch * 15
a = int(n // 60) % 24
b = n % 60

print(a, b)
