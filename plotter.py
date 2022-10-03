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