"""
2,3,4をn個使ってmを作ることは可能か？
m = 2*a + 3*b + 4*c
3*2=6=2*1+4*1より3を2個は2と4を1個ずつに変換可能
すなわち3=0個と3=1個の場合のみ全探索

3 9
1 1 1
"""
n,m=map(int,input().split())
# 3が0個
for i in range(n+1):
    s=2*i+4*(n-i)
    if s==m:
        print(i, 0, n-i)
        exit()
# 3が1個
for i in range(n):
    s=2*i+4*(n-i-1)+3
    if s==m:
        print(i, 1, n-i-1)
        exit()
print(-1,-1,-1)
