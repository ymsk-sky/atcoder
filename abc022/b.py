n=int(input())
l=set()
c=0
for _ in range(n):
    a=int(input())
    if a in l:
        c+=1
    else:
        l.add(a)
print(c)
