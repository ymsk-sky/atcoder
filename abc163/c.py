n=int(input())
as_=list(map(int,input().split()))
l=[0 for _ in range(n)]
for a in as_:
    l[a-1]+=1
for c in l:
    print(c)
