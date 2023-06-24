n = int(input())
al = list(map(int, input().split()))
ans = []
cnt = 0
for i in range(n*7):
    cnt += al[i]
    if i%7 == 6:
        ans.append(cnt)
        cnt = 0

print(*ans)
