a=int(input())
b=int(input())
c=0
z=a
while 1:
    z+=1
    if z>9:
        z=0
    c+=1
    if z==b:
        break
d=0
while 1:
    a-=1
    if a<0:
        a=9
    d+=1
    if a==b:
        break
print(min(c,d))
