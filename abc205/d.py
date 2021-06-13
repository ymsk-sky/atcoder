from bisect import bisect_right
n,q=map(int,input().split())
al=list(map(int,input().split()))
kl=[int(input()) for _ in range(q)]

def sr(k,base):
    ix=bisect_right(al,k)
    if ix==0:
        return 0
    if k==base:
        return sr(k+ix,base)
    else:
        return ix

for k in kl:
    p=sr(k,k)  # プラスする数
    print(k+p)

"""
5 5
2 4 6 8 10
1
2
3
4
5

1 3 5 7 9
"""
