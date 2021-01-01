"""a~bの排他的論理和F(a,b)を求めよ
n XOR n = 0 の特性より
F(a,b) = F(0,a-1) XOR F(0,b)
--
F(0,b)  =0,1,2,...,a-2,a-1,a,a+1,a+2,...,b-2,b-1,b
F(0,a-1)=0,1,2,...,a-2,a-1
--
となるので,直接F(a,b)を求めるよりF(0,n)を求めることを考える.
任意の偶数nについて
n XOR (n+1) = 1
（最下位ビットのみが1違うことから上記はわかる）
よって
  F(0,6)
= 0 XOR 1 XOR 2 XOR 3 XOR 4 XOR 5 XOR 6
= (0 XOR 1) XOR (2 XOR 3) XOR (4 XOR 5) XOR 6
= 1 XOR 1 XOR 1 XOR 6
ここで1 XOR 1 ... XOR 1については1が偶数個なら0,奇数個なら1となる
"""
a,b=map(int,input().split())
