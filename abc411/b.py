n = int(input())
dl = list(map(int, input().split()))

for i in range(n - 1):
    ans = []
    tmp = 0
    for j in range(i, n - 1):
        tmp += dl[j]
        ans.append(tmp)
    print(*ans)
