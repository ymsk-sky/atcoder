a,b,k=map(int,input().split())
al=list(range(a,min(b+1,a+k)))
bl=list(range(max(a,b-k+1),b+1))
l=sorted(set(al+bl))
for v in l:
    print(v)
