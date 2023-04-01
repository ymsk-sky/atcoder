n, m = map(int, input().split())
if n**2 < m:
    print(-1)
    exit()

def f(n):
    l, u = [], []
    i = 1
    while i*i <= n:
        if n%i == 0:
            l.append(i)
            if i != n//i:
                u.append(n//i)
        i += 1
    return l + u[::-1]

left = m
right = n**2
while right - left > 1:
    x = (left + right)//2
    l = f(x)
    if l[len(l)//2] <= n:
        right = x
    else:
        left = x
print(left)


"""
1<=n<=10**12
1<=m<=10**12
"""

"""
def f(n):
    lower_divisors , upper_divisors = [], []
    i = 1
    while i*i <= n:
        if n % i == 0:
            lower_divisors.append(i)
            if i != n//i:
                upper_divisors.append(n//i)
        i += 1
    return lower_divisors + upper_divisors[::-1]
"""
