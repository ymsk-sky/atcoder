n = int(input())
hl = list(map(int, input().split()))

# 自身より右側にある最寄りの自身より大きい値のインデックス
nxt = [-1] * n
stack = []
for i in range(n - 1, -1, -1):
    h = hl[i]
    while stack and hl[stack[-1]] < h:
        stack.pop()
    if stack:
        nxt[i] = stack[-1]
    stack.append(i)

# 連鎖カウント
cnt = [0] * n
for i in range(n - 2, -1, -1):
    if nxt[i] == -1:
        continue
    cnt[i] += cnt[nxt[i]] + 1

ans = [c + 1 for c in cnt[1:]] + [0]
print(*ans)


"""
5
2 1 4 3 5

3 2 2 1 0
"""