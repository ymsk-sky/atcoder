n=int(input())
def mdc(n):
    c=0
    i=1
    while i*i<=n:
        if n%i==0:
            c+=1
            if i!=n//i:
                c+=1
        i+=1
    return c
ans=0
for k in range(1,n+1):
    ans+=k*mdc(k)
print(ans)
