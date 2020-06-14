l=list(map(int,input().split()))
for i,x in enumerate(l,start=1):
    if x==0:
        print(i)
        exit()
