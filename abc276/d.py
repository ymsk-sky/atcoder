n = int(input())
al = list(map(int, input().split()))

def factorization(n):
    arr = []
    temp = n
    for i in range(2, int(-(-n**0.5//1))+1):
        if temp%i==0:
            cnt=0
            while temp%i==0:
                cnt+=1
                temp //= i
            arr.append([i, cnt])

    if temp!=1:
        arr.append([temp, 1])

    if arr==[]:
        arr.append([n, 1])

    return arr

fl = [[0, 0] for _ in range(n)]
kl = []
for i in range(n):
    f = factorization(al[i])
    for x, y in f:
        if x == 1:
            continue
        elif x == 2:
            fl[i][0] += y
        elif x == 3:
            fl[i][1] += y
        else:
            kl.append(x ** y)

x2 = min(fl, key=lambda f: f[0])[0]
x3 = min(fl, key=lambda f: f[1])[1]

ans = 0
for i in range(n):
    a = al[i]
    for k in kl:
        if a % k != 0:
            print(-1)
            exit()
    b, c = fl[i]
    ans += b - x2
    ans += c - x3
print(ans)
