n,s,t=map(int,input().split())
w=int(input())
c=1 if s<=w<=t else 0
for _ in range(n-1):
    a=int(input())
    w+=a
    if s<=w<=t:
        c+=1
print(c)
