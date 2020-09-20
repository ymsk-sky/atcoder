n,d,k=map(int,input().split())
h=[list(map(int,input().split())) for _ in range(d)]
for _ in range(k):
    s,t=map(int,input().split())
    p=s
    if s<t:
        for i,(l,r) in enumerate(h,start=1):
            if l<=p<=r:
                p=r
            if p>=t:
                print(i)
                break
    else:
        for i,(l,r) in enumerate(h,start=1):
            if l<=p<=r:
                p=l
            if p<=t:
                print(i)
                break
