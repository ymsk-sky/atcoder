n, q = map(int, input().split())
tl = list(map(int, input().split()))
l = [1] * n
for t in tl:
    l[t - 1] = 1 - l[t - 1]
print(sum(l))
