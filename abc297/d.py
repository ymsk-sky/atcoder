a, b = map(int, input().split())
if a == b:
    print(0)
    exit()
if a < b:
    a, b = b, a

ans = 0
while a%b != 0:
    n = a//b
    a -= b*n
    ans += n
    if a < b:
        a, b = b, a

n = a//b
ans += n - 1

print(ans)

"""
1<=a,b<=10**18
"""
