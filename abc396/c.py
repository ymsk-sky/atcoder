n, m = map(int, input().split())
bl = list(map(int, input().split()))
wl = list(map(int, input().split()))

bl.sort(reverse=True)
wl.sort(reverse=True)

b_sums = bl[:]
for i in range(n - 1):
    b_sums[i + 1] += b_sums[i]
for i in range(n - 2, -1, -1):
    b_sums[i] = max(b_sums[i], b_sums[i + 1])

ans = max(0, max(b_sums))
w_sum = 0
for i, w in enumerate(wl):
    if i == n:
        break
    w_sum += w
    ans = max(ans, w_sum + b_sums[i])
print(ans)
