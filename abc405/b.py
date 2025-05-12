n, m = map(int, input().split())
al = list(map(int, input().split()))
ans = 0
while al:
    fin = False
    for x in range(1, m + 1):
        if x not in al:
            fin = True
            break
    if fin:
        break
    ans += 1
    al.pop()
print(ans)
