import numpy as np
import matplotlib.pyplot as plt

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
exp=[]#empty list for potential
for ve in fe:
   exp.append(ve.split())
fe.close

xe=[]#empty list for x-values
ye=[]#empty list for y-values

for elem in exp:
  xe.append(elem[0])
  ye.append(elem[1])

plt.subplot(1,2,1)
plt.plot(xp,yp)

plt.xlabel("x [Bohr]")
plt.ylabel("Energy [Hartree]")

plt.subplot(1,2,2)
plt.plot(xe,ye, "*m")

plt.xlabel("[Bohr]")
plt.grid(axis = 'y', color = 'grey', linestyle = '-', linewidth = 0.5)
plt.show()