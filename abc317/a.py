n, h, x = map(int, input().split())
pl = list(map(int, input().split()))
ans = n
for i in range(n - 1, -1, -1):
    p = pl[i]
    if h + p >= x:
        ans = i + 1
print(ans)
