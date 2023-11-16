import math
def adamsfourthorderpredictor(a,b,y_a,h):
    t=a
    w_0=y_a
    w_1=RK4(a,a+h,y_a,h/5)
    w_2=RK4(a,a+2*h,y_a,h/5)
    w_3=RK4(a,a+3*h,y_a,h/5)
    while t<b-5*h:
        w=w_3+(h*(55*f(t+3*h,w_3)-59*f(t+2*h,w_2)+37*f(t+h,w_1)-9*f(t,w_0)))/24 #predictor
        w=w_3+(h*(9*f(t,w)+19*f(t+3*h,w_3)-5*f(t+2*h,w_2)+f(t+h,w_1)))/24 #corrector
        w_0=w_1
        w_1=w_2
        w_2=w_3
        w_3=w
        t=t+h
    print(w)
    return w

def RK4(a,b,y_a,h):
    t=a
    w=y_a
    while t<b:
        k_1=h*f(t,w)
        k_2=h*f(t+h/2,w+k_1/2)
        k_3=h*f(t+h/2,w+k_2/2)
        k_4=h*f(t+h,w+k_3)
        w=w+(k_1+2*k_2+2*k_3+k_4)/6
        t+=h
    return w

def f(t,y):
    """The function return the value of f(t,y)"""
    a=y-t**2+1
    return a
def error(a,b,y_a,h):
    actual=(1+b)**2-math.exp(b)/2
    print(actual)
    return abs(actual-adamsfourthorderpredictor(a,b,y_a,h))
a=0
b=2
y_a=0.5
h=0.2
print(error(a,b,y_a,h))
    