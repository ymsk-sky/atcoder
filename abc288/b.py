n, k = map(int, input().split())
ans = []
for i in range(1, n + 1):
    s = input()
    if i <= k:
        ans.append(s)
ans.sort()
print(*ans, sep="\n")