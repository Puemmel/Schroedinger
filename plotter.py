import numpy as np
import matplotlib.pyplot as plt

def visualizer(arg=None):
    """
    plot

    """
    
    #open all necessary files an save them in lists
    
    inppot = np.loadtxt("potential.dat")
    
    inpwav = np.loadtxt("wavefuncs.dat")
        
    inpexp = np.loadtxt("expvalues.dat")

    inpeng = np.loadtxt("energies.dat")
    #convert items into floats    

    energieslist = []
    for i in range(len(inpeng)):    
        energieslist.append(float(inpeng[i][0]))
        for j in range(2):
            inpexp[i][j] = float(inpexp[i][j])
    
    potlist = []
    for i in range(len(inpwav)):
        potlist.append(float(inppot[i][1]))
        for j in range(len(inpwav[0])):
            inpwav[i][j] = float(inpwav[i][j])
    
    inpwav = np.array(inpwav)
    inpexp = np.array(inpexp)
    
    
    plt.subplot(1, 2, 1)
    plt.plot(inpwav[:,0], potlist)
    for i in range(len(inpwav[0]) - 1):
        plt.plot(inpwav[:,0], 0.2*inpwav[:,i+1] + energieslist[i])
        #plt.plot(inpwav[:,0], energieslist[i])
        
           
    plt.title('Potential, Eigenstates, <x>')
    plt.ylabel('Energy [Hartree]')
    plt.xlabel('x [Boh]')

    plt.subplot(1, 2, 2)
    plt.title('lol')
    plt.plot(inpwav[:,0], potlist)
    plt.xlabel('[Bohr]')
    
    
    plt.show()
    
visualizer()