n,a,b=map(int,input().split())
c=0
for i in range(1,n+1):
    s=sum([int(v) for v in str(i)])
    if a<=s<=b:
        c+=i
print(c)
