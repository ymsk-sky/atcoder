a,b=map(int,input().split())
for c in range(b,0,-1):
    if (a+c-1)//c<b//c:
        print(c)
        exit()
