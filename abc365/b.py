n = int(input())
al = list(map(int, input().split()))
ans = sorted([(al[i], i + 1) for i in range(n)], reverse=True)[1]
print(ans[1])
