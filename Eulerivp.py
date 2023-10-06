# The function uses euler method to solve ivp of the form y'=f(x,y) with y(a)=ya on the interval [a,b] with N steps
# functions are defined later 
#a,b are the endpoint of the interval
#ya is the initial condition
#N is the number of steps 
import math
def eulerivp(x,a,b,ya,N):
    h=(b-a)/N
    x=a
    y=ya
    for i in range(N):
        y=y+h*f(x,y)
        x=x+h
    return (x,y)
#question 3
#def f(x,y):
    a=y*math.log(y)
    b=x
    result=a/b
    return result
#question 4
def f(x,y):
    a=y
    b=x
    return a-b

#def f(x,y):
    a=y**2
    b=x
    c=2*a*b
    return c
x=1
a=0
b=1
N=50
ya=0.5
print(eulerivp(x,a,b,ya,N))