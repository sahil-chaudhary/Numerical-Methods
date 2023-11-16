import math
import numpy as np
def nonlinearfinitedifference(a,b,y_a,y_b,n):
    h=(b-a)/(n+1)
    J=np.zeros((n,n))
    w=np.zeros(n)
    w_old=np.zeros(n)
    F=np.zeros(n) #f is the vector of f(w_i)
    maxiter=1000
    tol=1e-5
    for i in range(maxiter):
        for i in range(n):
            x=a+(i+1)*h
            if i==0:
                J[i][i]=2+h**2*Q(x,w[i],(w[i+1]-y_a)/(2*h))
            elif i==n-1:
                J[i][i]=2+h**2*Q(x,w[i],(y_b-w[i-1])/(2*h))
            else:
                J[i][i]=2+h**2*Q(x,w[i],(w[i+1]-w[i-1])/(2*h)) #diagonal filling and Q is the derivative of f with respect to w_i
        for i in range(n-1): #filling the upper and lower diagonals
            x=a+(i+1)*h
            if i!=n-1:
                J[i][i+1]=-1-h*Q1(x,w[i],(w[i+1]-w[i-1])/(2*h))/2 #Q1 is the derivative of f with respect to w_i+1
            if i!=0:
                J[i][i-1]=-1+h*Q1(x,w[i],(w[i+1]-w[i-1])/(2*h))/2 #Q2 is the derivative of f with respect to w_i-1
        #Now, solving the system of equations
        J[n-1][n-2]=-1+h**2*Q2(x,w[n-1],(y_b-w[n-2])/(2*h),h)
        
        for i in range(n):
            x=a+(i+1)*h
            if i==0:
                dy=w[i]
                y=(w[i+1]-y_a)/(2*h)
                F[i]=2*w[i]-w[i+1]+h**2*f(x, dy, y)
            if i==n-1:
                dy=w[i]
                y=(y_b-w[i-1])/(2*h)
                F[i]=2*w[i]-w[i-1]+h**2*f(x,dy,y)
            else:
                dy=w[i]
                y=(w[i+1]-w[i-1])/(2*h)
                F[i]=2*w[i]-w[i+1]-w[i-1]+h**2*f(x,dy,y)
        if i==0:
            w_old=F.copy()
        w=np.linalg.solve(J,-F)+w_old
        if np.linalg.norm(w-w_old) < tol:
            break
        w_old=w.copy()
    return w

def Q(x,w,dw): #the derivative is with respect to w_i(the term in middle)
    h=1e-5
    f_=f(x,w+h,dw)
    diff=(f_-f(x,w,dw))/h
    return diff

def Q1(x,w,dw):
    a=1e-5
    f_=f(x,w,dw+a)
    diff=(f_-f(x,w,dw))/a
    return diff
def Q2(x,w,dw,h):
    a=1e-5
    f_=f(x,w,dw-(a/(2*h)))
    diff=(f_-f(x,w,dw))/a
    return diff
def f(x,w,dw):
    value=32+2*(x**3)-w*dw
    value=value/8
    return value
def error(a,b,y_a,y_b,n):
    h=(b-a)/(n+1)
    x=a+h
    w=nonlinearfinitedifference(a,b,y_a,y_b,n)
    actual=[]
    error=[]
    print("The approximate values are",w)
    for i in range(n):
        x=a+(i)*h
        actual.append(x**2+(16/x))
        error.append(abs(actual[i]-w[i]))
    print("The actual values are",actual)
    return error

a=1
b=3
y_a=17
y_b=43/3
n=20
print("The error is",error(a,b,y_a,y_b,n))
        