import heapq

n = int(input())
que = []
heapq.heapify(que)
d = {}
for _ in range(n):
    s, c = map(int, input().split())
    heapq.heappush(que, s)
    d[s] = c

ans = 0
while que:
    s = heapq.heappop(que)
    c = d[s]
    ans += c%2
    s *= 2
    c //=2
    if s in d:
        d[s] += c
    elif c > 1:
        heapq.heappush(que, s)
        d[s] = c
    else:
        ans += c
print(ans)
