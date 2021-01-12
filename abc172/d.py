n=int(input())
ans=0
for j in range(1,n+1):
    y=n//j
    g=y*(y+1)*j//2
    ans+=g
print(ans)
