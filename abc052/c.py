n=int(input())
d={i:0 for i in range(2,n+1)}
def prime_factorize(n):
    a = []
    while n % 2 == 0:
        a.append(2)
        n //= 2
    f = 3
    while f * f <= n:
        if n % f == 0:
            a.append(f)
            n //= f
        else:
            f += 2
    if n != 1:
        a.append(n)
    return a
for i in range(2,n+1):
    for j in prime_factorize(i):
        d[j]+=1
a=1
for v in d.values():
    a=a*(v+1)
print(a%(10**9+7))
"""
x = p^n * q^m * ...
-> ans is (n+1)*(m+1)*...

N! = N * N-1 * N-2 * ... * 1
6! = 6 * 5 * 4 * 3 * 2 * 1
   = 2*3*5*2*2*3*2
   = 2^4 * 3^2 * 5^1
   -> (4+1)(2+1)(1+1) = 5*3*2=30
"""
