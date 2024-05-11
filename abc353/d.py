n = int(input())
al = list(map(int, input().split()))
mod = 998244353
kl = [10**len(str(a)) for a in al]
s = sum(kl) % mod
ans = 0
for i, a in enumerate(al):
    ans += a * i % mod
    s -= kl[i]
    ans += a * s % mod
print(ans % mod)
