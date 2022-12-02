*******************************
1D-SCHROEDINGER-Equation-solver
*******************************

Repository to solve the onedimensional time-independent Schroedinger Equation.
The Folder containts a file called "schrodinger.inp", which looks like this for example:

2.0 # mass
-2.0 2.0 1999 # xMin xMax nPoint
1 5 # first and last eigenvalue to print
linear # interpolation type
2 # nr. of interpolation points and xy declarations
-2.0 0.0
2.0 0.0

If you want to calculate your own values, you can change the parameters.
The points and the type of interpolation of the potential are given in the last lines of Schrodinger.inp.
To solve the schrodinger equation you have to run the "schrodinger_solver.py".
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
the following values can be plotted, if you execute the "schrodinger_plotter.py".

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

If you want to make changes, go to the folder /schroedinger/docs and open the .rst files
to change them. With the command "make html" you are able to create new html files, if sphinx is installed.

In order to make sure the programm calculates the correct values for
the potential as well as the expected values, 6 different directories
were created, containing 6 different schrodinger.inp files with
examples. Also each directory is having a file called "RefPot" and "RefExp",
containing the correct x- and y-values for that special case.
By executing a "pytest", 12 tests will be done, comparing the calculated results
to the reference files.