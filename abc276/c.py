n = int(input())
pl = list(map(int, input().split()))

r = [0] * (n + 1)
r[0] = r[1] = 1
for i in range(2, n + 1):
    r[i] = r[i - 1] * i

k = 0
used = [0] * (n + 1)
for i in range(1, n + 1):
    p = pl[i - 1]
    k += r[n - i] * (p - sum(used[:p]) - 1)
    used[p] = 1
k = 2020
ans = []
used = [0] * (n + 2)
s = 0
for i in range(n):
    num = 0
    while s + r[n - i - 1] <= k:
        s += r[n - i - 1]
        num += 1
    # 前にnum個ある
    tmp = 1
    cnt = 0
    while cnt < num:
        if used[tmp] == 0:
            cnt += 1
        tmp += 1
    ans.append(tmp)
    used[tmp] = 1
print(*ans)

"""
7
3 6 1 7 5 4 2

used = [0, 0, 0, 1, 0, 0, 1, 0, 0]
2020
720+720=1440
s=1920
"""