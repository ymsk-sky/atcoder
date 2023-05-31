from collections import deque

q = int(input())
ql = [list(map(int, input().split())) for _ in range(q)]
mod = 998244353
s = 1  # 数字
que = deque([1])  # 各桁の数値を管理
for query in ql:
    if query[0] == 1:
        x = query[1]
        s *= 10
        s += x
        s %= mod
        que.append(x)
    elif query[0] == 2:
        x = que.popleft()
        s -= x * pow(10, len(que), mod)
        s %= mod
    else:
        print(s)
