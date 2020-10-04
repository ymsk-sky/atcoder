n=int(input())
imosu=[0]*(10**6+2)
for _ in range(n):
    a,b=map(int,input().split())
    imosu[a]+=1
    imosu[b+1]-=1
for i in range(1,10**6+1):
    imosu[i]+=imosu[i-1]
print(max(imosu[:-1]))

"""
4
0 2
2 3
2 4
5 6

4
1000000 1000000
1000000 1000000
0 1000000
1 1000000
"""
