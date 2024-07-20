n, t, p = map(int, input().split())
ll = list(map(int, input().split()))
for i in range(1000):
    if sum([1 for l in ll if l + i >= t]) >= p:
        print(i)
        break
