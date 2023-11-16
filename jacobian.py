import math
import numpy
def nonlinearfinitemethod(a,b,y_a,y_b,n):
    h=(b-a)/(n+1)
    maxiter=1000
    tol=1e-40
    w_old=numpy.linspace(y_a,y_b,n)
    w_new=numpy.linspace(y_a,y_b,n)
    J=numpy.zeros((n,n))
    F=numpy.zeros(n)
    for i in range(maxiter):
        for i in range(n): #compute F 
            x=a+(i+1)*h
            if i==0:
                F[i]=2*w_old[i]-w_old[i+1]+h**2*f(x,w_old[i],(w_old[i+1]-y_a)/(2*h))-y_a
            elif i==n-1:
                F[i]=2*w_old[i]-w_old[i-1]+h**2*f(x,w_old[i],(y_b-w_old[i-1])/(2*h))-y_b
            else:
                F[i]=2*w_old[i]-w_old[i+1]-w_old[i-1]+h**2*f(x,w_old[i],(w_old[i+1]-w_old[i-1])/(2*h))
        for i in range(n):#fill the diagonal of J
            x=a+(i+1)*h
            if i==0:
                J[i][i]=2+h**2*derivative(x,w_old[i],(w_old[i+1]-y_a)/(2*h))
            elif i==n-1:
                J[i][i]=2+h**2*derivative(x,w_old[i],(y_b-w_old[i-1])/(2*h))
            else:
                J[i][i]=2+h**2*derivative(x,w_old[i],(w_old[i+1]-w_old[i-1])/(2*h))
        for i in range(n-1): #fill the upper and lower diagonal of J
            x=a+(i+1)*h
            J[i][i+1]=-1+h/2*derivative_y(x,w_old[i],(w_old[i+1]-w_old[i-1])/(2*h))
            J[i+1][i]=-1-h/2*derivative_y(x,w_old[i],(w_old[i+1]-w_old[i-1])/(2*h))
        delta=numpy.linalg.solve(J,F)
        w_new=w_old.copy()-delta
        if numpy.linalg.norm(w_new-w_old)<tol:
            break
        w_old=w_new.copy()
    return w_new

def derivative(x,w,dw):#compute derivative about w
    h=1e-50
    f_h=f(x,w+h,dw)
    g=f(x,w,dw)
    return (f_h-g)/h
def derivative_y(x,w,dw): #compute derivative about dw
    h=1e-50
    f_h=f(x,w,dw+h)
    g=f(x,w,dw)
    return (f_h-g)/h

def f(x,w,dw):
    value=1/8*(32+2*x**3-w*dw)
    return value
def error(a,b,y_a,y_b,n):
    h=(b-a)/(n+1)
    x=a+h
    w=nonlinearfinitemethod(a,b,y_a,y_b,n)
    actual=[]
    error=[]
    print("The approximate values are",w)
    for i in range(n):
        x=a+(i)*h
        y=x**2+16/x
        actual.append(y)
        error.append(abs(actual[i]-w[i]))
    print("The actual values are",actual)
    return error

a=1
b=2
y_a=1
y_b=2
n=9
print("The approx is", error(a,b,y_a,y_b,n))
        