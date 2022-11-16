*************
Main function
*************

The main function will call the functions listed below::

* Interpolator
* solver
* plotter

It will first run the Interpolator in order to read the Input-File (Schroedinger.inp)
and interpolate to create the Output-File (Potential.dat.)
Afterwards the Solver will use both files as well to solves the schroedinger equation with the interpolated potential
via eigenvalue problem. Afterwards the following files will be created:

* wavefuncs.dat
* energies.dat
* expvalues.dat

Then the main function will call the plotter script to plot the values into a graph.
