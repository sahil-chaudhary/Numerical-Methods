import math
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
def composite_trapezoid(a,b,n):
    h=(b-a)/n
    i=0
    y=[]
    while i<=n:
        y.append(a+i*h)
        i+=1   
    j=0
    sum=0
    while j<=n-1:
        x=y[j]
        z=y[j+1]
        f_0=F(x)
        f_1=F(z)
        error=-(6*((y[j+1]-y[j])/2)**3)/12
        sum+=(f_0+f_1)*(z-x)/2+error
        j+=1
    return sum
def composite_midpoint(a,b,n):
    h=(b-a)
    h=h/n
    y=[]
    i=0
    while i<=n:
        y.append(a+h*i)
        i+=1
    sum=0
    i=0
    while i<=n-1:
        mid=(y[i]+y[i+1])/2
        f_x=F(mid)
        diff=y[i+1]-y[i]
        sum+=f_x*diff
        i+=1
    return sum
def composite_multiple_simpson(a,b,c,d,n,m):
    h=(b-a)/n
    k=(d-c)/m
    i=0
    j=0
    y=[]
    z=[]
    while i<=m:
        z.append(c+i*k)
        i+=1
    while j<=n:
        y.append(a+j*h)
        j+=1
    #for f(x,y_0)


def F(x):
    a=math.sin(x)
    b=a*x
    return b
a=0
b=math.pi/2
n=2
print(composite_simpson(a,b,n))