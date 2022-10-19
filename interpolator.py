import numpy as np
import scipy.interpolate as interpolate

def interpol(arg=None):
    """
    opens schroedinger.inp and interpolates the given Potential
    saves the calculated xy points in potential.dat
    -------
    """
    f = open("schroedinger.inp", "r")

    pot = []
    for i in f:
        pot.append(i.split())
    f.close() 

    xpot = []
    ypot = []
    for i in range(int(pot[5][0])):
        xpot.append(float(pot[i+6][0]))
        ypot.append(float(pot[i+6][1]))
        
    #interpolation
    if str(pot[4][0]) == 'linear':
        z = interpolate.interp1d(xpot, ypot, kind = "linear")
        
    elif pot[4][0] == "polynomial":
        z = interpolate.lagrange(xpot, ypot)
        
    elif pot[4][0] == "cspline":
        z = interpolate.interp1d(xpot, ypot, kind = "cubic")
        
    else:
        print("Error with interpolation")
        pass

    #Create file potential.dat    
    x = np.linspace(float(pot[2][0]), float(pot[2][1]), int(pot[2][2]))
    potpoints = []
    potxpoints = []
 
    f2 = open("potential.dat", "w")
    for i in x:
        potpoints.append(z(i))
    
    for i in x:
        potxpoints.append(i)
    
    for i in range(len(potpoints)):
        f2.write(str(potxpoints[i]))
        f2.write(" ")
        f2.write(str(potpoints[i]))        
        f2.write('\n')
        
    f2.close()  
