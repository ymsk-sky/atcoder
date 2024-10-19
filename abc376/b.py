n, q = map(int, input().split())
ans = 0
pos_l = 0
pos_r = 1
for _ in range(q):
    h, t = input().split()
    t = int(t) - 1
    if h == "L":
        ok = False
        cnt = 0
        for x in range(n):
            if (pos_l + x) % n == pos_r:
                break
            if (pos_l + x) % n == t:
                ok = True
                cnt = x
                break
        if not ok:
            for x in range(n):
                if (pos_l - x) % n == t:
                    cnt = x
                    break
        ans += cnt
        pos_l = t
    elif h == "R":
        ok = False
        cnt = 0
        for x in range(n):
            if (pos_r + x) % n == pos_l:
                break
            if (pos_r + x) % n == t:
                ok = True
                cnt = x
                break
        if not ok:
            for x in range(n):
                if (pos_r - x) % n == t:
                    cnt = x
                    break
        ans += cnt
        pos_r = t
print(ans)
