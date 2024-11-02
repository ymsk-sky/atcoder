n = int(input())
qrl = [list(map(int, input().split())) for _ in range(n)]
q = int(input())
tdl = [list(map(int, input().split())) for _ in range(q)]
for t, d in tdl:
    q, r = qrl[t - 1]
    m = d % q
    if m == r:
        print(d)
    elif m < r:
        print(d + (r - m))
    else:
        print(d + (q - m) + r)
