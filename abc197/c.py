n = int(input())
al = list(map(int, input().split()))

ans = float("inf")
for l in range(1 << (n - 1)):
    vl = []
    v = al[0]
    for i in range(n - 1):
        if (l >> i) & 1:
            vl.append(v)
            v = al[i + 1]
        else:
            v |= al[i + 1]
    vl.append(v)
    tmp = vl[0]
    for i in range(1, len(vl)):
        tmp ^= vl[i]
    ans = min(ans, tmp)

print(ans)