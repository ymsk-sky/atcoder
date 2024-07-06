from collections import defaultdict

n = int(input())
al = list(map(int, input().split()))
wl = list(map(int, input().split()))

boxes = defaultdict(list)
for a, w in zip(al, wl):
    boxes[a].append(w)

ans = 0
for l in boxes.values():
    m = len(l)
    for i, a in enumerate(sorted(l)):
        if i == m - 1:
            break
        ans += a
print(ans)
