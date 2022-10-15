n = int(input())
def f(i):
    if i == 0:
        return 1
    else:
        return i * f(i - 1)

print(f(n))