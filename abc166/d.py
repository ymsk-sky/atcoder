x=int(input())
for a in range(-118, 120, 1):
    for b in range(-118, 120, 1):
        if ((a**5)-(b**5))==x:
            print(a,b)
            exit()
