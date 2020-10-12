"""
a*b + c = n
を満たすa,b,c(正整数)は何組

a*b < n
となる(a,b)の組に対する
a*b + c = n
のcは一意に決まる(ひとつのみ存在する)ため
a*b < n
を考えればよい
aを固定として1~(n-1)まで全探索する
"""
n=int(input())
ans=0
for a in range(1,n):
    ans+=(n-1)//a
print(ans)
