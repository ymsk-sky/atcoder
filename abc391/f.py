import heapq

N, K = map(int, input().split())
al = list(map(int, input().split()))
bl = list(map(int, input().split()))
cl = list(map(int, input().split()))

al.sort(reverse=True)
bl.sort(reverse=True)
cl.sort(reverse=True)

def val(i: int, j: int, k: int) -> int:
    a = al[i]
    b = bl[j]
    c = cl[k]
    return a*b + b*c + c*a

fin = set([(0, 0, 0)])
que = [(-val(0, 0, 0), 0)]
for idx in range(K):
    res, x = heapq.heappop(que)
    if idx == K - 1:
        print(-res)
        break
    i, j, k = x // N**2, (x % N**2) // N, (x % N**2) % N
    for p, q, r in ((1, 0, 0), (0, 1, 0), (0, 0, 1)):
        u, v, w = i + p, j + q, k + r
        if u >= N or v >= N or w >= N:
            continue
        if (u, v, w) in fin:
            continue
        fin.add((u, v, w))
        heapq.heappush(que, (-val(u, v, w), u*N**2 + v*N + w))
