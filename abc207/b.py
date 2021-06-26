a,b,c,d=map(int,input().split())
mz=a
ak=0
ans=0
for _ in range(10**5+1):
    if mz<=ak*d:
        break
    mz+=b
    ak+=c
    ans+=1
print(ans if mz<=ak*d else -1)
