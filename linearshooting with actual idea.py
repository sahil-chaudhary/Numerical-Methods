import math
def linearshooting(a,b,y_a,y_b,n):
    h=(b-a)/n
    y=[]#save the solution of ODE using y1 and y2
    y1_b=IVP1(a,b,y_a,n**5) #y(a)=y_a,y'(a)=0 to get y(b) in this problem
    y2_b=IVP2(a,b,0,n**5) #y(a)=0,y'(a)=1 to get y(b) in this problem
    for i in range(n+1):
        x=a+i*h
        y_x=IVP1(a,x,y_a,(i+1)*n**5)+(y_b-y1_b)/y2_b*IVP2(a,x,0,(i+1)*n**5)
        y.append(y_x)
    return y

def IVP1(a,b,y_a,n): #use rungekuttaorder 4 for higher order differential equation of order 2
    h=(b-a)/n
    w1=[]
    w2=[]
    w1.append(y_a)
    w2.append(0)
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

def IVP2(a,b,y_a,n): #use rungekuttaorder 4 for higher order differential equation of order 2
    h=(b-a)/n
    w1=[]
    w2=[]
    w1.append(0)
    w2.append(1)
    k1=[[],[]]
    k2=[[],[]]
    k3=[[],[]]
    k4=[[],[]]
    for i in range(n+1):
        x=a+i*h
        k1[0].append(h*w2[i])
        k1[1].append(h*g(x,w1[i],w2[i]))
        k2[0].append(h*(w2[i]+k1[0][i]/2))
        k2[1].append(h*g(x+h/2,w1[i]+k1[0][i]/2,w2[i]+k1[1][i]/2))
        k3[0].append(h*(w2[i]+k2[1][i]/2))
        k3[1].append(h*g(x+h/2,w1[i]+k2[0][i]/2,w2[i]+k2[1][i]/2))
        k4[0].append(h*(w2[i]+k3[1][i]))
        k4[1].append(h*g(x+h,w1[i]+k3[0][i],w2[i]+k3[1][i]))  
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
    y=linearshooting(a,b,y_a,y_b,n)
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



