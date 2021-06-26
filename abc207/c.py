n=int(input())
d=[list(map(int,input().split())) for _ in range(n)]
ans=0
def s(t,l,r):
    if t==1:
        return l,r
    elif t==2:
        return l,r-0.5
    elif t==3:
        return l+0.5,r
    else:
        return l+0.5,r-0.5
for i,(t1,l1,r1) in enumerate(d):
    l1,r1=s(t1,l1,r1)
    for t2,l2,r2 in d[i+1:]:
        l2,r2=s(t2,l2,r2)
        if l1<=l2<=r1 or r1>=r2>=l1 or (l2<=l1<=r2 and l2<=r1<=r2):
            ans+=1
print(ans)


"""
3
1 1 2
2 2 3
3 2 4

[1,2]: 1.0, 1.x, 2.0
[2,3): 2.0, 2.x
(2,4]: 2.x, 3.0, 3.x, 4.0

(1,2): 1.x, (1.x)
"""
