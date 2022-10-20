"""
Using input-file and potential.dat to create the wavefunctions, energies and expected values
"""
import math
import numpy as np
from scipy import linalg

def schroedinger_solver(arg=None):
    """
    solves the schroedinger equation with the interpolated potential via eigenvalue problem.
    -------
    returns wavefuncs.dat
            energies.dat
            expvalues.dat
    """
    with open("schroedinger.inp", "r", encoding="utf-8") as file1:
        inp = []
        for i in file1:
            inp.append(i.split())
        file1.close()

    #def some constants and trimatrix diagonals

    mass1 = float(inp[1][0])
    delta1 = (float(inp[2][1]) - float(inp[2][0]))/int(inp[2][2])
    npoints = int(inp[2][2])
    Res = 1/(mass1*delta1**2)

    diag = np.empty(npoints, dtype = float)
    offdiag = np.full(npoints-1, -0.5*Res)

    inppot = []
    with open("potential.dat", "r", encoding="utf-8") as file2:
        for i in file2:
            inppot.append(i.split())
        file2.close()

    for i in range(npoints):
        inppot[i][0] = float(inppot[i][0])
        inppot[i][1] = float(inppot[i][1])
    for i in range(npoints):
        diag[i] = inppot[i][1] + Res

    #Calculate eigenvalues and normed eigenvectormatrix in an array
    eigenvalues,eigenvectormatrix = linalg.eigh_tridiagonal(diag, offdiag)

    xval1 = np.linspace(float(inp[2][0]), float(inp[2][1]), int(inp[2][2]))
    list1 = [[] for xval1 in range(int(inp[3][0]),int(inp[3][1]) + 1)]

    abssquaremat = abs(eigenvectormatrix)**2
    redsquamat = np.empty((npoints,len(list1)), dtype=(float))

    for j in range(len(list1)):
        for i in range(npoints):
            redsquamat[i][j] = abssquaremat[i][j]

    normat = np.sum(redsquamat, axis=0) * delta1

    for j in range(len(list1)):
        for i in range(npoints):
            list1[j].append(eigenvectormatrix[i][j]/math.sqrt(normat[j]))

    with open("wavefuncs.dat", "w", encoding="utf-8") as file3:
        for i in range(len(xval1)):
            file3.write(str(xval1[i]))
            for j in range(len(list1)):
                file3.write(" ")
                file3.write(str(list1[j][i]))
            file3.write("\n")
        file3.close()

    with open("energies.dat", "w", encoding="utf-8") as file4:
        for i in range(int(inp[3][0]) - 1,int(inp[3][1])):
            file4.write(str(eigenvalues[i]))
            file4.write("\n")
        file4.close()

    # calculate ortsop and sigma
    expx = [[] for i in range(len(list1))]
    expxx = [[] for i in range(len(list1))]

    for j in range(len(list1)):
        for i in range(npoints):
            k = list1[j][i] * xval1[i] * list1[j][i]
            l = list1[j][i] * (xval1[i])**2 * list1[j][i]
            expxx[j].append(l)
            expx[j].append(k)

    for j in range(len(list1)):
        expx[j] = delta1 * sum(expx[j])
        expxx[j] = delta1 * sum(expxx[j])

    sigma = []
    for i in range(len(expx)):
        sigma.append(math.sqrt(expxx[i] - (expx[i])**2))

    #first sigma then x op. value
    with open("expvalues.dat", "w", encoding="utf-8") as file5:
        for i in range(len(sigma)):
            file5.write(str(sigma[i]))
            file5.write(" ")
            file5.write(str(expx[i]))
            file5.write("\n")
        file5.close()
    