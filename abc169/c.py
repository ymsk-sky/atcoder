from decimal import Decimal
a,b=map(str,input().split())
a=int(a)
b=Decimal(b)
print(int(a*b))
