n,m,x=map(int,input().split())
l=list(map(int,input().split()))
a=[1 if i in l else 0 for i in range(1,n)]
print(min(sum(a[:x-1]),sum(a[x:])))
