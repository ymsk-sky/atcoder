from bisect import bisect_right

n, m = map(int, input().split())
al = list(map(int, input().split()))
bl = list(map(int, input().split()))

mi = float("inf")
d = {}
l = []
for i, a in enumerate(al, start=1):
    if a < mi:
        d[a] = i
        l.append(a)
        mi = a

l.sort()
for b in bl:
    i = bisect_right(l, b) - 1
    if i < 0:
        ans = -1
    else:
        ans = d[l[i]]
    print(ans)
