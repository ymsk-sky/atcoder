n = int(input())
kl = list(map(int, input().split()))

ans = float("inf")
for state in range(1 << n):
    a = 0
    b = 0
    for i, k in enumerate(kl):
        if (state >> i) & 1:
            a += k
        else:
            b += k
    tmp = max(a, b)
    ans = min(ans, tmp)
print(ans)
