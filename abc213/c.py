h,w,n=map(int,input().split())
al=[]
bl=[]
for _ in range(n):
    a,b=map(int,input().split())
    al.append(a)
    bl.append(b)
sa={a:i for i,a in enumerate(sorted(list(set(al))),start=1)}
sb={b:j for j,b in enumerate(sorted(list(set(bl))),start=1)}
ans_a=[]
ans_b=[]
for a in al:
    ans_a.append(sa[a])
for b in bl:
    ans_b.append(sb[b])
for a,b in zip(ans_a,ans_b):
    print(a,b)
