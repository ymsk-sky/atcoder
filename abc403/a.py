n = int(input())
al = list(map(int, input().split()))
ans = 0
for i in range(0, n, 2):
    ans += al[i]
print(ans)
