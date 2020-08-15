n,k=map(int,input().split())
ps=list(map(int,input().split()))
cs=list(map(int,input().split()))
m=0#max(ans)
md={}
for p in ps:
    q=p-1
    d={}
    s=0#score
    for _ in range(n):
        if q in d:
            break
        else:
            s+=cs[q]
            d[q]=s
        q=ps[q]-1
    tm=max(list(d.values())[:k])
    if tm>m:
        m=tm
        md=d
print(m)
