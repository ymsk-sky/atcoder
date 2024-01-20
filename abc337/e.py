n = int(input())
m = 1
while 1:
    if 2**m >= n:
        break
    m += 1
print(m)
kl = [0] * m
al = [[] for _ in range(m)]
for cnt, i in enumerate(range(1 << m), start=1):
    for x in range(m):
        if (i >> x)&1:
            kl[x] += 1
            al[x].append(cnt)
    if cnt == n:
        break
for k, a in zip(kl, al):
    print(k, *a)
s = input()  # |s| = m
x = 1
for i in range(m):
    if s[i] == "1":
        x += 1 << i
print(x)


"""
2<=n<=100
"""
