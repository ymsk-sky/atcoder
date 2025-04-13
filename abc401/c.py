M = 10**9

n, k = map(int, input().split())

l = [1] * k
s = k
for i in range(k, n + 1):
    l.append(s)
    s -= l[i - k]
    s += l[-1]
    s %= M
ans = l[n]
print(ans)
