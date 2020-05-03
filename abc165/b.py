x=int(input())
sum_ = 100
for i in range(1, 10**18+2):
    sum_ = int(sum_ * 1.01)
    if sum_ >= x:
        break
print(i)
