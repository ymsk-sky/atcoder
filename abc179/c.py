n=int(input())
"""
a*b + c = n
を満たすa,b,c(正整数)は何組

a*b = n-c
a*b = v
"""
s=0
for c in range(1,n):
    v=n-c
    for b in range(1,v+1):
        a=v/b
        if a%1==0:
            s+=1
        #print('a={} b={} c={}'.format(a,b,c))
print(s)
