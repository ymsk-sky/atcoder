N, K, A = map(int,input().split())
m = K % N
l = [a for a in range(1, N + 1)]
print((l + l)[A + m - 2])
