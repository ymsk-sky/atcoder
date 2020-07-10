n=int(input())
ss=list(map(str,input().split()))
print('Three'if len(set(ss))==3else'Four')
