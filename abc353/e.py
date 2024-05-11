n = int(input())
sl = list(input().split())
d = [dict(), dict()]
for s in sl:
    k = ord(s[0]) - 96
    if k in d[0]:
        d[0][k].append(s)
    else:
        d[0][k] = [s]
i = 0
ans = 0
while len(d[0]) > 0 or len(d[1]) > 0:
    for k in d[i % 2].keys():
        lk = len(d[i % 2][k])
        ans += lk * (lk - 1) // 2
    i += 1
    for k in d[(i + 1) % 2].keys():
        for v in d[(i + 1) % 2][k]:
            if len(v) < i + 1:
                continue
            # k2 = "".join([k, v[i]])
            k2 = k*100 + (ord(v[i]) - 96)
            if k2 in d[i % 2]:
                d[i % 2][k2].append(v)
            else:
                d[i % 2][k2] = [v]
    d[(i + 1) % 2] = dict()
print(ans)


"""
2<=n<=3*10**5
1<=|s|
sum(|s|) <= 3*10**5

11
a
a
aaa
aaaba
aabbb
ab

b
baba
babb
bb
bba
"""