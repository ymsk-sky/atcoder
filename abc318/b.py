n = int(input())
l = [[0] * 101 for _ in range(101)]
for _ in range(n):
    a, b, c, d = map(int, input().split())
    for i in range(a, b):
        for j in range(c, d):
            l[i][j] = 1
ans = sum([sum(x) for x in l])
print(ans)
