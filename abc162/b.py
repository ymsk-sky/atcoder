n=int(input())
print(sum([i for i in range(1,n+1) if not (i%3==0 or i%5==0)]))
