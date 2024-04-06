n = int(input())
d = dict()
for _ in range(n):
    a, c = map(int, input().split())
    if c in d:
        d[c] = min(d[c], a)
    else:
        d[c] = a
print(max(d.values()))
