n=input()
if len(n)==1:
    print('Yes')
    exit()
while 1:
    if n[-1]=='0':
        n=n[:-1]
    else:
        break
l=len(n)
if l<2:
    print('Yes')
    exit()
a=n[:l//2]
b=n[l//2:] if l%2==0 else n[l//2+1:]
a=int(a)
b=int(b[::-1])
#print(a,b)
print('Yes' if a==b else 'No')
