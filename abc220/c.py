n=int(input())
al=list(map(int,input().split()))
x=int(input())
s=sum(al)
m=x%s
ans=x//s*n
for i,a in enumerate(al,start=1):
    m-=a
    if m<0:
        break
print(ans+i)
