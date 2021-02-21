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
