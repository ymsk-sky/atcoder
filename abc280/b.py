n = int(input())
sl = list(map(int, input().split()))
al = [0] * n
al[0] = sl[0]
for i in range(1, n):
    al[i] = sl[i] - sl[i - 1]
print(*al)