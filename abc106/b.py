n=int(input())
l=[]
for i in range(1,201):
    if i%2==0:
        l.append(0)
        continue
    c=0
    for j in range(1,i+1):
        if i%j==0:
            c+=1
    if c==8:
        l.append(1)
    else:
        l.append(0)
print(sum(l[:n]))
