x=int(input())
k=len(str(x))//2
for a in range(-10**k, 10**k, 1):
    for b in range(-10**k, 10**k, 1):
        if ((a**5)-(b**5))==x:
            print(a,b)
            exit()
