"""
Using input-file and potential.dat to create the wavefunctions, energies and expected values
"""
import math
import numpy as np
from scipy import linalg

def schrodinger_solver(arg):
    """
    solves the schroedinger equation with the interpolated potential via eigenvalue problem.
    -------
    returns wavefuncs.dat
            energies.dat
            expvalues.dat
    """
    a = arg + "schrodinger.inp"
    with open(a, "r", encoding="utf-8") as file1:
        inp = []
        for i in file1:
            inp.append(i.split())
        file1.close()

    #def some constants and trimatrix diagonals
    mass1 = float(inp[0][0])
    delta1 = (float(inp[1][1]) - float(inp[1][0]))/int(inp[1][2]) 
    npoints = int(inp[1][2]) 
    res1 = 1/(mass1*delta1**2)

    diag = np.empty(npoints, dtype = float)
    offdiag = np.full(npoints-1, -0.5*res1)

    inppot = []

    b = arg + "potential.dat"
    with open("potential.dat", "r", encoding="utf-8") as file2:
        for i in file2:
            inppot.append(i.split())
        file2.close()

    for i in range(npoints):
        inppot[i][0] = float(inppot[i][0])
        inppot[i][1] = float(inppot[i][1])
    for i in range(npoints):
        diag[i] = inppot[i][1] + res1 

    eigenvalues,eigenvectormatrix = linalg.eigh_tridiagonal(diag, offdiag)

    xval1 = np.linspace(float(inp[1][0]), float(inp[1][1]), int(inp[1][2]))
    list1 = [[] for xval1 in range(int(inp[2][0]),int(inp[2][1]) + 1)]

    abssquaremat = abs(eigenvectormatrix)**2 
    redsquamat = np.empty((npoints,len(list1)), dtype=(float)) 

    redsquamat= np.array(abssquaremat) 

    normat = np.sum(redsquamat, axis=0) * delta1

    for j, item in enumerate(list1):
        for i in range(npoints):
            item.append(eigenvectormatrix[i][j]/math.sqrt(normat[j]))

    c = arg + "wavefuncs.dat"
    with open(c, "w", encoding="utf-8") as file3:
        for i, elem in enumerate(xval1):
            file3.write(str(elem))
            for j, k in enumerate(list1):
                file3.write(" ")
                file3.write(str(k[i]))
            file3.write("\n")
        file3.close()

    d = arg + "energies.dat"
    with open(d, "w", encoding="utf-8") as file4:
        for i in range(int(inp[2][0]) - 1,int(inp[2][1])):
            file4.write(str(eigenvalues[i]))
            file4.write("\n")
        file4.close()

    # calculate ortsop and sigma
    expx = [[] for i in range(len(list1))]
    expxx = [[] for i in range(len(list1))]

    for j, _ in enumerate(list1):
        for i in range(npoints):
            k = _[i] * xval1[i] * _[i]
            sig = _[i] * (xval1[i])**2 * _[i]
            expxx[j].append(sig)
            expx[j].append(k)

    for j, _ in enumerate(list1):
        expx[j] = delta1 * sum(expx[j])
        expxx[j] = delta1 * sum(expxx[j])

    sigma = [] #Wurzel aus 
    for i, _ in enumerate(expx):
        sigma.append(math.sqrt(expxx[i] - (_)**2))

    #first sigma then x op. value
    e = arg + "expvalues.dat"
    with open(e, "w", encoding="utf-8") as file5:
        for i, _ in enumerate(sigma):
            file5.write(str(_))
            file5.write(" ")
            file5.write(str(expx[i]))
            file5.write("\n")
        file5.close()
    