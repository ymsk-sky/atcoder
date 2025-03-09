q = int(input())
queries = [list(map(int, input().split())) for _ in range(q)]

deck = [0] * 100

for query in queries:
    if query[0] == 1:
        x = query[1]
        deck.append(x)
    else:
        ans = deck.pop()
        print(ans)
