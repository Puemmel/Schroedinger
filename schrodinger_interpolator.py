"""
Script so create the potential.dat based on schroedinger.inp
"""

import numpy as np
from scipy import interpolate

def schrodinger_interpol():
    """
    opens schroedinger.inp and interpolates the given Potential
    saves the calculated xy points in potential.dat
    -------
    """
    pot = [] 
    with open ("schrodinger.inp", "r", encoding="utf-8") as file1:
        for i in file1:
            pot.append(i.split())
        file1.close()

    xpot = []
    ypot = []
    for i in range(int(pot[4][0])):
        xpot.append(float(pot[i+5][0])) 
        ypot.append(float(pot[i+5][1])) 

    if str(pot[3][0]) == 'linear': 
        pol1 = interpolate.interp1d(xpot, ypot, kind = "linear")

    elif pot[3][0] == "polynomial":
        pol1 = interpolate.lagrange(xpot, ypot)

    elif pot[3][0] == "cspline":
        pol1 = interpolate.interp1d(xpot, ypot, kind = "cubic")

    else:
        print("Error with interpolation")

    #Create file potential.dat
    xval1 = np.linspace(float(pot[1][0]), float(pot[1][1]), int(pot[1][2]))
    potpoints = []
    potxpoints = []

    with open("potential.dat", "w", encoding="utf-8") as file2: 
        for i in xval1: 
            potpoints.append(pol1(i))
        for i in xval1:
            potxpoints.append(i)
        for i, potpoint in enumerate(potpoints): 
            file2.write(str(potxpoints[i]))
            file2.write(" ")
            file2.write(str(potpoint))
            file2.write('\n')
    file2.close()
