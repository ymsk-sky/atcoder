n = int(input())
al = list(map(int, input().split()))

l = []  # 偶数
m = []  # 奇数
for a in al:
    if a % 2 == 0:
        l.append(a)
    else:
        m.append(a)

# 偶数 = 偶数+偶数, 奇数+奇数

ans = -1
if len(l) > 1:
    l.sort()
    ans = max(ans, l[-1] + l[-2])
if len(m) > 1:
    m.sort()
    ans = max(ans, m[-1] + m[-2])
print(ans)