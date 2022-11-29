******************
Schrodinger solver
******************

In the first step, the schrodinger solver will read the schrodinger.inp,
which needs to contain all information necessary to solve the onedimensional 
Schrodinger equation. To achieve this, please create a file called "schrodinger,inp",
containing the following information in that order:

* 2.0 # mass
* -2.0 2.0 1999 # xMin xMax nPoint
* 1 5 # first and last eigenvalue to print
* linear # interpolation type
* 2 # nr. of interpolation points and xy declarations
* -2.0 0.0
* 2.0 0.0

Please note that it is possible to add additional Interpolation points in the 
end of the file. But this needs to be declared als well with the number of Interpolation points
and the xy declarations as in the last lines of the example data. Additionally,
line 5 needs to be modified then too, as it contains the amount of interpolation points.

In the second step, the program interpolates the given potential and saves the calculated xy points in
potential.dat. 
Afterwards the schrodinger_solver will use the schrodinger.inp and the calculated potential,
saved in the potential.dat, to solve the schroedinger equation with the interpolated potential via eigenvalue problem.
It will then return the following files:

* wavefuncs.dat
* energies.dat
* expvalues.dat

If the Inputfile was created according to the example above,
the solver should create these files while the user ist calling 
the schrodinger_solver.py.

The script schrodinger_solver.py can also be called by commandline
with the addition "-p" or "--path" to change the directory you want to work in.
If the directory is to be changed, please make sure that it consists an file
called schrodinger.inp with the necessary information as well.
Otherwise the script will be stopped.

To test the functionality of the program, six example-files were created according to 
the all.dat and saved in six different case-folders (Case1/ - Case6/).
It contains schrodinger.inp files for six different cases and it will 
test the functionality of the potential.dat y-values and the 
expected y-values created by the schrodinger_solver.
It can be executed by calling pytest.