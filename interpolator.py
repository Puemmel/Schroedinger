"""
Script so create the potential.dat based on schroedinger.inp
"""

import numpy as np
from scipy import interpolate

def interpol(arg=None):
    """
    opens schroedinger.inp and interpolates the given Potential
    saves the calculated xy points in potential.dat
    -------
    """
    pot = []
    with open ("schroedinger.inp", "r", encoding="utf-8") as file1:
        for i in file1:
            pot.append(i.split())
        file1.close()

    xpot = []
    ypot = []
    for i in range(int(pot[5][0])):
        xpot.append(float(pot[i+6][0]))
        ypot.append(float(pot[i+6][1]))

    #interpolation
    if str(pot[4][0]) == 'linear':
        pol1 = interpolate.interp1d(xpot, ypot, kind = "linear")

    elif pot[4][0] == "polynomial":
        pol1 = interpolate.lagrange(xpot, ypot)

    elif pot[4][0] == "cspline":
        pol1 = interpolate.interp1d(xpot, ypot, kind = "cubic")

    else:
        print("Error with interpolation")

    #Create file potential.dat
    xval1 = np.linspace(float(pot[2][0]), float(pot[2][1]), int(pot[2][2]))
    potpoints = []
    potxpoints = []

    file2 = open("potential.dat", "w", encoding="utf-8")
    for i in xval1:
        potpoints.append(pol1(i))

    for i in xval1:
        potxpoints.append(i)

    for i in range(len(potpoints)):
        file2.write(str(potxpoints[i]))
        file2.write(" ")
        file2.write(str(potpoints[i]))
        file2.write('\n')

    file2.close()
