"""
rでソートしてr1<=r2<=...<=rnとすると,
ある(i,j)についてlj<riになるjの個数分がi番目と重なっている.
これを昇順に行っていけばよい.
"""

from sortedcontainers import SortedList

n = int(input())
lrl = [list(map(int, input().split())) for _ in range(n)]
lrl.sort(key=lambda e: e[1])
s = SortedList()
ans = 0
for l, r in lrl[::-1]:
    ans += s.bisect_right(r)
    s.add(l)
print(ans)


"""
2<=n<=5*10**5
0<=l<r<=10**9
"""