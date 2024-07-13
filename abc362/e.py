mod = 998244353
n = int(input())
al = list(map(int, input().split()))
if n == 1:
    print(1)
    exit()

difs = set()
for i in range(n):
    for j in range(i + 1, n):
        difs.add(al[j] - al[i])
# dp[i][k][dif]: 末尾がi番目の長さkでdifの等差数列の個数
dp = [[{dif: 0 for dif in difs} for _ in range(n + 1)] for _ in range(n)]
for i in range(n):
    for dif in difs:
        dp[i][1][dif] += 1

for i, a in enumerate(al):
    for k in range(2, n + 1):
        for j in range(i):
            dif = a - al[j]
            dp[i][k][dif] += dp[j][k - 1][dif]
            dp[i][k][dif] %= mod
ans = [n]
for k in range(2, n + 1):
    res = 0
    for i in range(n):
        for dif in difs:
            res += dp[i][k][dif]
    ans.append(res % mod)
print(*ans)

"""DPっぽい
1<=n<=80
1<=a<=10**9
"""