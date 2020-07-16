a,b=map(int,input().split())
s=input()
if s[:a].isdecimal() and s[a+1:].isdecimal() and s[a]=='-':
    print('Yes')
else:
    print('No')
