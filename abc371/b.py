n, m = map(int, input().split())
abl = [input().split() for _ in range(m)]

l = [False] * n
for a, b in abl:
    if b == "F":
        print("No")
    else:
        a = int(a) - 1
        if l[a]:
            print("No")
        else:
            l[a] = True
            print("Yes")
