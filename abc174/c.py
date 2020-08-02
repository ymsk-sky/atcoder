k=int(input())
if k%2==0:
    print(-1)
    exit()
for i in range(1,10**6):
    # v=int('7'*l)
    v=(10**i-1)*7//9
    if v%k==0:
        break
print(i)
