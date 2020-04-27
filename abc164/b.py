a,b,c,d=map(int,input().split())
t=c//b+1if not c/b==c//b else c//b
a=a//d+1if not a/d==a//d else a//d
print('Yes'if t<=a else'No')
