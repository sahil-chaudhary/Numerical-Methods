import math
def trapezoidalapproximation(y_x,a,b,n):
    """The function uses trapezoidal approximation to solve the differential equation y'=f(t,y) with y(a)=y_x and returns the value of y(b). The function uses fixed point iteration method to solve issue f(t_(i+1),w_(i+1))"""
    h=(b-a)/n
    t=a
    w=y_x
    for i in range(1,n+1):
        w=w+h*(f(t,w)+f(t+h,w+(h/2)*(f(t,w)+f(t+h,w))))/2
        t=a+i*h
    print(w)
    return w


def f(x,y):
    a=x*math.exp(3*x)
    b=a-2*y
    return b


def h(x):
    """Solution we seeking for"""
    a=x*math.exp(3*x)
    b=a/5-math.exp(3*x)/25+math.exp(-2*x)/25
    print(b)
    return b
      

def error2(y_x,a,b,n):
    return abs(h(b)-trapezoidalapproximation(y_x,a,b,n))


a=0
b=1
n=2
y_x=0
print(error2(y_x,a,b,n))
