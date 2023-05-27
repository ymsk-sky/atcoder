from collections import deque

n = int(input())
edges = [set() for _ in range(n)]
in_nums = [0]*n  # 次数
for _ in range(n - 1):
    u, v = map(int, input().split())
    u, v = u - 1, v - 1
    edges[u].add(v)
    edges[v].add(u)
    in_nums[u] += 1
    in_nums[v] += 1

que = deque([])
for i in range(n):
    if in_nums[i] == 1:
        que.append(i)

fin = [0]*n
ans = []
while que:
    crt = que.popleft()
    if fin[crt]:
        continue
    fin[crt] = 1
    center = list(edges[crt])[0]
    fin[center] = 1
    cnt = 1
    for nxt in edges[center]:
        if nxt == crt:
            continue
        cnt += 1
        if in_nums[nxt] == 1:
            fin[nxt] = 1
        else:
            in_nums[nxt] -= 1
            edges[nxt].remove(center)
            if in_nums[nxt] == 1:
                fin[nxt] = 1
                mxt = list(edges[nxt])[0]
                que.append(mxt)
                edges[mxt].remove(nxt)
    ans.append(cnt)

ans.sort()
print(*ans)

"""
3<=n<=2*10**5
"""
