n=int(input())
abl=[list(map(int,input().split())) for _ in range(n)]
t=0
for a,b in abl:
    t+=a/b
t/=2
u=0
ans=0
for a,b in abl:
    u+=a/b
    if t<=u:
        u-=a/b
        t-=u
        ans+=b*t
        break
    ans+=a
print(ans)
