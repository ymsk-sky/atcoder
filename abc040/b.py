n=int(input())
a=float('inf')
for i in range(1,10**5+1):
    j=n//i
    m=(n-i*j)+abs(i-j)
    a=min(a,m)
print(a)
