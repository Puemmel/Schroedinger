import numpy as np
import matplotlib.pyplot as plt

def visualizer(arg=None):
    """
    plots the potential, wavefunctions, energies, expected x value and sigma
    
    """
    
    #open all necessary files an save them in lists
    
    inppot = np.loadtxt("potential.dat")
    
    inpwav = np.loadtxt("wavefuncs.dat")
        
    inpexp = np.loadtxt("expvalues.dat")

    inpeng = np.loadtxt("energies.dat")
    
    
    #convert items into floats    

    energieslist = []
    for i in range(len(inpeng)):    
        energieslist.append(float(inpeng[i]))
        for j in range(2):
            inpexp[i][j] = float(inpexp[i][j])
    
    potlist = []
    for i in range(len(inpwav)):
        potlist.append(float(inppot[i][1]))
        for j in range(len(inpwav[0])):
            inpwav[i][j] = float(inpwav[i][j])
    
    inpwav = np.array(inpwav)
    inpexp = np.array(inpexp)
    
    
    #ask user if he wants to manipulate the plot
    t = 0
    while t == 0:
        
        ans = input("Do you want the plot as default or your own settings? [d/s]")
        if ans == "d":
            value = False
            ampl = 1
            t = 1
        elif ans == "s":
            value = True
            t = 1
            
            print("Please enter your values for the x and y axis for both plots")
            xmin = float(input("xmin:"))
            xmax = float(input("xmax:"))
            ymin = float(input("ymin:"))
            ymax = float(input("ymax:"))
            
            sigmaxmin = float(input("sigmaxmin:"))
            sigmaxmax = float(input("sigmaxmax:"))
            sigmaymin = float(input("sigmaymin:"))
            sigmaymax = float(input("sigmaymax:"))
        
            ampl = float(input("amplitude of the wavefunc:"))
        else:
            print("Youre input is not correct. Please repeat")
            t = 0
    
    plt.subplot(1, 2, 1)
    if value:
        plt.xlim(xmin, xmax)
        plt.ylim(ymin,ymax)
    
    #plot energie grid
    for i in range(len(energieslist)):
        plt.axhline(y=energieslist[i], color='gray', linestyle='-',alpha=0.5)
         
    
    plt.plot(inpwav[:,0], potlist)
    for i in range(len(inpwav[0]) - 1):
        plt.plot(inpwav[:,0], ampl*inpwav[:,i+1] + energieslist[i])
    
    for i in range(len(inpexp)):
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
    for i in range(len(energieslist)):
        plt.axhline(y=energieslist[i], color='gray', linestyle='-',alpha=0.5)
         
    
    for i in range(len(inpexp)):
        plt.plot(inpexp[i][0], energieslist[i], 'm+')
    
    plt.xlabel('[Bohr]')
    
   
    
    plt.show()