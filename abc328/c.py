n, q = map(int, input().split())
s = input()
x = [0] * (n + 1)  # x[i]: sのi文字目が一つ前と同じか
for i in range(1, n):
    if s[i - 1] == s[i]:
        x[i + 1] = 1
    x[i + 1] += x[i]
ans = []
for _ in range(q):
    l, r = map(int, input().split())
    cnt = x[r] - x[l]
    ans.append(cnt)
print(*ans, sep="\n")
