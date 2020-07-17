x,y=map(int,input().split())
c=1
for _ in range(y):
    x=x*2
    if x>y:
        break
    c+=1
print(c)
