n, m = map(int, input().split())
al = list(map(int, input().split()))

xl = []
for x in range(1, n + 1):
    if x in al:
        continue
    xl.append(x)

print(len(xl))
print(*xl)
