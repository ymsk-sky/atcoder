n = int(input())
ll = []
for _ in range(n):
    l = list(map(int, input().split()))
    ll.append(l)
ans = 0
for j in range(n):
    if ans - 1 < j:
        ans = ll[j][ans - 1]
    else:
        ans = ll[ans - 1][j]
print(ans)
