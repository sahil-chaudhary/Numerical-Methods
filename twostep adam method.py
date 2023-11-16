import math
def adambashforthexplictit(a,b,y_a,h):
    """The function return ths value of y at b using two step Adam Bashforth Explicit Method"""
    w_0=y_a
    t=a
    #compute first step using Runge Kutta Method of order 4
    w_1=euler(a,a+h,y_a,h/5)#error has to be of same order
    while t<b-h:
        w=w_1+h*(3*f(t+h,w_1)-f(t,w_0))/2
        t+=h
        w_0=w_1
        w_1=w
        print(w)
    print(w)
    return w

def euler(a,b,y_a,h):
    """The function return the value of y at b using euler method"""
    w=y_a
    t=a
    while t<b:
        w=w+h*f(t,w)
        t+=h
    return w

def f(t,y):
    """The function return the value of f(t,y)"""
    a=t*math.exp(3*t)-2*y
    return a
def error(a,b,y_a,h):
    actual=(1/5)*math.exp(3*b)*b-(1/25)*math.exp(3*b)+(1/25)*math.exp(-2*b)
    print(actual)
    return abs(actual-adambashforthexplictit(a,b,y_a,h))
a=0
b=1
y_a=0
h=0.2
print(error(a,b,y_a,h))

