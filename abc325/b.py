n = int(input())
wxl = [list(map(int, input().split())) for _ in range(n)]
ans = 0
for t in range(24):
    tmp = 0
    for w, x in wxl:
        if 9 <= (t + x) % 24 < 18:
            tmp += w
    ans = max(ans, tmp)
print(ans)
