import heapq

INF = float("inf")

t = int(input())
ans = []
for _ in range(t):
    n, k = map(int, input().split())
    al = list(map(int, input().split()))
    bl = list(map(int, input().split()))
    l = [(a, b) for a, b in zip(al, bl)]
    l.sort()  # aの順にソート
    al = [a for a, _ in l]
    bl = [b for _, b in l]
    s = 0
    que = []
    out = []
    for i in range(k):
        b = bl[i]
        s += b
        heapq.heappush(que, -b)
    res = s * al[k - 1]
    for i in range(k, n):
        a, b = al[i], bl[i]
        # 最大のものを1つ抜く
        _b = -heapq.heappop(que)
        s -= _b
        # 外に出しておく
        heapq.heappush(out, _b)
        # 今回のものを追加
        s += b
        # 値を比較
        tmp = a * s
        res = min(res, tmp)
        # 次に備える
        s -= b
        heapq.heappush(out, b)
        _b = heapq.heappop(out)
        s += _b
        heapq.heappush(que, -_b)
    ans.append(res)
print(*ans, sep="\n")
