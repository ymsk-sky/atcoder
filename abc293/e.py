a, x, m = map(int, input().split())
if a == 1:
    print(x%m)
else:
    ans = (pow(a, x, m*(a - 1)) - 1) // (a - 1)
    print(ans)

"""
1<=a,m<=10*9
1<=x<=10**12

x-1
 Σ a**i = (a**x - 1)/(a - 1)
i=0
"""
