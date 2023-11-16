import math
def threestepadamexplicit(a,b,y_a,h):
    #order 4 local truncation
    w_0=y_a
    t=a
    #compute first step using Runge Kutta Method of order 4
    w_1=RK3(a,a+h,y_a,h/5)#error has to be of same order since implicit has local truncation 
    w_2=RK3(a,a+2*h,y_a,2*h/5)
    while t<b-3*h:
        w=w_2+h*(23*f(t+2*h,w_2)-16*f(t+h,w_1)+5*f(t,w_0))/12
        t+=h
        w_0=w_1
        w_1=w_2
        w_2=w
    print(w)
    return w

def RK3(a,b,y_a,h):
    """The function return the value of y at b using euler method"""
    w=y_a
    t=a
    while t<b:
        k1=f(t,w)
        k2=f(t+(h/3),w+(h/3)*k1)
        k3=f(t+(2*h/3),w+(2*h/3)*k2)
        w=w+(k1+3*k3)*h/4
        t+=h
    return w

def f(t,y):
    """The function return the value of f(t,y)"""
    a=1+(y/t)
    return a
def error(a,b,y_a,h):
    actual=b*math.log(b)+2*b
    print(actual)
    return abs(actual-threestepadamexplicit(a,b,y_a,h))
a=1
b=2
y_a=2
h=0.2
print(error(a,b,y_a,h))