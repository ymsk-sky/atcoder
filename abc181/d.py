"""
8*125=1000なので下3桁のみを考えればよい
"""
from collections import Counter
s=input()
# 2桁以下の場合
if len(s)<=2:
    # そのままの値もしくは反転した値(18->81)を判定
    if int(s)%8==0 or int(s[::-1])%8==0:
        print('Yes')
    else:
        print('No')
    exit()
# 3桁以上の場合
cnt=Counter(s)
for i in range(112,1000,8):
    if not Counter(str(i)) - cnt:
        print('Yes')
        exit()
print('No')
