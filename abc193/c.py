n=int(input())
s=set()
for a in range(2,int(n**(1/2))+1):
    x=a*a
    while x<=n:
        s.add(x)
        x*=a
print(n-len(s))
