n=int(input())
l=list(map(int,input().split()))
m=[abs(x) for x in l]
print(sum(m))
print(sum([x**2 for x in l])**(1/2))
print(max(m))
