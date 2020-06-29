a,b,c=map(int,input().split())
k=int(input())
for _ in range(k):
    m=max(a,b,c)
    if m==a:
        a*=2
    elif m==b:
        b*=2
    else:
        c*=2
print(sum([a,b,c]))
