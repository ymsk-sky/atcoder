n,m=map(int,input().split())
l=sorted(list(map(int,input().split())))
if n>=m:
    print(0)
    exit()
s=l[-1]-l[0]
l=sorted([a-b for a,b in zip(l[1:],l)], reverse=True)
print(s-sum(l[:n-1]))
