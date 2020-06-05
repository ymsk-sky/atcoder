n=int(input())
hs=list(map(int,input().split()))
c=0
m=max(hs)
while not m==0:
    b=0
    for i,h in enumerate(hs):
        if h==m:
            if not b==m:
                c+=1
            hs[i]-=1
        b=h
    m=max(hs)
print(c)
