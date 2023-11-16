import math
import numpy as np
import jacobi

def linearfinite(al,bi,y_a,y_b,n):
    h=(bi-al)/(n+1)
    A=np.zeros((n,n))
    B=np.zeros((n,1))
    for i in range(n): #fill the diagonal
        x=al+(i+1)*h
        A[i][i]=2+h**2*q(x)
    for i in range(n-1): #fill the upper 
        x=al+(i+1)*h
        A[i][i+1]=-1+h/2*p(x) #upper diagonal
    for i in range(n-1):
        x=al+(i+2)*h
        A[i+1][i]=-1-h/2*p(x)

    for i in range(n):
        x=al+(i+1)*h
        if i==0:
            B[i][0]=-h**2*r(x)+y_a*(1+h/2*p(x))
        elif i==n-1:
            B[i][0]=-h**2*r(x)+y_b*(1-h/2*p(x))
        else:
            B[i][0]=-h**2*r(x)
  
    W=jacobi.gausssiedelmethod(A,B)
    W=np.insert(W,0,y_a)
    W=np.append(W,y_b)
    W=list(W)
    return W


def p(x):
    return 0
def q(x):
    return -(1+x**2)
def r(x):
    value=64*x**6-128*x**5+128*x**4-128*x**3-704*x**2+768*x-128
    return -value
def error(a,b,y_a,y_b,n):
    approx=linearfinite(a,b,y_a,y_b,n)
    print(approx)
    h=(b-a)/(n+1)
    error=[]
    exact=[]
    for i in range(n+2):
        x=a+i*h
        exact.append(64*x**2*(1-x)**2)
        error.append(abs(approx[i]-exact[i]))
    print(exact)
    return error

a=0
b=1
y_a=0
y_b=0
n=9
print(error(a,b,y_a,y_b,n))