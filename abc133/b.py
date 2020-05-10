n,d=map(int,input().split())
xs=[list(map(int,input().split())) for _ in range(n)]
ans=0
for i,y in enumerate(xs):
    for z in xs[i+1:]:
        s=sum([(a-b)**2 for a,b in zip(y,z)])**(1/2)
        if s==s//1:
            ans+=1
print(ans)
