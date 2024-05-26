with open('./24_yandex7/24_yandex7.txt') as f:
    s = f.readline()

# l = ''

# l_max = 0

# for i in s:
#     if 'AHAHA' not in l:
#         l += i

#         if i == s[-1]:
#             l_max = max(l_max, len(l) - 1)
#     else:
#         if (len(l) - 1 > l_max):
#             print('-' * 20)
#             print(l)
#             l_max = len(l) - 1

#         l = l[-4:] + i

# print(l_max)

m = [0] * len(s)

m[0] = 1
m[1] = 2
m[2] = 3
m[3] = 4

for i in range(4, len(s)):
    if (s[i - 4] + s[i - 3] + s[i - 2] + s[i - 1] + s[i]) != 'AHAHA':
        m[i] = 1 + m[i - 1]
    else:
        m[i] = 4
    
print(max(m))

while 'AHAHA' in s: s = s.replace('AHAHA', 'AHAHA AHAHA')

print(max(len(i) for i in s.split()))
