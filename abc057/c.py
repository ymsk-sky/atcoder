def make_divisors(n):
    lower_divisors , upper_divisors = [], []
    i = 1
    while i*i <= n:
        if n % i == 0:
            lower_divisors.append(i)
            if i != n // i:
                upper_divisors.append(n//i)
        i += 1
    return lower_divisors + upper_divisors[::-1]
n=int(input())
l=make_divisors(n)
s=(len(l)+1)//2
a=len(str(l[:s][-1]))
b=len(str(l[::-1][:s][-1]))
print(max(a,b))
