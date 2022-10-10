import numpy as np
import matplotlib.pyplot as plt
import os
from scipy import linalg
import scipy.interpolate as interpolate
import math

 

def schroedinger_solver():
    """
    solves the schroedinger equation with the interpolated potential via eigenvalue problem.
    
    -------
    returns wavefuncs.dat
            energies.dat
            expvalues.dat
    
    
    """

    f = open("schroedinger.inp", "r")
    inp = []
    for x in f:
        inp.append(x.split())
    f.close() 
    
    
    #def some constants and trimatrix diagonals
    
    m = float(inp[0][0])
    delta = (float(inp[1][1]) - float(inp[1][0]))/int(inp[1][2])    
    n = int(inp[1][2])
    a = 1/(m*delta**2)
    
    
    
    diag = np.empty(n, dtype = float)
    offdiag = np.full(n-1, -0.5*a)
    
    
    f1 = open("potential.dat", "r")
    inppot = []
    for y in f1:
        inppot.append(y.split())
    f1.close()
    
    for i in range(n):
        inppot[i][0] = float(inppot[i][0])
        inppot[i][1] = float(inppot[i][1])
    
    
    for i in range(n):
        diag[i] = inppot[i][1] + a
    
    #Calculate eigenvalues and normed eigenvectormatrix in an array
    
    eigenvalues,eigenvectormatrix = linalg.eigh_tridiagonal(diag, offdiag)
    
   
    x = np.linspace(float(inp[1][0]), float(inp[1][1]), int(inp[1][2]))
    d = [[] for x in range(int(inp[2][0]),int(inp[2][1]) + 1)]
    
    
    abssquaremat = abs(eigenvectormatrix)**2
    redsquamat = np.empty((n,len(d)), dtype=(float))
    
    for j in range(len(d)):
        for i in range(n):
            redsquamat[i][j] = abssquaremat[i][j]

    

    normat = np.sum(redsquamat, axis=0) * delta
  
    for j in range(len(d)):
        for i in range(n):
            d[j].append(eigenvectormatrix[i][j]/math.sqrt(normat[j]))
   
    
    f2 = open("wavefuncs.dat", "w")
    for i in range(len(x)):
        f2.write(str(x[i]))
        for j in range(len(d)):
            f2.write(" ")
            f2.write(str(d[j][i]))
        f2.write("\n")
    f2.close()
         
    
    
    f3 = open("energies.dat", "w")
    for i in range(int(inp[2][0]) - 1,int(inp[2][1])):
        f3.write(str(eigenvalues[i]))
        f3.write("\n")
    f3.close()
    

    
    # calculate ortsop and sigma
    
    expx = [[] for i in range(len(d))]
    expxx = [[] for i in range(len(d))]
    
    for j in range(len(d)):
        for i in range(n):
            k = d[j][i] * x[i] * d[j][i] 
            l = d[j][i] * (x[i])**2 * d[j][i] 
            expxx[j].append(l)
            expx[j].append(k)
        

    for j in range(len(d)):
        expx[j] = delta * sum(expx[j])
        expxx[j] = delta * sum(expxx[j])
   
   
    sigma = []
    for i in range(len(expx)):
        sigma.append(math.sqrt(expxx[i] - (expx[i])**2))
    

    #first sigma then x op. value
    f4 = open("expvalues.dat", "w")
    for i in range(len(sigma)):
        f4.write(str(sigma[i]))
        f4.write(" ")
        f4.write(str(expx[i]))
        f4.write("\n")
    f4.close()
    
    
  
