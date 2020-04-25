n=int(input())
for a in range(1,10):
    for b in range(1,10):
        if n==a*b:
            print('Yes')
            exit()
print('No')
