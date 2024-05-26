with open('./24_probnik_yandex7/24_probnik_yandex7.txt') as f:
    s = f.readline()

while 'AHAHA' in s: s = s.replace('AHAHA', 'AHAH HAHA')

print(max(len(i) for i in s.split()))
