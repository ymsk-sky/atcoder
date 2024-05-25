a, b = map(int, input().split())
l = [1] * 3
l[a - 1] = 0
l[b - 1] = 0
if sum(l) == 1:
    print(l.index(1) + 1)
else:
    print(-1)
