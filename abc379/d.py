from sortedcontainers import SortedList

q = int(input())
queries = [list(map(int, input().split())) for _ in range(q)]

sl = SortedList()
th = 0
fin = 0
for query in queries:
    if query[0] == 1:
        sl.add(-th)
    elif query[0] == 2:
        t = query[1]
        th += t
    else:
        h = query[1]
        n = sl.bisect_left(h - th)
        ans = len(sl) - n - fin
        print(ans)
        fin += ans
