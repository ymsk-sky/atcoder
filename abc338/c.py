n = int(input())
ql = list(map(int, input().split()))
al = list(map(int, input().split()))
bl = list(map(int, input().split()))
M = 10**6
ans = 0
for x in range(M + 1):
    # Aをx個, Bをy個作る
    rl = []
    for i in range(n):
        q = ql[i]
        a = al[i]
        if q - a*x < 0:
            break
        rl.append(q - a*x)
    else:
        y = M
        for i in range(n):
            if bl[i] == 0:
                continue
            y = min(y, rl[i] // bl[i])
        ans = max(ans, x + y)
print(ans)

"""
1<=n<=10
1<=q<=10**6
0<=a,b<=10**6
1<=a,bが1つはある
"""
