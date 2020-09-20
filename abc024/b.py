n,t=map(int,input().split())
s=n*t
p=0
for _ in range(n):
    a=int(input())
    if p>a:
        s-=p-a
    p=a+t
print(s)
