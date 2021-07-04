p=int(input())
ans=0
def b(n):
    if n==1: return 1
    return n*b(n-1)
for i in range(10,0,-1):
    c=b(i)
    cnt=p//c
    if cnt<=100:
        ans+=cnt
        p%=c
    else:
        ans+=100
        p%=(c*100)
print(ans)
