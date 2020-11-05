"""下記それぞれの最小を比較する
AABBCC AAAAAA AABBBB AAAAAA
AABBCC AAAAAA AABBBB AAAAAA
AABBCC BBBBBB AABBBB BBBCCC
AABBCC BBBBBB AACCCC BBBCCC
AABBCC CCCCCC AACCCC BBBCCC
AABBCC CCCCCC AACCCC BBBCCC
"""
h,w=map(int,input().split())
# 縦分割
if w%3==0:
    print(0)
    exit()
else:
    tmp1=h
# 横分割
if h%3==0:
    print(0)
    exit()
else:
    tmp2=w
# 1縦2横
tmp3=float('inf')
if h%2==0:
    h1=h2=h//2
else:
    h1=h//2
    h2=h//2+1
for i in range(1,w//2+1):
    a=h*i
    b=h1*(w-i)
    c=h2*(w-i)
    max_=max(a,b,c)
    min_=min(a,b,c)
    tmp3=min(tmp3,max_-min_)
# 2縦1横
tmp4=float('inf')
if w%2==0:
    w1=w2=w//2
else:
    w1=w//2
    w2=w//2+1
for i in range(1,h//2+1):
    a=w*i
    b=w1*(h-i)
    c=w2*(h-i)
    max_=max(a,b,c)
    min_=min(a,b,c)
    tmp4=min(tmp4,max_-min_)
print(min(tmp1,tmp2,tmp3,tmp4))
