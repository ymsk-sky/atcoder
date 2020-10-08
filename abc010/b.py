n=int(input())
s=0
for i in list(map(int,input().split())):
    if i==2 or i==4 or i==8:
        s+=1
    if i==5:
        s+=2
    if i==6:
        s+=3
print(s)
