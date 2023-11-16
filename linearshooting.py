import math
def linearshooting(a,b,y_a,y_b,n):
    h=(b-a)/n
    u_1=[y_a]
    u_2=[0]
    v_1=[0]
    v_2=[1]
    for i in range(n+1):
        x=a+i*h
        k_11=h*u_2[i]
        k_12=h*(p(x)*u_2[i]+q(x)*u_1[i]+r(x))
        k_21=h*(u_2[i]+0.5*k_12)
        k_22=h*(p(x+h/2)*(u_2[i]+0.5*k_12)+q(x+h/2)*(u_1[i]+0.5*k_11)+r(x+h/2))
        k_31=h*(u_2[i]+0.5*k_22)
        k_32=h*(p(x+h/2)*(u_2[i]+0.5*k_22)+q(x+h/2)*(u_1[i]+0.5*k_21)+r(x+h/2))
        k_41=h*(u_2[i]+k_32)
        k_42=h*(p(x+h)*(u_2[i]+k_32)+q(x+h)*(u_1[i]+k_31)+r(x+h))
        u_1.append(u_1[i]+(k_11+2*k_21+2*k_31+k_41)/6)
        u_2.append(u_2[i]+(k_12+2*k_22+2*k_32+k_42)/6)
        m_11=h*v_2[i]
        m_12=h*(p(x)*v_2[i]+q(x)*v_1[i])
        m_21=h*(v_2[i]+0.5*m_12)
        m_22=h*(p(x+h/2)*(v_2[i]+0.5*m_12)+q(x+h/2)*(v_1[i]+0.5*m_11))
        m_31=h*(v_2[i]+0.5*m_22)
        m_32=h*(p(x+h/2)*(v_2[i]+0.5*m_22)+q(x+h/2)*(v_1[i]+0.5*m_21))
        m_41=h*(v_2[i]+m_32)
        m_42=h*(p(x+h)*(v_2[i]+m_32)+q(x+h)*(v_1[i]+m_31))
        v_1.append(v_1[i]+(m_11+2*m_21+2*m_31+m_41)/6)
        v_2.append(v_2[i]+(m_12+2*m_22+2*m_32+m_42)/6)
    w_1=y_a
    w_2=(y_b-u_1[n])/v_1[n]
    W_1=[]
    W_2=[]
    ans=[]
    for i in range(n+1):
        x=a+i*h
        W_1.append(u_1[i]+w_2*v_1[i])
        W_2.append(u_2[i]+w_2*v_2[i])
    return [W_1,W_2]
def p(x):
    return 0
def q(x):
    return 4
def r(x):
    value=-4*x
    return value
def error(a,b,y_a,y_b,n):
    h=(b-a)/n
    y=linearshooting(a,b,y_a,y_b,n)
    print(y)
    actual=[]
    error=[]
    for i in range(n+1):
        x=a+(i)*h
        actual.append(math.exp(2)/(math.exp(4)-1)*(math.exp(2*x)-math.exp(-2*x))+x)
        error.append(abs(actual[i]-y[0][i]))
    print(actual)
    return error
a=0
b=1
y_a=0
y_b=2
n=10
y=error(a,b,y_a,y_b,n)
print(y)