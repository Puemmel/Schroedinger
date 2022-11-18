******
solver
******

The solver ist taking the schroedinger.inp and the created potential.dat
to solve the schroedinger equation with the interpolated potential via eigenvalue problem.
It will then return the following files:

* wavefuncs.dat
* energies.dat
* expvalues.dat

If the Inputfile was created according to chapter Interpolator,
the solver should create this files while the user ist calling 
the main script.
