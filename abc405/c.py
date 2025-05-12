n = int(input())
al = list(map(int, input().split()))

acc = al[:]
for i in range(n - 1, 0, -1):
    acc[i - 1] += acc[i]

ans = 0
for i in range(n - 1):
    ans += al[i] * acc[i + 1]
print(ans)
