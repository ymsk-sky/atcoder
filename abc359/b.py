n = int(input())
al = list(map(int, input().split()))
ans = 0
for i in range(2*n - 2):
    if al[i] == al[i + 2]:
        ans += 1
print(ans)
