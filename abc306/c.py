n = int(input())
al = list(map(int, input().split()))
l = [[-1, i] for i in range(1, n + 1)]
for i in range(3*n):
    a = al[i]
    if l[a - 1][0] == -1:
        l[a - 1][0] += 1
    elif l[a - 1][0] == 0:
        l[a - 1][0] = i + 1
l.sort()
print(*[r[1] for r in l])
