n = int(input())
pl = list(map(int, input().split()))
q = int(input())
for _ in range(q):
    a, b = map(int, input().split())
    if pl.index(a) < pl.index(b):
        print(a)
    else:
        print(b)
