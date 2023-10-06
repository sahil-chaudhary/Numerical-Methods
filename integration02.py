import math
def simpson(a,b):
    h=b-a
    mid=(a+b)/2
    f_a=(math.cos(a))**2
    f_mid=(math.cos(mid))**2
    f_b=(math.cos(b))**2
    error=(h**5/90)*(8*math.cos((a+b)))
    integral=(h/3)*(f_a+4*f_mid+f_b)-error
    return integral
print(simpson(0,math.pi/3))