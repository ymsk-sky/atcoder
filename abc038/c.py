n=int(input())
l=list(map(int,input().split()))+[-1]
ans=0
cnt=0
pre=-1
for a in l:
    if a>pre:
        cnt+=1
    else:
        ans+=cnt*(cnt+1)//2
        cnt=1
    pre=a
print(ans)
