a,b,c,d=map(int,input().split())
l=a+b
r=c+d
print('Left'if l>r else'Right'if l<r else'Balanced')
