import math
def trapeinteg(a,b):
    """The function takes the lower and upper limit of the integral and returns the integral of the function f(x)=(1+x^2)^(1/2) using the trapezoidal rule."""
    h=b-a
    f_a=math.sqrt(1+a**2)
    f_b=math.sqrt(1+b**2)
    return h*(f_a+f_b)/2+error

print(trapeinteg(1,5))