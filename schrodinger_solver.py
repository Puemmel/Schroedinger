"""
Solving the 1D schrodinger-equation
"""
import sys
import math
import numpy as np
from scipy import interpolate
from scipy import linalg

arg = "Case3/"

def read_schrodingerinp(arg):
    """
    reads schroedinger.inp and puts the content into three seperate lists

    Returns the content, x values, y values for the Interpolation
    """
    a_arg = arg + "schrodinger.inp"
    pot = []
    with open (a_arg, "r", encoding="utf-8") as file1:
        for i in file1:
            pot.append(i.split())
        file1.close()

    xpot = []
    ypot = []
    for i in range(int(pot[4][0])):
        xpot.append(float(pot[i+5][0]))
        ypot.append(float(pot[i+5][1]))

    return pot, xpot, ypot

def read_potentialdat(arg):
    """
    reads the potential.dat and puts the content into a list

    Returns list
    """
    b_arg = arg + "potential.dat"
    inppot = []
    with open(b_arg, "r", encoding="utf-8") as file2:
        for i in file2:
            inppot.append(i.split())
        file2.close()

    return inppot

def schrodinger_interpol(arg):
    """
    interpolates the given Potential
    -------
    Returns y values of the interpolated potential
    """
    pot, xpot, ypot = read_schrodingerinp(arg)

    if str(pot[3][0]) == 'linear':
        pol1 = interpolate.interp1d(xpot, ypot, kind = "linear")

    elif str(pot[3][0]) == "polynomial":
        pol1 = interpolate.lagrange(xpot, ypot)

    elif str(pot[3][0]) == "cspline":
        pol1 = interpolate.CubicSpline(xpot, ypot, bc_type='natural')

    else:
        print("Error with interpolation")
        sys.exit('Aborting')

    return pol1

def writepotential(arg) -> list:
    """
    saves the calculated xy points in potential.dat
    """
    pot, xpot, ypot = read_schrodingerinp(arg)
    pol1 = schrodinger_interpol(arg)
    xval1 = np.linspace(float(pot[1][0]), float(pot[1][1]), int(pot[1][2]))
    potpoints = []
    potxpoints = []
    ppoints = []
    b_arg = arg + "potential.dat"
    with open(b_arg, "w", encoding="utf-8") as file2:
        for i in xval1: 
            potpoints.append(pol1(i))
            potxpoints.append(i)
        for i, potpoint in enumerate(potpoints):
            ppoints.append(float(potpoint))
            file2.write(str(potxpoints[i]))
            file2.write(" ")
            file2.write(str(potpoint))
            file2.write('\n')
    file2.close()
    return ppoints

def schrodinger_solver(arg):
    """
    solves the schroedinger equation with the interpolated potential via eigenvalue problem.

    and calculates wavefunctions, x-operator and sigma
    """
    inp, xpot, ypot = read_schrodingerinp(arg)

    #def some constants and trimatrix diagonals
    mass1 = float(inp[0][0])
    delta1 = (float(inp[1][1]) - float(inp[1][0]))/int(inp[1][2])
    npoints = int(inp[1][2])
    res1 = 1/(mass1*delta1**2)

    diag = np.empty(npoints, dtype = float)
    offdiag = np.full(npoints-1, -0.5*res1)

    inppot = read_potentialdat(arg)

    for i in range(npoints):
        inppot[i][0] = float(inppot[i][0])
        inppot[i][1] = float(inppot[i][1])
    for i in range(npoints):
        diag[i] = inppot[i][1] + res1

    eigenvalues,eigenvectormatrix = linalg.eigh_tridiagonal(diag, offdiag)

    xval1 = np.linspace(float(inp[1][0]), float(inp[1][1]), int(inp[1][2]))

    solutionmat = eigenvectormatrix[0:int(inp[1][2]),0:int(inp[2][1])]
    solutionmat = abs(solutionmat)**2
    solutionmat = np.sum(solutionmat, axis=0) * delta1
    solution = np.empty((int(inp[1][2]),int(inp[2][1])), dtype=(float))

    for j in range(int(inp[2][1])):
        for i in range(int(inp[1][2])):
            solution[i][j] = eigenvectormatrix[i][j]/math.sqrt(solutionmat[j])

    # calculate ortsop and sigma
    expx = np.empty((int(inp[1][2]),int(inp[2][1])))
    sigma = np.empty((int(inp[1][2]),int(inp[2][1])))

    for j in range(int(inp[2][1])):
        for i in range(int(inp[1][2])):
            expx[i][j] = solution[i][j]*xval1[i]*solution[i][j]
            sigma[i][j] = solution[i][j]*(xval1[i])**2*solution[i][j]

    for j in range(int(inp[2][1])):
        expx[:,j] = delta1 * np.sum(expx[:,j],axis=0)
        sigma[:,j] = delta1 * np.sum(sigma[:,j],axis=0)

    for j in range(int(inp[2][1])):
        sigma[0][j] = math.sqrt(sigma[0][j] - (expx[0][j])**2)

    return solution, eigenvalues, sigma, expx, xval1

def writeplotdata(arg):
    """
    returns wavefuncs.dat
            energies.dat
            expvalues.dat
    """
    inp, xpot, ypot = read_schrodingerinp(arg)
    solution, eigenvalues, sigma, expx, xval1 = schrodinger_solver(arg)

    c_arg = arg + "wavefuncs.dat"
    with open(c_arg, "w", encoding="utf-8") as file3:
        for i in range(int(inp[1][2])):
            file3.write(str(xval1[i]))
            for j in range(int(inp[2][1])):
                file3.write(" ")
                file3.write(str(solution[i][j]))
            file3.write("\n")
        file3.close()

    d_arg = arg + "energies.dat"
    with open(d_arg, "w", encoding="utf-8") as file4:
        for i in range(int(inp[2][0]) - 1,int(inp[2][1])):
            file4.write(str(eigenvalues[i]))
            file4.write("\n")
        file4.close()

    e_arg = arg + "expvalues.dat"
    with open(e_arg, "w", encoding="utf-8") as file5:
        for i in range(int(inp[2][1])):
            file5.write(str(sigma[0][i]))
            file5.write(" ")
            file5.write(str(expx[0][i]))
            file5.write("\n")
        file5.close()

read_schrodingerinp(arg)
schrodinger_interpol(arg)
writepotential(arg)
schrodinger_solver(arg)
writeplotdata(arg)
