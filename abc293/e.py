a, x, m = map(int, input().split())

# a**n % mod を計算 O(log(n))
def modpow(a, n, mod):
    res = 1
    while n > 0:
        if n & 1:
            res = res * a % mod
        a = a * a % mod
        n >>= 1
    return res

# modを法とした逆元
def inv(n, mod):
    return pow(n, mod - 2, mod)

print((modpow(a, x, m) - 1)*inv(a - 1, m)%m)

"""
1<=a,m<=10*9
1<=x<=10**12

x-1
 Σ a**i = (a**x - 1)/(a - 1)
i=0
"""
