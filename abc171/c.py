n=int(input())
s=''
while n:
    n-=1
    c=chr(ord('a')+int(n%26))
    s+=c
    n//=26
print(s[::-1])
