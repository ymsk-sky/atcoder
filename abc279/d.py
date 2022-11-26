a, b = map(int, input().split())

def f(x):
    return (1.0*b*x + 1.0*a/((x + 1)**0.5))

def fd(x):
    # f'(x)
    # return (1.0*b - 1.0*a*((x + 1)**(-3/2))/2)
    return (b - a/2*(x+1)**(-3/2))

if b >= a:
    print(f(0))
    exit()

left = 0
right = 10**18
while right - left > 1:
    mid = (left + right) // 2
    tmp = fd(mid)
    if tmp == 0:
        break
    elif tmp < 0:
        left = mid
    else:
        right = mid

ans = min(f(mid), f(left), f(right))
print(f"{ans:.8f}")
#print(f"{f(mid):.8f}")
#print(f"{f(left):.8f}")
#print(f"{f(right):.8f}")

"""
1<=a,b<=10**18
"""
