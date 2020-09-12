from bisect import bisect_left
n=5
l=[0,1,3,5,8]
for i in range(0,10):
    s=bisect_left(l,i)
    if s!=n:
        print('i={}->{}({})'.format(i,s,l[s]))
    else:
        print('FIN',i,s)
