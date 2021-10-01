n=int(input())
s=[]
while n!=0:
    if n%2==1:
        s.append('A')
        n-=1
    else:
        s.append('B')
        n//=2
print(''.join(s[::-1]))
