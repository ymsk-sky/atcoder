n=int(input())
s=[c for c in input()]
q=int(input())
f=1
for _ in range(q):
    t,a,b=map(int,input().split())
    a-=1
    b-=1
    if t==1:
        if f==-1:
            if a<n:
                a+=n
            else:
                a-=n
            if b<n:
                b+=n
            else:
                b-=n
        tmp=s[a]
        s[a]=s[b]
        s[b]=tmp
    else:
        f*=-1
        #s=s[n:]+s[:n]
print(''.join(s) if f==1 else ''.join(s[n:]+s[:n]))
