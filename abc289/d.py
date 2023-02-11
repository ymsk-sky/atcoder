n = int(input())
al = list(map(int, input().split()))
m = int(input())
bl = list(map(int, input().split()))
x = int(input())
M = 10**5
dp = [0] * (M + 1)
for b in bl:
    dp[b] = -1
dp[0] = 1
for i in range(M + 1):
    if dp[i] != 1:
        continue
    for a in al:
        # j=次の段目
        j = i + a
        if j > M:
            continue
        if dp[j] == -1:
            continue
        dp[j] = 1
print("Yes" if dp[x] == 1 else "No")
