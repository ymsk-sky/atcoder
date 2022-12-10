n, t = map(int, input().split())
al = list(map(int, input().split()))
s = sum(al)

t %= s
l = [0]
for a in al:
    l.append(l[-1] + a)

for i in range(1, n + 1):
    if l[i] - t > 0:
        print(i, t - l[i - 1])
        exit()