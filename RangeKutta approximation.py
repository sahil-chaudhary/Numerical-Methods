import math
def rangekutta(y_x,a,b,n):
    """The function approximates y(b) using rangekutta method"""
    h=(b-a)/n
    t=a
    w=y_x
    for i in range(n):
        k_1=h*f(t,w)
        k_2=h*f(t+h/2,w+k_1/2)
        k_3=h*f(t+h/2,w+k_2/2)
        k_4=h*f(t+h,w+k_3)
        w=w+(k_1+2*k_2+2*k_3+k_4)/6
        t=a+i*h
    print(w)
    return w

def h(x):
    """Solution we seeking for"""
    a=x*math.exp(3*x)
    b=a/5-math.exp(3*x)/25+math.exp(-2*x)/25
    print(b)
    return b

def f(x,y):
    a=x*math.exp(3*x)-2*y
    return a

def error2(y_x,a,b,n):
    return abs(h(b)-rangekutta(y_x,a,b,n))


a=0
b=1
n=2
y_x=0
print(error2(y_x,a,b,n))
