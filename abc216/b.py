n=int(input())
l=[input() for _ in range(n)]
if len(l)==len(set(l)):
    print('No')
else:
    print('Yes')
