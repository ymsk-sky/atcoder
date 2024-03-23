from collections import defaultdict

h, w, m = map(int, input().split())
tax = [list(map(int, input().split())) for _ in range(m)]
tate = defaultdict(int)
tate_num = 0
tate_comp = set()
yoko = defaultdict(int)
yoko_num = 0
yoko_comp = set()
for t, a, x in tax[::-1]:
    if t == 1:
        if a in yoko_comp:
            continue
        yoko_comp.add(a)
        yoko[x] += w - tate_num
        yoko_num += 1
    elif t == 2:
        if a in tate_comp:
            continue
        tate_comp.add(a)
        tate[x] += h - yoko_num
        tate_num += 1
# TODO: 最初からある色0の処理
color0def = h*w - sum(yoko.values()) - sum(tate.values())
ans = defaultdict(int)
for k, v in tate.items():
    ans[k] += v
for k, v in yoko.items():
    ans[k] += v
ans[0] += color0def

num = sum([1 for v in ans.values() if v > 0])
print(num)
for k in sorted(ans.keys()):
    if ans[k] > 0:
        print(k, ans[k])
