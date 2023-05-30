q = int(input())
ql = [list(map(int, input().split())) for _ in range(q)]
mod = 998244353
s = 1  # 数字
k = 1  # 桁数
for query in ql:
    if query[0] == 1:
        x = query[1]
        s *= 10
        s += x
        k += 1
    elif query[0] == 2:
        k -= 1
        s %= 10**k
    else:
        print(s%mod)
