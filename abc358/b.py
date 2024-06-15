n, a = map(int, input().split())
tl = list(map(int, input().split()))
crt = 0
for t in tl:
    if crt < t:
        crt = t + a
    else:
        crt += a
    print(crt)
