def is_prime(n):
    if n<2: return False
    for p in range(2, n):
        if n%p==0:
            return False
    return True
x=int(input())
while not is_prime(x):
    x+=1
print(x)
