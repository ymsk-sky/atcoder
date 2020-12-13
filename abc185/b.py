n,m,t=map(int,input().split())
nm=n
abs=[list(map(int,input().split())) for _ in range(m)]
tmp=0
for a,b in abs:
    n-=a-tmp
    if n<=0:
        print('No')
        exit()
    n+=b-a
    if n>nm:
        n=nm
    tmp=b
n-=t-b
print('Yes' if n>0 else 'No')
