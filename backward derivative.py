import math
"""The function uses backward difference formula to calculate the derivative of a function at a point x"""
def derivative(x,h):
    f_x=f(x)
    f_xh=f(x-h)
    return (f_x-f_xh)/h

def f(x):
    return math.log(x)

def actaul(x):
    return 1/x
x=1.8
h=[0.1,0.05,0.01]
for i in h:
    print("h=",i,"derivative=",derivative(x,i))
    print("Error=",abs(actaul(x)-derivative(x,i)))
