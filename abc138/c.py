n=int(input())
vs=list(map(int,input().split()))
while not len(vs)==1:
    vs.sort()
    a=vs.pop(0)
    b=vs.pop(0)
    t=(a+b)/2
    vs.append(t)
print(vs[0])
