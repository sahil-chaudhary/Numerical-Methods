import math
"""This function calculates the central derivative of a function f(x) at a point x using a step size h."""
def centralderivative(x,h):
    return (f(x+h)-f(x-h))/(2*h)

def f(x):
    return math.log(x)

x=1.8
h=[0.1,0.05,0.01]
for i in h:
    print("h=",i,"derivative=",centralderivative(x,i))
    print("Error=",abs(1/x-centralderivative(x,i)))