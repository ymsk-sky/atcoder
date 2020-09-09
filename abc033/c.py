s=input()
c=0
for p in s.split('+'):
    if '0' in p:
        pass
    else:
        c+=1
print(c)
