n, m = map(int, input().split())
xl = list(map(int, input().split()))
al = list(map(int, input().split()))

if sum(al) != n:
    print(-1)
    exit()

l = [[x, a] for x, a in zip(xl, al)]
l.sort()
l.append([n + 1, 0])

if l[0][0] != 1:
    print(-1)
    exit()

ans = 0
for i in range(m):
    x, a = l[i]
    x_nxt, _ = l[i + 1]
    # 不足か
    width = x_nxt - x
    if width > a:
        print(-1)
        exit()
    # 敷き詰める
    ans += width * (width - 1) // 2
    a -= width
    # 余りを次に回す
    l[i + 1][1] += a
    ans += a * width
if l[-1][1] > 0:
    print(-1)
    exit()
print(ans)
