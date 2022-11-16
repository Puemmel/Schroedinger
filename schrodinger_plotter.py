"""
Uses the files created beforehand to plot the values
"""
import numpy as np
import matplotlib.pyplot as plt

inppot = np.loadtxt("potential.dat")
inpwav = np.loadtxt("wavefuncs.dat")
inpexp = np.loadtxt("expvalues.dat")
inpeng = np.loadtxt("energies.dat")

energieslist = [] 
for i, _ in enumerate(inpeng): 
    energieslist.append(float(inpeng[i]))
    for j in range(2):
        inpexp[i][j] = float(inpexp[i][j])

potlist = [] 
for i, _ in enumerate(inpwav):
    potlist.append(float(inppot[i][1]))
    for j in range(len(inpwav[0])):
        inpwav[i][j] = float(inpwav[i][j])
    
    inpwav = np.array(inpwav)
    inpexp = np.array(inpexp)

def schrodinger_plotter():
    """
    plots the potential, wavefunctions, energies, expected x value and sigma

    """
    #convert items into floats

    plt.subplot(1, 2, 1)
    if value:
        plt.xlim(xmin, xmax)
        plt.ylim(ymin,ymax)

    #plot energie grid
    for i, _ in enumerate(energieslist):
        plt.axhline(y=_, color='gray', linestyle='-',alpha=0.5)

    plt.plot(inpwav[:,0], potlist)
    for i in range(len(inpwav[0]) - 1):
        plt.plot(inpwav[:,0], ampl*inpwav[:,i+1] + energieslist[i])

    for i, _ in enumerate(inpexp):
        plt.plot(inpexp[i][1] , energieslist[i], "kx")

    plt.title('Potential, Eigenstates, <x>')
    plt.ylabel('Energy [Hartree]') 
    plt.xlabel('x [Bohr]') 

    plt.subplot(1, 2, 2)
    plt.title('\u03C3')
    if value:
        plt.xlim(sigmaxmin, sigmaxmax)
        plt.ylim(sigmaymin,sigmaymax)

    #plot energie grid
    for i, _ in enumerate(energieslist):
        plt.axhline(y=_, color='gray', linestyle='-',alpha=0.5)

    for i, _ in enumerate(inpexp):
        plt.plot(inpexp[i][0], energieslist[i], 'm+')

    plt.xlabel('[Bohr]')

    plt.show()
