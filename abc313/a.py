n = int(input())
pl = list(map(int, input().split()))
p1 = pl[0]
if n == 1:
    print(0)
    exit()
pm = max(pl[1:])
print(max(0, pm - p1 + 1))
