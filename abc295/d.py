from collections import defaultdict

s = input()
d = defaultdict(int)
d[0] += 1
state = 0
for c in s:
    c = int(c)
    if (state >> c) & 1:
        state -= 1 << c
    else:
        state += 1 << c
    d[state] += 1
ans = 0
for k in d:
    n = d[k]
    ans += n*(n - 1)//2
print(ans)

"""
0000000000
"""
