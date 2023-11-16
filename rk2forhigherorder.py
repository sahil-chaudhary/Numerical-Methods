import math
def rk2(a,b,y_a,h):
    #a is an array of the initial conditions
    #b is the upper bound of the interval
    #y_a is the value for each a in a.
    result=[]
    k1=[]
    k2=[]
    w=y_a
    t=a[0]
    n=int((b[0]-a[0])/h)
    for i in range(n):
        k1.append(h*f(t,w[0],w[1]))
        k1.append(h*g(t,w[0],w[1]))
        k2.append(h*f(t+h/2,w[0]+k1[0]/2,w[1]+k1[1]/2))
        k2.append(h*g(t+h/2,w[0]+k1[0]/2,w[1]+k1[1]/2))
        for j in range(len(a)):
            w[j]=w[j]+h*(k1[j]+k2[j])/2
    return w

def f(t,x,y):
    a=3*x+2*y-(((2*t)**2+1)*math.exp(2*t))
    return a

def g(t,x,y):
    b=4*x+y+(t**2+2*t-4)*math.exp(2*t)
    return b

def error(a,b,y_a,h):
    x=b[0]
    u_1=(1/3)*math.exp(5*x)-(1/3)*math.exp(-x)+math.exp(2*x)
    u_2=(1/3)*math.exp(5*x)+(2/3)*math.exp(-x)+(x**2)*math.exp(2*x)
    result=rk2(a,b,y_a,h)
    print(result)
    print(u_1,u_2)
    e_1=abs(result[0]-u_1)
    e_2=abs(result[1]-u_2)
    return [e_1,e_2]
a=[0,0]
b=[1,1]
y_a=[1,1]
h=0.2
print(error(a,b,y_a,h))