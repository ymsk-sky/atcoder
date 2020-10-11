n=int(input())
l=list(map(int,input().split()))
t=[0]*(2*10**5+1)
at=0
for p in l:
    t[p]+=1
    while t[at]:
        at+=1
    print(at)
