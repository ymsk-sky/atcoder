import heapq

n, a, b, c = map(int, input().split())
dl = [list(map(int, input().split())) for _ in range(n)]
INF = float("inf")

dist_car = [INF] * n
que = [(0, 0)]
heapq.heapify(que)
while que:
    cost, crt = heapq.heappop(que)
    if dist_car[crt] <= cost:
        continue
    dist_car[crt] = cost
    for nxt in range(n):
        if crt == nxt:
            continue
        nxt_cost = dl[crt][nxt] * a
        if dist_car[nxt] <= cost + nxt_cost:
            continue
        heapq.heappush(que, (cost + nxt_cost, nxt))

dist_train = [INF] * n
que = [(0, n - 1)]
heapq.heapify(que)
while que:
    cost, crt = heapq.heappop(que)
    if dist_train[crt] <= cost:
        continue
    dist_train[crt] = cost
    for nxt in range(n):
        if crt == nxt:
            continue
        nxt_cost = dl[crt][nxt] * b + c
        if dist_train[nxt] <= cost + nxt_cost:
            continue
        heapq.heappush(que, (cost + nxt_cost, nxt))

ans = min([x + y for x, y in zip(dist_car, dist_train)])
print(ans)

"""
2<=n<=1000
1<=a,b,c<=10**6
d<=10**6
"""
