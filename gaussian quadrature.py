import math
def gausian_quadrature(a,b,n):
    h=(b-a)/n
    i=0
    y=[]
    while i<=n:
        y.append(a+i*h)
        i+=1
    j=0
    sum=0
    #compute c_i's and f(x_i)'s
    while j<=n or i>1:
        z=abs(composite_simpson(y[i-2],y[i-1],n)) #computing the integral of legendre polynomial
        g_i=g(y[j])
        sum+=g_i*z
        j+=1
        i-=1
    return sum

def composite_simpson(a,b,n):
    h=(b-a)/n
    i=0
    y=[]
    while i<=n:
        y.append(a+i*h)
        i+=1
    j=0
    sum=0
    while j<=n-1:
        mid=(y[j]+y[j+1])/2
        diff=(y[j+1]-y[j])/6
        x=y[j]
        z=y[j+1]
        f_0=F(x)
        f_1=F(mid)
        f_2=F(z)
        sum+=(f_0+4*f_1+f_2)*diff
        j+=1
    return sum

def F(x): #compute legendre integration at x_j's
    a=3*x**2-1
    b=0.5*(math.sqrt(5/2))
    return a*b

def g(x):
    a=math.sin(x)
    b=a*x
    return b

print(gausian_quadrature(0,math.pi/2,2))