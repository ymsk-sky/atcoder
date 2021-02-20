n,k=map(str,input().split())
def f(x):
    x=''.join(sorted(x))
    return str(int(x[::-1])-int(x))
for _ in range(int(k)):
    n=f(n)
print(n)
