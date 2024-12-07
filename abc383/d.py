from bisect import bisect_right

# エラトステネスの篩で素数判定(l[i] == 1 のときiは素数)
M = 4 * 10**6
l = [1] * (M + 1)
l[0] = l[1] = 0
for i in range(2, M + 1):
    if l[i] == 0:
        continue
    for j in range(2*i, M + 1, i):
        l[j] = 0
pl = [i for i in range(M + 1) if l[i]]  # 素数リスト
ql = [p**2 for p in pl]  # 素数**2リスト
m = len(ql)

n = int(input())
ans = 0

# x**8 <= n
for p in pl:
    if p**8 <= n:
        ans += 1
    else:
        break

# a < bの x**2 * y**2 <= n
for i in range(m):
    a = ql[i]
    j = bisect_right(ql, n // a)
    b = ql[j]
    if a * b > n:
        j -= 1
    if j <= i:
        continue
    cnt = j - i
    ans += cnt
print(ans)

"""
4, 9, 25, 49, 121, 169, 289, 361, 529, 841, 961, 1369, 1681, 1849, 2209, 2809, 3481, 3721, 4489, 5041

x   : 0 1 2 3  4  5  6  7  8
x**2: 0 1 4 9 16 25 36 49 64

N=200
i=3, a=3**2=9
200//9=22
j=5-1=4, b=4**2=16

i**2 * j**2 = 144
3**2 * 4**2=2**4
"""