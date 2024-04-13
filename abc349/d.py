l, r = map(int, input().split())
ans = []
while l < r:
    tmp = r
    cnt = 0
    while tmp % 2 == 0:
        tmp //= 2
        cnt += 1
    # 2**cnt * tmpの形で表される
    l_tmp = 2**cnt * (tmp - 1)
    while l_tmp < l:
        cnt -= 1
        tmp *= 2
        l_tmp = 2**cnt * (tmp - 1)
    res = [l_tmp, r]
    ans.append(res)
    r = l_tmp

print(len(ans))
for an in ans[::-1]:
    print(*an)

"""
0<=l<r<=2**60

0 1024
1
0 1024

0 1023
10
0 512
512 768
768 896
...
1022 1023
"""