n=int(input())
s=[c for c in input()]
q=int(input())
for _ in range(q):
    t,a,b=map(int,input().split())
    a-=1
    b-=1
    if t==1:
        tmp=s[a]
        s[a]=s[b]
        s[b]=tmp
    else:
        s=s[n:]+s[:n]
print(''.join(s))
