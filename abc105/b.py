n=int(input())
for c in range(26):
    for d in range(15):
        if c*4+d*7==n:
            print('Yes')
            exit()
print('No')
