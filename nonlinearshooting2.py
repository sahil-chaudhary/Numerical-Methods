import math
def nonlinearshooting(a,b,y_a,y_b,n,m,tol):
    #n is the number of subintervals
    #m is the number of iterations
    #tol is the tolerance
    h=(b-a)/n
    k=1
    TK=(y_b-y_a)/(b-a)
    while k<=m:
        w_1=[y_a]
        w_2=[TK]
        u_1=[0]
        u_2=[1]
        i=1
        while i<=n:
            x=a+(i-1)*h
            k_11=h*w_2[i-1]
            k_12=h*f(x,w_1[i-1],w_2[i-1])
            k_21=h*(w_2[i-1]+0.5*k_12)
            k_22=h*f(x+h/2,w_1[i-1]+0.5*k_11,w_2[i-1]+0.5*k_12)
            k_31=h*(w_2[i-1]+0.5*k_22)
            k_32=h*f(x+h/2,w_1[i-1]+0.5*k_21,w_2[i-1]+0.5*k_22)
            k_41=h*(w_2[i-1]+k_32)
            k_42=h*f(x+h,w_1[i-1]+k_31,w_2[i-1]+k_32)
            w_1.append(w_1[i-1]+(k_11+2*k_21+2*k_31+k_41)/6)
            w_2.append(w_2[i-1]+(k_12+2*k_22+2*k_32+k_42)/6)
            m_11=h*u_2[i-1]
            m_12=h*(f_u(x,w_1[i-1],w_2[i-1])*u_1[i-1]+f_v(x,w_1[i-1],w_2[i-1])*u_2[i-1])
            m_21=h*(u_2[i-1]+0.5*m_12)
            m_22=h*(f_u(x+h/2,w_1[i-1],w_2[i-1])*(u_1[i-1]+0.5*m_11)+f_v(x+h/2,w_1[i-1],w_2[i-1])*(u_2[i-1]+0.5*m_12))
            m_31=h*(u_2[i-1]+0.5*m_22)
            m_32=h*(f_u(x+h/2,w_1[i-1],w_2[i-1])*(u_1[i-1]+0.5*m_21)+f_v(x+h/2,w_1[i-1],w_2[i-1])*(u_2[i-1]+0.5*m_22))
            m_41=h*(u_2[i-1]+m_32)
            m_42=h*(f_u(x+h,w_1[i-1],w_2[i-1])*(u_1[i-1]+m_31)+f_v(x+h,w_1[i-1],w_2[i-1])*(u_2[i-1]+m_32))
            u_1.append(u_1[i-1]+(m_11+2*m_21+2*m_31+m_41)/6)
            u_2.append(u_2[i-1]+(m_12+2*m_22+2*m_32+m_42)/6)
            i=i+1
        if abs(w_1[n]-y_b)<tol:
            return [w_1,w_2]
        else:
            TK=TK-(w_1[n]-y_b)/u_1[n]
            k=k+1

def f(x,y,y_):
    a=-(y_)**2-y+math.log(x)
    return a
def f_u(x,y,y_):
    h=0.0000001
    a=(f(x,y+h,y_)-f(x,y,y_))/h
    return a
def f_v(x,y,y_):
    h=0.0000001
    a=(f(x,y,y_+h)-f(x,y,y_+h))/h
    return a
def error(a,b,y_a,y_b,n,m,tol):
    approx=nonlinearshooting(a,b,y_a,y_b,n,m,tol)
    h=(b-a)/n
    err=[]
    for i in range(n+1):
        x=a+i*h
        y=math.log(x)
        error=abs(y-approx[0][i])
        err.append([approx[0][i],error])
    return err
a=1
b=2
y_a=0
y_b=math.log(2)
n=2
m=30
tol=0.01
print(error(a,b,y_a,y_b,n,m,tol))