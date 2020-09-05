n,q=map(int,input().split())
x=[0]*n
y=[list(map(int,input().split())) for _ in range(q)]
for l,r,t in y:
    for i in range(l,r+1):
        x[i-1]=t
for v in x:
    print(v)
