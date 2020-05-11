n=int(input())
ps=list(map(int,input().split()))
c=0
for i in range(1,n-1):
    p1=ps[i-1]
    p2=ps[i]
    p3=ps[i+1]
    if p1<p2<p3 or p3<p2<p1:
        c+=1
print(c)
