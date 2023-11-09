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
            for k in range(j-1):
                xnew[j] -= A[j,k]*xnew[k]
            for k in range(j+1,n):
                xnew[j] -= A[j,k]*xold[k]
            xnew[j] /= A[j,j]
        if np.linalg.norm(xnew-xold) < tol:
            break
        xold = xnew.copy()
    return xnew
