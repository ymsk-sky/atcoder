x=int(input())
a=x//11*2
b=x%11
print(a if b==0 else a+1 if b<7 else a+2)
