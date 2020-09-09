n=int(input())
x=''
y=0
a=0
for _ in range(n):
    s,p=map(str,input().split())
    p=int(p)
    a+=p
    if y<p:
        x=s
        y=p
print(x if y>a/2 else 'atcoder')
