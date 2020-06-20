x=int(input())
for i in range(1,361):
    if i*x%360==0:
        break
print(i)
