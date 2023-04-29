n, a, b = map(int, input().split())
cl = list(map(int, input().split()))
for i in range(n):
    if cl[i] == a + b:
        print(i + 1)
