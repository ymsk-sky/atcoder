n, d = map(int, input().split())
tl = list(map(int, input().split()))
ans = -1
for t1, t2 in zip(tl, tl[1:]):
    if t2 - t1 <= d:
        ans = t2
        break
print(ans)
