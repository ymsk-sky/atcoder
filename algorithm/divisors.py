# nの約数をO(√n)で算出する。
# AtCoder制約 10**9にも間に合うアルゴリズム

""" Reference """
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

""" short """
def md(n):
    l,u=[],[]
    i=1
    while i*i<=n:
        if n%i==0:
            l.append(i)
            if i!=n//i:
                u.append(n//i)
        i+=1
    return l+u[::-1]
