# s = open('./24_14643/24_14643.txt').readline()

# curr = ''

# l_max = 0

# for i in s:
#     if 'AXMM' not in curr:
#         curr += i
#     else:
#         l_max = max(l_max, len(curr))

#         curr = curr[-3:] + i

# print(l_max - 1)

s = open('./24_14643/24_14643.txt').readline()

while 'AXMM' in s:
    s = s.replace('AXMM', 'AXM XMM')

print(max(len(i) for i in s.split()))
