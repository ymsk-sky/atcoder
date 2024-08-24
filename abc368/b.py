import heapq

n = int(input())
al = list(map(int, input().split()))

que = [-a for a in al]
heapq.heapify(que)
ans = 0
while que:
    a1 = heapq.heappop(que)
    a2 = heapq.heappop(que)
    if a2 == 0:
        break
    a1 += 1
    a2 += 1
    heapq.heappush(que, a1)
    heapq.heappush(que, a2)
    ans += 1
print(ans)
