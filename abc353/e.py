import sys
from collections import defaultdict
sys.setrecursionlimit(10**7)

n = int(input())
sl = list(input().split())
d = defaultdict(list)
for s in sl:
    d[s[0]].append(s)
ans = 0
def dfs(d, i):
    global ans
    for k in d:
        l = len(d[k])
        ans += l * (l - 1) // 2
        d2 = defaultdict(list)
        for s in d[k]:
            if len(s) < i + 1:
                continue
            d2[s[i]].append(s)
        if len(d2) > 0:
            dfs(d2, i + 1)
dfs(d, 1)
print(ans)

"""
2<=n<=3*10**5
1<=|s|
sum(|s|) <= 3*10**5

11
ab bb aaa bba baba babb aaaba aabbb a a b

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