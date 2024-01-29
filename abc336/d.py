n = int(input())
al = list(map(int, input().split()))

l = [1] * n
r = [1] * n
k = 1
for i in range(n):
    if al[i] >= k:
        l[i] = k
        k += 1
    else:
        l[i] = al[i]
        k = al[i] + 1
k = 1
for i in range(n - 1, -1, -1):
    if al[i] >= k:
        r[i] = k
        k += 1
    else:
        r[i] = al[i]
        k = al[i] + 1
ans = max([min(a, b) for a, b in zip(l, r)])
print(ans)
