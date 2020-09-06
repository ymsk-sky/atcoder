n=int(input())
p=[input() for _ in range(n)]
for i in range(n):
    for j in range(n-1,-1,-1):
        print(p[j][i],end='')
    print('')
print('')
