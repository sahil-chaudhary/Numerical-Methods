import math
def comptrap(a,b,n):
    h=(b-a)/n
    integral=0
    while h<=b:
        integral=trapeinteg(a,h)+integral
        a=h
        h=h+0.125
    return float(integral)

def trapeinteg(a,b):
    h=b-a
    f_a=a**3
    f_b=b**3
    error=(h**3/12)*(6*((a+b)/2))
    integral=(h/2)*(f_a+f_b)-error
    return integral

print(comptrap(1,2,8))
