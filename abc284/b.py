t = int(input())
for _ in range(t):
    n = int(input())
    al = list(map(int, input().split()))
    ans = 0
    for a in al:
        if a % 2 == 1:
            ans += 1
    print(ans)