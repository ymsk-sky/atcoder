n = int(input())
cards = [list(map(int, input().split())) for _ in range(n)]

# dp[i]: カードの残りがbin(j)の状態
dp = [-1] * ((1 << n) + 1)
dp[0] = 0  # 負け

for i in range(1, (1 << n) + 1):
    if bin(i).count("1") < 2:
        dp[i] = 0  # 負け
        continue
    l = []
    for j in range(n):
        if (i >> j) & 1:
            l.append((cards[j], j))
    flag = False
    for j in range(len(l)):
        a = l[j]
        for k in range(j + 1, len(l)):
            b = l[k]
            if a[0][0] == b[0][0] or a[0][1] == b[0][1]:
                state = i - (1 << a[1]) - (1 << b[1])
                if dp[state] == 0:
                    flag = True
    dp[i] = int(flag)
if dp[(1 << n) - 1]:
    print("Takahashi")
else:
    print("Aoki")

print(dp)

"""
1<=n<=18

1回の行動で2枚除外するので, 最大でも9回(10回目で終了)のゲーム.

"""