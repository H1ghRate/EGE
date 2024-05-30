# Доступен файл для чтения: 24.txt
with open('24.txt') as f:
  s = f.readline()

st = end = 0

c_e = 0

l_min = len(s) + 1

for i in s:
  end += 1

  c_e += i == 'E'

  while c_e > 240:
    c_e -= s[st] == 'E'

    st += 1

  while st < len(s) and s[st] != 'E':
    st += 1

  if c_e >= 240:
    l_min = min(l_min, end - st)

print(l_min)