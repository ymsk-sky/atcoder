n, m, h, k = map(int, input().split())
s = input()
xyl = set([tuple(map(int, input().split())) for _ in range(m)])
crt = [0, 0]
for c in s:
    h -= 1
    if c == "R":
        crt[0] += 1
    elif c == "L":
        crt[0] -= 1
    elif c == "U":
        crt[1] += 1
    else:
        crt[1] -= 1
    if h < 0:
        print("No")
        exit()
    if tuple(crt) in xyl:
        if h < k:
            h = k
            xyl.remove(tuple(crt))
print("Yes")
