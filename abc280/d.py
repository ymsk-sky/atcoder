k = int(input())

def f(n):
    arr = []
    tmp = n
    for i in range(2, int(-(-n**0.5 // 1)) + 1):
        if tmp%i == 0:
            cnt = 0
            while tmp%i == 0:
                cnt += 1
                tmp //= i
            arr.append((i, cnt))
    if tmp != 1:
        arr.append((tmp, 1))
    if arr == []:
        arr.append((n, 1))
    return arr

ans = 0
for p, a in f(k):
    # p**a: pがa個
    lim = a
    # p ~ a*p
    for nx in range(p, a*p + 1, p):
        j = nx
        while j%p == 0:
            j //= p
            lim -= 1
            if lim <= 0:
                break
        if lim <= 0:
            break
    ans = max(ans, nx)
print(ans)