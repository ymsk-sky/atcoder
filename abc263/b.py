n = int(input())
l = list(map(int, input().split()))
p = l[-1]
ans = 0
while 1:
    ans += 1
    if p == 1:
        break
    p = l[p - 2]
print(ans)
