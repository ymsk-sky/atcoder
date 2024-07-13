xa, ya = map(int, input().split())
xb, yb = map(int, input().split())
xc, yc = map(int, input().split())
ab2 = ((xa - xb)**2 + (ya - yb)**2)
bc2 = ((xb - xc)**2 + (yb - yc)**2)
ca2 = ((xc - xa)**2 + (yc - ya)**2)
m = max(ab2, bc2, ca2)
s = ab2 + bc2 + ca2
print("Yes" if s - m == m else "No")
