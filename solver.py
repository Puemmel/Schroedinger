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
    
    
    m = float(inp[0][0])
    delta = (float(inp[1][1]) - float(inp[1][0]))/int(inp[1][2])    
    n = int(inp[1][2])
    a = 1/(m*delta**2)

    diag = np.empty(n, dtype = float)
    offdiag = np.full(n-1, -0.5*a)
    
    f2 = open("potential.dat", "r")
    inppot = []
    for y in f2:
        inppot.append(y.split())
    f2.close() 
    
    for i in range(n):
        diag[i] = inppot[i][1]
    
    eigenvalues,eigenvectormatrix = linalg.eigh_tridiagonal(diag, offdiag)
    
    x = np.linspace(float(inp[1][0]), float(inp[1][1]), int(inp[1][2]))
    d = [[] for x in range(int(inp[2][0]),int(inp[2][1]) + 1)]
    
    
    

    quamatrix = np.empty((n, n))
    for j in range(n):
        for i in range(n):
            quamatrix[j][i] = (abs(eigenvectormatrix[j][i])**2)

    normmat = np.sum(quamatrix, axis=1)
    


    for j in range(len(d)):
        for i in range(n):
            d[j].append(delta/(normmat[j]) * eigenvectormatrix[i][j])
   
    
    
    
    
    
    
    wavexpoints = []
    for i in x:
        wavexpoints.append(i)
    
    
    f2 = open("wavefuncs.dat", "w")
    for i in range(len(wavexpoints)):
        f2.write(str(wavexpoints[i]))
        for j in range(len(d)):
            f2.write(" ")
            f2.write(str(d[j][i]))
        f2.write("\n")
    f2.close()
    
    
    
    
    
    
    f3 = open("energies.dat", "w")
    for i in range(int(inp[2][0]),int(inp[2][1]) + 1):
        f3.write(str(eigenvalues[i]))
        f3.write("\n")
    f3.close()
    
    
    
    
    
    
    
    # calculate ortsop and sigma
    
    expx = [[] for i in range(len(d))]
    expxx = [[] for i in range(len(d))]
    
    for j in range(len(d)):
        for i in range(n):
            k = d[j][i] * wavexpoints[i] * d[j][i] 
            expx[j].append(k)
            
    
    for j in range(len(d)):
        for i in range(n):
            k = d[j][i] * (wavexpoints[i])**2 * d[j][i] 
            expxx[j].append(k)

    for j in range(len(d)):
        expx[j] = delta * sum(expx[j])
        expxx[j] = delta * sum(expxx[j])
   
    
   
    sigma = []
    for i in range(len(expx)):
        sigma.append(math.sqrt(expxx[i] - (expx[i])**2))
    
    
    
    
    
    f4 = open("expvalues.dat", "w")
    for i in range(len(sigma)):
        f4.write(str(sigma[i]))
        f4.write("\n")
    f4.close()
    
    
    
