*******************
Interpolator script
*******************

The interpolator script will read an Input file, which has to be named schroedinger.inp.
It needs to contain the following informations:

* Unendlich tiefer Potentialkopf
* 2.0 # mass
* -2.0 2.0 1999 # xMin xMax nPoint
* 1 5 # first and last eigenvalue to print
* linear # interpolation type
* 2 # nr. of interpolation points and xy declarations
* -2.0 0.0
* 2.0 0.0

It interpolates the given Potential and saves the calculated xy points in potential.dat.
The header will be used in the testing functions, to check if 
reference-files are available and therefore the testing functions can be performed using pytest.
