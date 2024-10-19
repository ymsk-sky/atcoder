n, c = map(int, input().split())
tl = list(map(int, input().split()))
ans = 1
bef = tl[0]
for t in tl[1:]:
    if bef + c <= t:
        ans += 1
        bef = t
print(ans)
