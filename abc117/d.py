"""
1以上k以下の整数で
f(x)=(x XOR A1)+(x XOR A2)+...+(x XOR An)
の値が最大となるf(x)を求める
"""
n,k=map(int,input().split())
l=list(map(int,input().split()))

"""
3 7
1 6 3
14
f(4) = 4XOR1 + 4XOR6 + 4XOR3 が最大

7:111
6:110
5:101
4:100
3:011
2:010
1:001
0:000

1:001
6:110
3:011
"""
