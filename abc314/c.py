from collections import deque

n, m = map(int, input().split())
s = input()
cl = list(map(int, input().split()))

ql = [deque() for _ in range(m)]
for i in range(n):
    ch = s[i]
    co = cl[i]
    ql[co - 1].append(ch)

for i in range(m):
    ql[i].rotate()

ans = []
for co in cl:
    ch = ql[co - 1].popleft()
    ans.append(ch)

print(*ans, sep="")
