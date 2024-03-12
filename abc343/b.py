n = int(input())
al = [list(map(int, input().split())) for _ in range(n)]
for a in al:
    print(*[i + 1 for i in range(n) if a[i]])
