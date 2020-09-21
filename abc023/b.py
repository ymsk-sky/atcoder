n=int(input())
s=input()
t='b'
if n%2==0:
    print(-1)
    exit()
for i in range((n-1)//2):
    if i%3==0:
        t='a'+t+'c'
    elif i%3==1:
        t='c'+t+'a'
    elif i%3==2:
        t='b'+t+'b'
print((n-1)//2 if s==t else -1)
