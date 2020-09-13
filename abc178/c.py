n=int(input())
m=10**9+7
if n==1:
    print(0)
else:
    # かぶりを考えないと
    print((2*(n-1)*10**(n-2))%m)

"""ex3
869121
2511445
"""
