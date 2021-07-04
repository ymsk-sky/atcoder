import bisect
n,k=map(int,input().split())
al=list(map(int,input().split()))
bl=sorted(al)
l=[0]*n  # 順序リスト
for i,a in enumerate(al):
    x=bisect.bisect_right(bl,a)
    l[i]=x
base=k//n
mod=k%n
for x in l:
    if x>mod:
        print(base)
    else:
        print(base+1)
