n=int(input())
l=list(map(int,input().split()))
m=sorted([a-i for i,a in enumerate(l, start=1)])
b1,b2=m[n//2],m[n//2-1]
print(min(sum([abs(a-b1) for a in m]),sum([abs(a-b2) for a in m])))
