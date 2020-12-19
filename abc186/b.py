h,w=map(int,input().split())
al=[list(map(int,input().split())) for _ in range(h)]
min_=float('inf')
for a in al:
    min_=min(min_,min(a))
ans=0
for a in al:
    ans+=sum([v-min_ for v in a])
print(ans)
