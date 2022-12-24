n = int(input())
al = list(map(int, input().split()))
q = int(input())
for _ in range(q):
    query = list(map(int, input().split()))
    if query[0] == 1:
        _, k, x = query
        al[k - 1] = x
    else:
        _, k = query
        print(al[k - 1])
