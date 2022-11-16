import schrodinger_plotter as pt
import numpy as np
  #open all necessary files an save them in lists

counter = 0
while counter == 0:

  ans = input("Do you want the plot as default or your own settings? [d/s]")
  if ans == "d":
    value = False
    ampl = 1
    counter = 1
  elif ans == "s":
    value = True
    counter = 1

  print("Please enter your values for the x and y axis for both plots as floats")
  try:
    xmin = float(input("xmin:"))
    xmax = float(input("xmax:"))
    ymin = float(input("ymin:"))
    ymax = float(input("ymax:"))
    sigmaxmin = float(input("sigmaxmin:"))
    sigmaxmax = float(input("sigmaxmax:"))
    sigmaymin = float(input("sigmaymin:"))
    sigmaymax = float(input("sigmaymax:"))
    ampl = float(input("amplitude of the wavefunc:"))
  except ValueError:
    print("It seems like you havent entered a float")
    print("The graph will be printed with default settings")
    value = False
    ampl = 1
    counter = 1
  else:
    print("Youre input is not correct. Please repeat")
    counter = 0

pt.schrodinger_plotter()