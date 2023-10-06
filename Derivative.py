import math
#f(x)=lnx at x_0=1.8 using h=0.1 h=0.05 and h=0.01
def derivative(x,h):
    f_x1=f(x+h)
    f_x=f(x)
    return (f_x1-f_x)/h

def f(x):
    return math.log(x)


def Error(derivative,x):
    a=1/x
    b=a-derivative
    return  abs(b)

x=1.8
h=[0.1,0.05,0.01]
for i in h:
    print("h=",i,"derivative=",derivative(x,i))
    print("Error=",Error(derivative,x))

print("Error=",Error(x))