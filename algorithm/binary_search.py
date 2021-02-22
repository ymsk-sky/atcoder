"""二分探索
ABC192 - D問題 Base n
https://atcoder.jp/contests/abc192/tasks/abc192_d

答えを1,2,3,...,Nと順に調べていくと計算量O(N)となるため
LEFT(最小)とRIGHT(最大)の範囲でVAL=(LEFT+RIGHT)/2として
VALと答えを比較し答えがVALより大きいか小さいかで答えを絞っていく手法

実際にpythonで実装したもの
"""
x=input()
m=int(input())
d=int(max(x))
def decode(digits,base):  # base進数の数digits(str)を10進数へ変換する
    value=0
    for digit in digits:
        value=value*base+int(digit)
    return value
# xが一桁のときは例外
if len(x)==1:
    print(1 if int(x)<=m else 0)
######## 実装部分 ########
else:  # 二分探索
    left=d
    right=m+1
    while right-left>1:
        val=(left+right)//2
        if decode(x,val)>m:
            right=val
        else:
            left=val
    print(left-d)
########################
