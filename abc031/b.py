l,h=map(int,input().split())
n=int(input())
al=[int(input()) for _ in range(n)]
for a in al:
    if l<=a<=h:
        print(0)
    if l>a:
        print(l-a)
    if h<a:
        print(-1)
