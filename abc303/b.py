n, m = map(int, input().split())
l = [[0]*n for _ in range(n)]
for _ in range(m):
    al = list(map(int, input().split()))
    for a, b in zip(al, al[1:]):
        l[a - 1][b - 1] = 1
        l[b - 1][a - 1] = 1

ans = -n
for i in range(n):
    ans += l[i].count(0)

print(ans//2)
