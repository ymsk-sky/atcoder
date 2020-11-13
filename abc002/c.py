xa,ya,xb,yb,xc,yc=map(int,input().split())
xa,ya,xb,yb,xc,yc=xa-xa,ya-ya,xb-xa,yb-ya,xc-xa,yc-ya
print(abs(xb*yc-yb*xc)/2)
