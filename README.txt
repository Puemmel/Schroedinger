*******************************
1D-SCHROEDINGER-Equation Solver
*******************************

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
you have to run schrodinger_solver.py.
It will calculate all the values and save them in four different files:

-energies.dat
-expvalues.dat
-potential.dat
-wavefuncs.dat

After the schrodinger_solver.py was executed,
the following values can be plotted, if the schrodinger_plotter.py is run.

-the potential
-the eigenvalues
-the wavefunctions
-the expected values for the eigenvalues

You can find additional information in the API-Documentation within
the folder docs/_build/html. Open the index.html to get
to the overview and choose the module you want to read about.

The Folders with the Cases 1-6 consist of reference-files
to perform the pytest on the program.