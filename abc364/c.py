n, x, y = map(int, input().split())
al = list(map(int, input().split()))
bl = list(map(int, input().split()))
al.sort(reverse=True)
bl.sort(reverse=True)
ans = n
a_s = 0
for i, a in enumerate(al, start=1):
    a_s += a
    if a_s > x:
        break
ans = min(ans, i)
b_s = 0
for i, b in enumerate(bl, start=1):
    b_s += b
    if b_s > y:
        break
ans = min(ans, i)
print(ans)
