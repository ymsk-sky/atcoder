n, k = map(int, input().split())
abl = [list(map(int, input().split())) for _ in range(n)]
abl.sort()
s = sum([b for _, b in abl])
if s <= k:
    print(1)
    exit()

for a, b in abl:
    s -= b
    if s <= k:
        print(a + 1)
        break
