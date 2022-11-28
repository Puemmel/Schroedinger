"""
Opening the files created by schrodinger_solver
and plotting the values
"""
import numpy as np
import matplotlib.pyplot as plt
import argparse
import sys


def plotread():

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
    
    return energieslist, inpwav, inpexp, potlist


def schrodinger_plotter():
    """
    plots the potential, wavefunctions, energies, expected x value and sigma

    """
    energieslist, inpwav, inpexp, potlist = plotread()
    
    ampl = float(args.a)
    plt.subplot(1, 2, 1) 
    #plot energie grid
    for i, _ in enumerate(energieslist):
        plt.axhline(y=_, color='gray', linestyle='-',alpha=0.5)

    plt.plot(inpwav[:,0], potlist)
    for i in range(len(inpwav[0]) - 1):
        plt.plot(inpwav[:,0], ampl*inpwav[:,i+1] + energieslist[i])

    for i, _ in enumerate(inpexp):
        plt.plot(inpexp[i][1] , energieslist[i], "kx")
     
    if args.xmin or args.xmax or args.ymin or args.ymax is not None:
        try:    
            xmin = float(args.xmin)
            ymin = float(args.ymin)
            xmax = float(args.xmax)
            ymax = float(args.ymax)
            plt.xlim(xmin, xmax)
            plt.ylim(ymin,ymax)
        except:
            print("You have to define all parametrs xmin, xmax, ymin, ymax as numbers")
            sys.exit("Aborted")
    
    plt.title('Potential, Eigenstates, <x>')
    plt.ylabel('Energy [Hartree]')
    plt.xlabel('x [Bohr]')

    plt.subplot(1, 2, 2)
    plt.title('\u03C3')
    
    #plot energie grid
    for i, _ in enumerate(energieslist):
        plt.axhline(y=_, color='gray', linestyle='-',alpha=0.5)

    for i, _ in enumerate(inpexp):
        plt.plot(inpexp[i][0], energieslist[i], 'm+')

    plt.xlabel('[Bohr]')
    
    if args.sigmaxmin or args.sigmaxmax or args.sigmaymin or args.sigmaymax is not None:
        try:    
            xmin = float(args.sigmaxmin)
            ymin = float(args.sigmaymin)
            xmax = float(args.sigmaxmax)
            ymax = float(args.sigmaymax)
            plt.xlim(xmin, xmax)
            plt.ylim(ymin,ymax)
        except:
            print("You have to define all parametrs xmin, xmax, ymin, ymax as numbers")
            sys.exit("Aborted")
            
    plt.show()


parser = argparse.ArgumentParser()
parser.add_argument('--a', type=float, default ='1', required= False, help = "amplitude factor of the wavefunctions")

parser.add_argument('--xmin', type=float, required= False, help = "x-axes minimum for plot of the wavefunctions")
parser.add_argument('--ymin', type=float, required= False, help = "y-axes minimum for plot of the wavefunctions")
parser.add_argument('--xmax', type=float, required= False, help = "x-axes maximum for plot of the wavefunctions")
parser.add_argument('--ymax', type=float, required= False, help = "y-axes maximum for plot of the wavefunctions")

parser.add_argument('--sigmaxmin', type=float, required= False, help = "x-axes minimum of the sigma plot")
parser.add_argument('--sigmaymin', type=float, required= False, help = "y-axes minimum of the sigma plot")
parser.add_argument('--sigmaxmax', type=float, required= False, help = "x-axes maximum of the sigma plot")
parser.add_argument('--sigmaymax', type=float, required= False, help = "y-axes maximum of the sigma plot")

args = parser.parse_args()

schrodinger_plotter()