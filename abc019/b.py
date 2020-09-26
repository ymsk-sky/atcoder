s=input()+' '
c=1
for a,b in zip(s,s[1:]):
    if a==b:
        c+=1
    else:
        print(a+str(c),end='')
        c=1
print('')
