n,k=map(int,input().split())
s=[int(input()) for _ in range(n)]
ans=0
cnt=0
p_end=0
val=1
for p_top in range(n):
    current=s[p_top]
    if current==0:
        print(n)
        exit()
    val*=current
    cnt+=1
    if val<=k:
        ans=max(ans,cnt)
    else:
        val//=s[p_end]
        p_end+=1
        cnt-=1
print(ans)
