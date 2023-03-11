n = int(input())
al = list(map(int, input().split()))
l = [0] * n
for i in range(n):
    a = al[i]
    if l[i] == 0:
        l[a - 1] = 1
cnt = 0
ans = []
for i in range(n):
    if l[i] == 0:
        cnt += 1
        ans.append(i + 1)

print(cnt)
print(*ans)
