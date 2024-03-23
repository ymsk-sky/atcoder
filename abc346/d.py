n = int(input())
s = input()
cl = list(map(int, input().split()))
l0 = [0] * (n + 1)  # 01010...に置き換えた場合の累積和
l1 = [0] * (n + 1)  # 10101...に置き換えた場合の累積和
for i in range(n):
    if s[i] == "0":
        if i%2 == 0:
            l1[i + 1] = cl[i]
        else:
            l0[i + 1] = cl[i]
    else:
        if i%2 == 0:
            l0[i + 1] = cl[i]
        else:
            l1[i + 1] = cl[i]
for i in range(n):
    l0[i + 1] += l0[i]
    l1[i + 1] += l1[i]
ans = float("inf")
for i in range(1, n):
    cost00 = 0  # ターゲット部分を00にするコスト
    cost11 = 0  # ターゲット部分を11にするコスト
    a, b = s[i - 1], s[i]
    if a == "1":
        cost00 += cl[i - 1]
    else:
        cost11 += cl[i - 1]
    if b == "1":
        cost00 += cl[i]
    else:
        cost11 += cl[i]
    if i > 1:  # 前部分
        if i%2 == 0:
            cost00 += l1[i - 1]
            cost11 += l0[i - 1]
        else:
            cost00 += l0[i - 1]
            cost11 += l1[i - 1]
    if i < n - 1:  # 後部分
        if i%2 == 0:
            cost00 += l0[n] - l0[i + 1]
            cost11 += l1[n] - l1[i + 1]
        else:
            cost00 += l1[n] - l1[i + 1]
            cost11 += l0[n] - l0[i + 1]
    c = min(cost00, cost11)
    ans = min(ans, c)
print(ans)

"""
2<=n<=2*10**5
1<=c<=10**9

累積和
"""