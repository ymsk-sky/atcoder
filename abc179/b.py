n=int(input())
m=0
c=0
for _ in range(n):
    a,b=map(int,input().split())
    if a==b:
        c+=1
    else:
        c=0
    m=max(m,c)
if m<3:
    print('No')
else:
    print('Yes')
