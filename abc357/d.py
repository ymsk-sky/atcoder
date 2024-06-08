n = input()
m = len(n)
v = int(n)
mod = 998244353

a = v  # 初項
r = pow(10, m, mod)  # 公比 ok
x = v  #項数

def inv(val):
    return pow(val, mod - 2, mod)

# s = a * (pow(r, x, mod) - 1) // (r - 1) % mod
s = a * (pow(r, x, mod) - 1) * inv(r - 1)
ans = s % mod
print(ans)

"""
1<=n<=10**18

10
154579416

12
214985338
"""
