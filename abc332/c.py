n, m = map(int, input().split())
s = input()
for k in range(1001):
    logo = k
    muji = m
    for c in s:
        if c == "0":
            muji = m
            logo = k
        elif c == "1":
            if muji > 0:
                muji -= 1
            else:
                logo -= 1
        elif c == "2":
            logo -= 1
        if muji < 0 or logo < 0:
            break
    else:
        print(k)
        break
