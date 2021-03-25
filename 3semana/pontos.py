import math
 
def distancia(xa,ya, xb,yb):
    """ Calcula a distancia entre dois pontos"""
    dx = xb-xa
    dy = yb-ya
    d = math.sqrt(dx*dx + dy*dy)
    return d    
 
x0 = float(input("Digite x0 da origem: "))
y0 = float(input("Digite y0 da origem: "))
 
n = int(input("Digite n:"))
 
dmin = -1
for i in range(0,n,1):
    x = float(input("Digite x%d: "%(i+1)))
    y = float(input("Digite y%d: "%(i+1)))
    d = distancia(x0,y0, x,y)
    if dmin < 0 or d < dmin:
        dmin = d
        xmin = x
        ymin = y
 
print("x=%.2f, y=%.2f, d=%.2f"%(xmin,ymin,dmin))