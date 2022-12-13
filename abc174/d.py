n=int(input())
cs=input()
lw=0
rr=cs.count('R')
ans=max(lw,rr)
for c in cs:
    if c=='W':
        lw+=1
    else:  # c=='R'
        rr-=1
    tmp=max(lw,rr)
    ans=min(ans,tmp)
print(ans)
