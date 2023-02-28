from collections import deque

n, m = map(int, input().split())
edges = [[] for _ in range(n)]
in_nums = [0] * n
for _ in range(m):
    x, y = map(int, input().split())
    x, y = x - 1, y - 1
    edges[y].append(x)
    in_nums[x] += 1

que = deque()
tmp = 0
for i in range(n):
    if in_nums[i] == 0:
        que.append(i)
        tmp += 1

if tmp != 1:
    print("No")
    exit()

ans = [0] * n
num = n
while 1:
    crt = que.popleft()
    tmp -= 1

    ans[crt] = num
    num -= 1
    if num == 0:
        break

    for nxt in edges[crt]:
        in_nums[nxt] -= 1
        if in_nums[nxt] == 0:
            que.append(nxt)
            tmp += 1
    
    if tmp != 1:
        print("No")
        exit()

print("Yes")
print(*ans)
