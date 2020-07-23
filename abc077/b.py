n=int(input())
for i in range(n,0,-1):
    j=i**(1/2)
    if j/1==j//1:
        print(i)
        exit()
