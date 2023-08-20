m = int(input())
dl = list(map(int, input().split()))
l = []
for i in range(m):
    l.extend([(i + 1, j) for j in range(1, dl[i] + 1)])

print(*l[len(l)//2])
