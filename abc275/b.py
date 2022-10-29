a, b, c, d, e, f = map(int, input().split())
mod = 998244353

ans = a * b % mod
ans *= c
ans %= mod

m = d * e % mod
m *= f
m %= mod

ans -= m
ans %= mod

print(ans)