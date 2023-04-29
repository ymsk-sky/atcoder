from bisect import bisect_left

n = int(input())

# 素数リスト作成
m = int(n**0.5) + 1
l = [1] * (m + 1)
l[0] = l[1] = 0
for i in range(2, m + 1):
    if l[i] == 0:
        continue
    for j in range(i*2, m + 1, i):
        l[j] = 0
l = [i for i in range(m + 1) if l[i]]
l2 = [v**2 for v in l]
m = len(l)

ans = 0
for j in range(1, m - 1):
    b = l[j]
    for k in range(j + 1, m):
        c = l2[k]
        if b*c > n:
            break
        lim = int(n/b/c)
        i = min(bisect_left(l2, lim), j - 1)
        tmp = [i - 1, i, i + 1]
        for x in tmp:
            a = l2[x]
            if b*c*a <= n:
                i = x
        i = min(i, j - 1)
        ans += i + 1 if c*b*l2[i] <= n else 0
print(ans)
