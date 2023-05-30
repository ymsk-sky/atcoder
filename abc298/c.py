n = int(input())
q = int(input())
cards = [set() for _ in range(2*10**5 + 1)]
boxes = [[] for _ in range(n + 1)]
ql = [list(map(int, input().split())) for _ in range(q)]
for query in ql:
    if query[0] == 1:
        i, j = query[1:]
        cards[i].add(j)
        boxes[j].append(i)
    elif query[0] == 2:
        i = query[1]
        print(*sorted(boxes[i]))
    else:
        i = query[1]
        print(*sorted(cards[i]))
