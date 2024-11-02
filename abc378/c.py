n = int(input())
al = list(map(int, input().split()))
d = dict()
bl = [-1] * n
for i in range(n):
    a = al[i]
    if a in d:
        bl[i] = d[a]
    d[a] = i + 1
print(*bl)
