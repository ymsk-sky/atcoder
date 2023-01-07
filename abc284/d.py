t = int(input())
for _ in range(t):
    n = int(input())
    for i in range(2, int(-(-n ** 0.5 // 1)) + 1):
        if n%i == 0:
            break
    n //= i
    if n%i == 0:
        p = i
        q = n // i
    else:
        q = i
        p = int(n**0.5)
    print(p, q)

"""
1<=t<=10
1<=n<=9*10**18
"""
