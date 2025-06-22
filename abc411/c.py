n, q = map(int, input().split())
al = list(map(int, input().split()))

if n == 1:
    for i in range(q):
        print(1 if i % 2 == 0 else 0)
    exit()

l = [0] * n
ans = 0
for a in al:
    if l[a - 1] == 0:
        if a == 1:
            if l[a] == 0:
                ans += 1
        elif a == n:
            if l[a - 2] == 0:
                ans += 1
        else:
            if l[a - 2] == l[a] == 0:
                ans += 1
            elif l[a - 2] == l[a] == 1:
                ans -= 1
    else:
        if a == 1:
            if l[a] == 0:
                ans -= 1
        elif a == n:
            if l[a - 2] == 0:
                ans -= 1
        else:
            if l[a - 2] == l[a] == 0:
                ans -= 1
            elif l[a - 2] == l[a] == 1:
                ans += 1
    l[a - 1] = 1 - l[a - 1]
    print(ans)
