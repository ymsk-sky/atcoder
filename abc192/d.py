x=input()
m=int(input())
d=int(max(x))
min_=int(max(x))+1
max_=20  # logN
def decode(digits, base):
    value = 0
    for digit in digits:
        value = value * base + int(digit)
    return value
ans=(min_+max_)//2
for _ in range(10):
    print(min_,ans,max_)
    if m<decode(x,d+1):
        tmp=min_
        min_=ans
        ans=(tmp+ans)//2
    else:
        tmp=max_
        max_=ans
        ans=(tmp+ans)//2
    if min_==max_:
        break
print(ans)

"""
999
1500
10 ~ 20
15->2169
12->1413
16->2457

10 999
11 1197
12 1413
13 1647
14 1899
15 2169
16 2457
17 2763
18 3087
19 3429
20 3789
"""
