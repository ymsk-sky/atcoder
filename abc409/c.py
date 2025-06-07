n, l = map(int, input().split())
dl = list(map(int, input().split()))

if l % 3 > 0:
    print(0)
    exit()

pl = [0] * l
crt = 0
pl[crt] += 1
for d in dl:
    crt += d
    crt %= l
    pl[crt] += 1

m = l // 3
ans = 0
for i in range(m):
    ans += pl[i] * pl[i + m] * pl[i + 2*m]
print(ans)
