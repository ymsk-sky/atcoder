n = int(input())
al = list(map(int, input().split()))
d = dict()
for i in range(n):
    a = al[i]
    if a in d:
        d[a].append(i)
    else:
        d[a] = [i]
ans = 0
for k in d:
    l = d[k]
    m = len(l)
    for i in range(m - 1):
        a, b = l[i], l[i + 1]
        if b - a > 1:
            ans += (b - a - 1) * (i + 1) * (m - i - 1)
print(ans)

"""
3<=n<=3*10**5
1<=a<=n

(i,j,k)
    1 <= i < j < k <= n
    ai == ak
    ai != aj <=> ak != aj

7: [1, 3] ->2 = 1個
11: [2, 8, 9, 10] = 5個*1*3
13: [7, 12] = 4
"""
