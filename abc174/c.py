"""
7,77,777,... -> {a1,a2,a3,...}の数列として考える
ai = 0 mod k
である最小のiを求める(kで割ったあまりが0)
"""
k=int(input())
b=7%k
if b==0:
    print(1)
    exit()
for i in range(2,k+1):
    b=(b*10+7)%k
    if b==0:
        print(i)
        exit()
print(-1)
