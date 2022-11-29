*******************************
1D-SCHROEDINGER-Equation-solver
*******************************

Repository to solve the onedimensional time-independent Schroedinger Equation.
You need to create an file called "schrodinger.inp" and save it to the main folder
of the project, called "Schroedinger".

The file needs to have the following information in this order:

2.0 # mass
-2.0 2.0 1999 # xMin xMax nPoint
1 5 # first and last eigenvalue to print
linear # interpolation type
2 # nr. of interpolation points and xy declarations
-2.0 0.0
2.0 0.0

To run the calculation of the potential, energies, expected values and the wavefunctions,
you have to run the "schrodinger_solver.py".
It will calculate all the values and save them in four different files:

-energies.dat
-expvalues.dat
-potential.dat
-wavefuncs.dat

You can change the working directory by using the commandline "-p" or "--path"
and adding the directory, where you want to work in. Please keep in mind,
that the directory you plan to work in needs to contain an "schrodinger.inp" file with
the information mentioned above.

After the "schrodinger_solver.py" was executed,
the following values can be plotted, if the "schrodinger_plotter.py" is run.

-the potential
-the eigenvalues
-the wavefunctions
-the expected values for the eigenvalues

You can find additional information in the API-Documentation within
the folder:

/Schroedinger/docs/_build/html

If you open the file "index.html", you will be guided by your browser to the
table of contents, consisting of two entries with further information regarding the solver and plotter:

-schrodinger_solver
-schrodinger_plotter

In order to make sure the programm calculates the correct values for
the potential as well as the expected values, 6 different directories
were created, containing 6 different schrodinger.inp files with
examples. Also each directory is having a file called "RefPot" and "RefExp",
containing the correct x- and y-values for that special case.
It can be executed by running a "pytest".