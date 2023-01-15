import sys
sys.setrecursionlimit(10**7)

n = int(input())
sl = set()
dl = dict()
l = []
for i in range(n):
    s, t = input().split()
    sl.add(s)
    dl[s] = i
    l.append((s, t))

fin = [0] * n

def dfs(i):
    fin[i] = 1
    s, t = l[i]
    if t in sl:
        j = dl[t]
        if fin[j]:
            print("No")
            exit()
        dfs(j)
    sl.discard(s)
    sl.add(t)
    dl[t] = i

for i in range(n):
    if fin[i]:
        continue
    dfs(i)

print("Yes")

"""
1<=n<=10**5
1<=|s|,|t|<=8
"""
