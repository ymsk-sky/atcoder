n=int(input())
k=int(input())
xs=list(map(int,input().split()))
a=0
for x in xs:
    a+=2*min(x,k-x)
print(a)
