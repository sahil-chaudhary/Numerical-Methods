import math
def nonlinearshooting(a,b,y_a,y_b,n):
    """The method solves the nonlinear boundary value problem using secant approximation"""
    h=(b-a)/n
    y=[[],[]]
    z=[]
    t=[]
    tol=10**(-20)
    #initial guess for tk's
    for i in range(3):
        tk=(i+1)*(y_b-y_a)/(b-a)
        t.append(tk)
    #compute y(tk) for k=1,2
    for i in range(n+1):
        x=a+i*h
        y_x=IVP1(a,x,y_a,t[0],(i+1)*n)
        y[0].append(y_x)
        y_x=IVP1(a,x,y_a,t[1],(i+1)*n)
        y[1].append(y_x)
    
    k=0 
    maxiter=1000
    while k<=maxiter:
        for i in range(n+1):
            x=a+i*h
            y_x=IVP1(a,x,y_a,t[k+2],(i+1)*n)
            z.append(y_x)
        y.append(z)
        #use secant method to find new tk
        tk1=t[k+1]-((t[k+1]-t[k])/(y[k+1][n]-y[k][n]))*(y[k+1][n]-y_b)
        t.append(tk1)
        if abs(t[k+2]-t[k+1])<tol:
            break
        k=k+1
        z=[]
    return y[k+1]

def IVP1(a,b,y_a,t,n): #use rungekuttaorder 4 for higher order differential equation of order 2
    h=(b-a)/n
    w1=[]
    w2=[]
    w1.append(y_a)
    w2.append(t)
    k1=[[],[]]
    k2=[[],[]]
    k3=[[],[]]
    k4=[[],[]]
    for i in range(n+1):
        x=a+i*h
        k1[0].append(h*w2[i])
        k1[1].append(h*f(x,w1[i],w2[i]))
        k2[0].append(h*(w2[i]+k1[0][i]/2))
        k2[1].append(h*f(x+h/2,w1[i]+k1[0][i]/2,w2[i]+k1[1][i]/2))
        k3[0].append(h*(w2[i]+k2[1][i]/2))
        k3[1].append(h*f(x+h/2,w1[i]+k2[0][i]/2,w2[i]+k2[1][i]/2))
        k4[0].append(h*(w2[i]+k3[1][i]))
        k4[1].append(h*f(x+h,w1[i]+k3[0][i],w2[i]+k3[1][i]))
        w1.append(w1[i]+(k1[0][i]+2*k2[0][i]+2*k3[0][i]+k4[0][i])/6)
        w2.append(w2[i]+(k1[1][i]+2*k2[1][i]+2*k3[1][i]+k4[1][i])/6)
    return w1[n]


def f(x,y1,y2):
    a=p(x)
    b=q(x)
    c=r(x)
    value=a*y2+b*y1+c
    return value

def g(x,y1,y2):
    a=p(x)
    b=q(x)
    value=a*y2+b*y1
    return value
def p(x):
    return 0
def q(x):
    return 4
def r(x):
    value=-4*x
    return value
def error(a,b,y_a,y_b,n):
    h=(b-a)/n
    y=nonlinearshooting(a,b,y_a,y_b,n)
    print(y)
    actual=[]
    error=[]
    for i in range(n+1):
        x=a+(i)*h
        actual.append(math.exp(2)/(math.exp(4)-1)*(math.exp(2*x)-math.exp(-2*x))+x)
        error.append(abs(actual[i]-y[i]))
    print(actual)
    return error
a=0
b=1
y_a=0
y_b=2
n=10
y=error(a,b,y_a,y_b,n)
print(y)
