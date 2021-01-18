import heapq
n,m=map(int,input().split())
l=[-a for a in list(map(int,input().split()))]
heapq.heapify(l)
for _ in range(m):
    max_=heapq.heappop(l)
    heapq.heappush(l,-(-max_//2))
print(-sum(l))
