n=int(input())
t,a=map(int,input().split())
hs=list(map(int,input().split()))
n=0
m=float('inf')
for i,h in enumerate(hs, start=1):
    x=abs(a-(t-h*0.006))
    if m>x:
        m=x
        n=i
print(n)
