import math
def taylormethod(y_x,a,b,n):
    """The function uses taylor method appxoimation to estimate the value of y(b)"""
    h=(b-a)/n
    t=a
    w=y_x
    for i in range(n):
        w=w+h*(f(t,w)+(h/2)*g(t,w)) #f represents y'=f(x,y) and g represents y''=g(x,y)
        t=a+i*h
    print(w)
    return w

def f(x,y):
    a=x*math.exp(3*x)-2*y
    return a

def g(x,y):
    h=0.0001
    """The function return the value of y''=g(x,y)"""
    f_x=(f(x+h,y)-f(x,y))/h
    f_y=(f(x,y+h)-f(x,y))/h
    value=f_x+f(x,y)*f_y
    return value

def h(x):
    """Solution we seeking for"""
    a=x*math.exp(3*x)
    b=a/5-math.exp(3*x)/25+math.exp(-2*x)/25
    print(b)
    return b

def error1(y_x,a,b,n):
    """The function returns the error of the approximation"""
    return abs(h(b)-taylormethod(y_x,a,b,n))

a=0
b=1
n=2
y_x=0
print(error1(y_x,a,b,n))