*******************
Interpolator script
*******************

The interpolator script will read an Input file, which has to be named
schroedinger.inp. It needs to contain the following informations:

* 2.0 # mass
* -2.0 2.0 1999 # xMin xMax nPoint
* 1 5 # first and last eigenvalue to print
* linear # interpolation type
* 2 # nr. of interpolation points and xy declarations
* -2.0 0.0
* 2.0 0.0

It interpolates the given Potential and saves the calculated xy points in
potential.dat. 
To create the files that can used for the Visualizer. 
