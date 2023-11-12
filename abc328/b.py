n = int(input())
dl = list(map(int, input().split()))
ans = 0
for i in range(1, n + 1):
    d = dl[i - 1]
    for j in range(1, d + 1):
        s = set(str(i) + str(j))
        if len(s) == 1:
            ans += 1
print(ans)
