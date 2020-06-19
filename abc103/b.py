s=input()
t=input()
if s==t:
    print('Yes')
    exit()
u=s
for c in s[::-1]:
    u=c+u[:-1]
    if u==t:
        print('Yes')
        exit()
print('No')
