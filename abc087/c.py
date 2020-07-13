n=int(input())
l=[list(map(int,input().split()))for _ in range(2)]
a=0
for i in range(n):
    a=max(a,sum(l[0][:i+1])+sum(l[1][i:]))
print(a)
