from collections import deque

n, a, b = map(int, input().split())
s = input()
que = deque(s)

def check(t):
    res = 0
    for i in range(n//2):
        if que[i] != que[n - 1 - i]:
            res += b
    return res

ans = check(que)

for i in range(1, n//2 + 1):
    c = que.popleft()
    que.append(c)
    tmp = a*i + check(que)
    ans = min(ans, tmp)

print(ans)
