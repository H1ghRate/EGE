f = open('24_14100.txt')
s = f.readline()
dp = [0] * len(s)
prim = ['ABA', 'CB', 'AC' , 'BB', 'ABC', 'BCB', 'BA', 'AB']

for i in range(1, len(s)):
    for j in prim:
        if i >= len(j) - 1:
            if s[i-len(j)+1:i+1]==j:
                dp[i] = max(dp[i], dp[i-len(j)] + len(j))
                
print(max(dp))