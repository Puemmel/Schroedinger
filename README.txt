************
SCHROEDINGER
************

Package to solve the onedimensional time-independent Schroedinger Equation.
You need to create an file called schrodinger.inp and copy it to the main folder
of the project, called Schroedinger.

The file needs to have the following information in this order:

2.0 # mass
-2.0 2.0 1999 # xMin xMax nPoint
1 5 # first and last eigenvalue to print
linear # interpolation type
2 # nr. of interpolation points and xy declarations
-2.0 0.0
2.0 0.0

To run the calculation of the potential, energies, expected Values and the wavefunctions, 
you have to run the Schrodinger.main.py.
It will calculate all the values and save them in four different files:

-energies.dat
-expvalues.dat
-potential.dat
-wavefuncs.dat

After the schrodinger.main.py was executed,
the following values can be plotted, if the Visualizer.main.py is run.

-the potential
-the eigenvalues
-the wavefunctions
-the expected values for the eigenvalues

You can find additional information in the API-Documentation within
the docs folder. 



The reference-files within the schroedinger folder, called RefExp
and RefPot are used to perform the pytest for functionality testing of
the interpolator and the solver.