alphabet = "0123456789ABCDEF"

def atoa(N, b):
    R = []
    Rn = []
    while N > 0:
        R.append(N%b)
        Rn.append(N%b)
        N//=b
    for i in range(len(R)):
        R[i] = alphabet[R[i]]
    r = ""
    for i in R[::-1]:
        r+=i
    return r, Rn[::-1]

x = 0
for i in range(8**6, 8**7):
    R, Rn = atoa(i, 8)
    choot = 0
    valid = True
    if len(R) == 7:
        for j in range(len(Rn)):
            if Rn[j] % 2 == 0: choot += 1
        if choot == 2:
            if not((Rn[0] == 7 and Rn[1] % 2 == 0) or (Rn[0] != 7 and (Rn[0] % 2 != 0 and Rn[1] != 7) or Rn[0] % 2 == 0)):
                continue

            if not((Rn[-1] == 7 and Rn[-2] % 2 == 0) or (Rn[-1] != 7 and (Rn[-1] % 2 != 0 and Rn[-2] != 7) or Rn[-1] % 2 == 0)):
                continue

            for j in range(len(Rn)-2):
                if Rn[j+1] == 7:
                    if Rn[j] % 2 == 1 or Rn[j+2] % 2 == 1:
                        valid = False
                        break

            if valid: x += 1

print(x)
