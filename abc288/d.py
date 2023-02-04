n, k = map(int, input().split())
al = list(map(int, input().split()))
q = int(input())

ans = []
for _ in range(q):
    l, r = map(int, input().split())
    l, r = l - 1, r - 1
    ans.append()
print(*ans, sep="\n")


"""
1<=n<=2*10**5
1<=k<=10
-10**9<=a<=10**9
1<=q<=2*10**5
1<=l,r<=n
r-l+1>=k
"""