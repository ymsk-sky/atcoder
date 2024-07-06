from sortedcontainers import SortedList

n, t = map(int, input().split())
s = input()
xl = list(map(int, input().split()))
l = [(c, x) for c, x in zip(s, xl)]
xl = [x - t if c == "0" else x + t for c, x in sorted(l, key=lambda e: e[1])]
sl = SortedList(xl)

ans = 0
for x in xl:
    sl.discard(x)
    ans += sl.bisect_right(x)
print(ans)


"""
2<=n<=2*10**5
1<=t<=10**9
-10**9<=x<=10**9

6 3
101010
-5 -1 0 1 2 4

  -5 -4 -3 -2 -1  0  1  2  3  4  5
0: 1  .  .  .  2  3  4  5  .  6  .
1: .  1  .  2  .  4  3  .  56 .  .
2: .  .  12 .  4  .  .  36 .  5  .
3: .  2  .  14 .  .  6  .  3  .  5
"""