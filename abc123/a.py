l=[int(input()) for _ in range(5)][::-1]
k=int(input())
for i,a in enumerate(l):
    for b in l[i+1:]:
        if a-b>k:
            print(':(')
            exit()
print('Yay!')
