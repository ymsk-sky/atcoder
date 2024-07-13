n = int(input())
lrl = []
ans = []
remain = []  # 余裕
for _ in range(n):
    l, r = map(int, input().split())
    ans.append(l)
    remain.append(r - l)
    lrl.append([l, r])
s = sum(ans)
if s > 0:
    print("No")
    exit()
s *= -1
for i in range(n):
    if s == 0:
        break
    r = remain[i]
    if s >= r:
        x = r
        s -= r
    else:
        x = s
        s = 0
    ans[i] += x
if s != 0:
    print("No")
    exit()
print("Yes")
print(*ans)
