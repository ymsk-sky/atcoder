n, k = map(int, input().split())
al = list(map(int, input().split()))
bl = sorted(set(al))
m = len(bl)
bef = -1
cnt = 0
for i in range(m):
    if cnt == k:
        break
    a = bl[i]
    if bef + 1 == a:
        cnt += 1
    else:
        break
    bef = a
print(bef + 1)
