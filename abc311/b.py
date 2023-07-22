n, d = map(int, input().split())
sl = [input() for _ in range(n)]
ans = 0
for i in range(d):
    for j in range(i + 1, d + 1):
        cnt = 0
        for s in sl:
            if not ("x" in s[i:j]):
                cnt += 1
            else:
                break
        if cnt == n:
            ans = max(ans, j - i)
print(ans)
