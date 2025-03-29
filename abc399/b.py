n = int(input())
pl = list(map(int, input().split()))

l = sorted([(p, i) for i, p in enumerate(pl)], reverse=True)
ans = [0] * n
r = 0
k = -1
for j, (p, i) in enumerate(l, start=1):
    if p != k:
        r = j
        k = p
    ans[i] = r

print(*ans, sep="\n")
