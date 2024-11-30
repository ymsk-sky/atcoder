import sys

sys.setrecursionlimit(10**7)

n, m = map(int, input().split())

ans = []
al = []
def dfs(i: int) -> None:
    bef = al[-1]
    if i == n:
        for last in range(bef + 10, m + 1):
            ans.append(al + [last])
        return
    for a in range(bef + 10, m + 1):
        if a + 10*(n - i) > m:
            break
        al.append(a)
        dfs(i + 1)
        al.pop()

for a in range(1, m):
    al.append(a)
    dfs(2)
    al.pop()

print(len(ans))
for an in ans:
    print(*an)
