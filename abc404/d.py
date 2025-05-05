from itertools import product

n, m = map(int, input().split())
cl = list(map(int, input().split()))
al_l = []
for _ in range(m):
    _, *al = list(map(int, input().split()))
    al_l.append(al)

ans = 1 << 60
for pl in product(range(3), repeat=n):
    nums = [0] * m
    tmp = sum([c * p for c, p in zip(cl, pl)])
    for i, al in enumerate(al_l):
        for a in al:
            nums[i] += pl[a - 1]
    ok = True
    for x in nums:
        if x < 2:
            ok = False
            break
    if ok:
        ans = min(ans, tmp)
print(ans)
