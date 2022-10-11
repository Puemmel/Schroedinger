import numpy as np
import matplotlib.pyplot as plt
import os.path

answer = input("Is the file in the current path [y/n]?")

if answer != "n":
    print('getcwd:      ', os.getcwd())

else:
    file_path = input('Enter a file path: ')

    # e.g. C:\Users\Bob\Desktop\example.txt
    # or /home/Bob/Desktop/example.txt
    print(file_path)

    if os.path.exists(file_path):
        print('The file exists')

        with open(file_path, 'r', encoding='utf-8-sig') as f:
            lines = f.readlines()

            print(lines)
    else:
        print('The specified file does NOT exist')

fp = open("potential.dat","r")
pot=[]#empty list for potential
for vp in fp:
    pot.append(vp.split())

xp=[]#empty list for x-values
yp=[]#empty list for y-values

for elem in pot:
    xp.append(elem[0])
    yp.append(elem[1])

#lastxp = xp.pop() #get last value of list
#lastyp = yp.pop() #get last value of list

fe = open("expvalues.dat","r")
exp=[] #empty list for potential
for ve in fe:
    exp.append(ve.split())
fe.close

xe=[]#empty list for x-values
ye=[]#empty list for y-values

for elem in exp:
    xe.append(elem[0])
    ye.append(elem[1])
  
plt.figure(figsize=(10, 8))

plt.subplot(1,2,1,)
plt.plot(xp,yp,)

plt.xlabel("x [Bohr]")
plt.ylabel("Energy [Hartree]")
plt.title("Potential, Eigenstates,(x)")
plt.gca().invert_yaxis()

plt.subplot(1,2,2)
plt.plot(xe,ye, "*m")
plt.xlabel("[Bohr]")
plt.grid(axis = 'y', color = 'grey', linestyle = '-', linewidth = 1)
plt.title('$\sigma_x$')

plt.subplots_adjust(left=0.125,
                    bottom=0.1, 
                    right=0.9, 
                    top=0.9, 
                    wspace=0.5)

plt.show()

import numpy as np
import matplotlib.pyplot as plt
import os
import math



def visualizer():
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