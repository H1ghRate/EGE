def algo(N):
    conda = "57" in N
    condb = "877" in N
    condc = "777" in N
    
    while conda or condb or condc:
        if conda:
            N = N.replace("57", "7", 1)
        condb = "877" in N
        if condb:
            N = N.replace("877", "75", 1)
        condc = "777" in N
        if condc:
            N = N.replace("777", "8", 1)
        conda = "57" in N
        condb = "877" in N
        condc = "777" in N
    return N

def summx(N):
    return sum(int(i) for i in N)

print(max(summx(algo("5"+"7"*n)) for n in range(4, 10001)))
