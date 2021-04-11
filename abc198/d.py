from itertools import permutations
s1=input()
s2=input()
s3=input()
s=list(set(s1+s2+s3))
l=len(s)
if l>10:
    print('UNSOLVABLE')
    exit()
for p in permutations(range(10),l):
    d1=s1
    d2=s2
    d3=s3
    f=1
    for val, dig in zip(s,p):
        d1=d1.replace(val,str(dig))
        d2=d2.replace(val,str(dig))
        d3=d3.replace(val,str(dig))
        if d1[0]=='0' or d2[0]=='0' or d3[0]=='0':
            f=0
            break
    if f:
        if int(d1)+int(d2)==int(d3):
            print(d1)
            print(d2)
            print(d3)
            exit()
print('UNSOLVABLE')

"""
p
q
p
"""
