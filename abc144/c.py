n=int(input())
def md(n):
    l,u=[],[]
    i=1
    while i*i<=n:
        if n%i==0:
            l.append(i)
            if i!=n//i:
                u.append(n//i)
        i+=1
    return l+u[::-1]
m=md(n)
l=len(m)
l2=len(m)//2
if l%2==0:
    print(m[l2]+m[l2-1]-2)
else:
    print(2*(m[l2]-1))
