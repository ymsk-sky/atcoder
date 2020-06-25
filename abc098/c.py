n=int(input())
s=input()
v=0
for i,c in enumerate(s):
    if c=='W':
        v+=(2**(n-i-1))
u=(2**n)-1
m=float('inf')
for i in range(n):
    v2=bin(v)[2:].zfill(n)
    u2=bin(u)[2:].zfill(n)
    v3=int(v2[:i]+v2[i+1:],2)
    u3=int(u2[:i]+u2[i+1:],2)
    m=min(m,bin(v3^u3).count('1'))
    u>>=1
print(m)
