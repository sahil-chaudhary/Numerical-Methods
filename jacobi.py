import numpy as np
def jacobimethod(A,B):
    """Solves the linear system of equations Ax = B using the Jacobi method. A and B must be numpy matrix"""
    n = A.shape[0]
    x = np.zeros((n,1))
    xold = np.zeros((n,1))
    xnew = np.zeros((n,1))
    tol = 1e-10
    maxiter = 1000
    for i in range(maxiter):
        for j in range(n):
            xnew[j] = B[j]
            for k in range(n):
                if k != j:
                    xnew[j] -= A[j,k]*xold[k]
            xnew[j] /= A[j,j]
            
        if np.linalg.norm(xnew-xold) < tol:
            break
        xold = xnew.copy()
    return xnew

def gausssiedelmethod(A,B):
    """Solves the linear system of equations Ax = B using the Gauss-Seidel method. A and B must be numpy matrix where A and B are of the form np.array([],[]...,[])"""
    n = A.shape[0]
    x = np.zeros((n,1))
    xold = np.zeros((n,1))
    xnew = np.zeros((n,1))
    tol = 1e-10
    maxiter = 1000
    for i in range(maxiter):

        for j in range(n):
            xnew[j] = B[j]
            k=0
            for k in range(j):
                xnew[j] -= A[j,k]*xnew[k]
            for k in range(j+1,n):
                xnew[j] -= A[j,k]*xold[k]
            xnew[j] /= A[j,j]
        if np.linalg.norm(xnew-xold) < tol:
            break
        xold = xnew.copy()
    return xnew

def gaussianelimination(A, b):
    """Solves the system of linear equations Ax = b using Gaussian elimination with back substitution.
    A and b must be numpy arrays of the same shape."""
    n=A.shape[0]
    x = np.zeros((n,1))
    augmented = np.concatenate((A,b), axis=1, dtype=float)
    for i in range(n):
        for j in range(i+1,n):
            if augmented[i,i] == 0:
                raise ValueError("The matrix is singular")
            ratio = augmented[j,i]/augmented[i,i]
            augmented[j,:] -= ratio*augmented[i,:]   
    for i in range(n-1,-1,-1):
        x[i] = augmented[i,n]/augmented[i,i]
        for j in range(i-1,-1,-1):
            augmented[j,n] -= augmented[j,i]*x[i,0]
    return x

