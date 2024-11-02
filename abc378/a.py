al = list(map(int, input().split()))
l = [0] * 4
for a in al:
    l[a - 1] += 1
ans = 0
for x in l:
    if x >= 2:
        ans += x // 2
print(ans)
