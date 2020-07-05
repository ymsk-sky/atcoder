h,w,k=map(int,input().split())
l=[input()for _ in range(h)]
def t(m,h,w):
    n=[]
    for i in range(w):
        s=''
        for j in range(h):
            s+=m[j][i]
        n.append(s)
    return n
ans=0
for i in range(2**h):
    m=l.copy()
    b=bin(i)[2:].zfill(h)
    for n,i_ in enumerate(b):
        if i_=='1':
            m[n]='x'*w
    m=t(m,h,w)
    for j in range(2**w):
        x=m.copy()
        b=bin(j)[2:].zfill(w)
        for n,j_ in enumerate(b):
            if j_=='1':
                x[n]='x'*h
        c=0
        for r in x:
            c+=r.count('#')
        if c==k:
            ans+=1
print(ans)
