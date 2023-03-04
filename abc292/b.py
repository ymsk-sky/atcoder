n, q = map(int, input().split())
l = [0] * n
for _ in range(q):
    e = list(map(int, input().split()))
    if e[0] == 1:
        l[e[1] - 1] += 1
    elif e[0] == 2:
        l[e[1] - 1] += 2
    else:
        if l[e[1] - 1] >= 2:
            print("Yes")
        else:
            print("No")
