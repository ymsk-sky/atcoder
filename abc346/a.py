n = int(input())
al = list(map(int, input().split()))

bl = []
for i in range(n - 1):
    b = al[i] * al[i + 1]
    bl.append(b)
print(*bl)
