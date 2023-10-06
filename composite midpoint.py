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

def F(x):
    return x**3+5*x**2+1

a=1
b=5
n=10
print(composite_midpoint(a,b,n))        
