n = int(input())
al = list(map(int, input().split()))
bl = list(map(int, input().split()))

al.sort()
M = 10**9

left = 0
right = M + 1
while right - left > 1:
    mid = (left + right) // 2
    boxes = sorted(bl + [mid])
    ok = True
    for a, b in zip(al, boxes):
        if a > b:
            ok = False
            break
    if ok:
        right = mid
    else:
        left = mid
print(-1 if right == M + 1 else right)
