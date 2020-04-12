n,k=map(int,input().split())
hs=list(map(int,input().split()))
hs.sort()
print(sum(hs) if k==0 else sum(hs[:-k]))
