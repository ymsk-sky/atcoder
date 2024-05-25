n, m = map(int, input().split())
al = list(map(int, input().split()))
bl = list(map(int, input().split()))
s = set(al)
cl = sorted(al + bl)
for c1, c2 in zip(cl, cl[1:]):
    if c1 in s and c2 in s:
        print("Yes")
        exit()
print("No")
