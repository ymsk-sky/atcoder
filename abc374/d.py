from itertools import permutations

n, s, t = map(int, input().split())
l = [list(map(int, input().split())) for _ in range(n)]

# 線の描画時間
base = sum([((a - c)**2 + (b - d)**2)**0.5 for a, b, c, d in l])
base /= t

# 移動時間
ans = float("inf")
for per in permutations(range(n)):
    for state in range(1 << n):
        tmp = 0
        p, q = 0, 0
        for i in range(n):
            if (state >> i) & 1:
                a, b, c, d = l[per[i]]
            else:
                c, d, a, b = l[per[i]]
            tmp += ((p - a)**2 + (q - b)**2)**0.5
            p, q = c, d
        ans = min(ans, tmp)
ans /= s
print(ans + base)
