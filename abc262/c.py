n = int(input())
l = list(map(int, input().split()))

ans = 0

for i in range(1, n):
    for j in range(i + 1, n + 1):
        if min(l[i -1], l[j - 1]) == i and max(l[i - 1], l[j - 1]) == j:
            ans += 1

print(ans)
