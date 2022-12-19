n = int(input())

def factorization(n):
    arr = []
    tmp = n
    for i in range(2, int(-(-n**0.5 // 1)) + 1):
        if tmp%i == 0:
            cnt = 0
            while tmp%i == 0:
                cnt += 1
                tmp //= i
            arr.append([i, cnt])
    if tmp != 1:
        arr.append([tmp, 1])
    if arr == [] and n != 1:
        arr.append([n, 1])
    return arr

f = factorization(n)
ans = 0
for p, e in f:
    x = 1
    while 1:
        e -= x
        if e < 0:
            break
        x += 1
        ans += 1
print(ans)