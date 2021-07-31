xl=input()
if len(set(xl))==1:
    print('Weak')
    exit()
c=0
for x1,x2 in zip(xl,xl[1:]):
    if x1=='9':
        x1='-1'
    if int(x1)+1==int(x2):
        c+=1
print('Weak' if c==3 else 'Strong')
