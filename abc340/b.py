l = []
q = int(input())
for _ in range(q):
    n, x = map(int, input().split())
    if n == 1:
        l.append(x)
    else:
        print(l[::-1][x - 1])
