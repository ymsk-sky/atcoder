from itertools import product
a,b,c,d=map(int,input())
for op1,op2,op3 in product((1,-1),repeat=3):
    if a+op1*b+op2*c+op3*d==7:
        x='+'if op1==1else'-'
        y='+'if op2==1else'-'
        z='+'if op3==1else'-'
        print('{}{}{}{}{}{}{}=7'.format(a,x,b,y,c,z,d))
        exit()
