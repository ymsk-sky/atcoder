n=int(input())
s=input()
a=''
for c in s:
    o=ord(c)+n
    if o>90:
        o-=26
    a+=chr(o)
print(a)
