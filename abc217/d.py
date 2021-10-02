import array
import bisect
l,q=map(int,input().split())
edges=array.array('I',[0,l])
for _ in range(q):
    c,x=map(int,input().split())
    i=bisect.bisect_left(edges,x)
    if c==1:
        edges.insert(i,x)
    else:
        print(edges[i]-edges[i-1])
