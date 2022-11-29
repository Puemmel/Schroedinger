*******************
Schrodinger_plotter
*******************

The plotter will automatically visualize the potential, wavefuctions,
expected values of the Local operator and the energies. The user needs 
to execute the schrodinger_plotter.py to do so.
The following files will be used automatically:

* potential.dat
* wavefuncs.dat
* expvalues.dat
* energies.dat

These will be created, if an schrodinger.inp is created according to 
the example (see README oder schrodinger_solver) and if the 
schrondinger_solver.py is executed beforehand. 
Otherwise the files mentioned above can be copied to the folder
or created manually and be plotted by executing the schrodinger_plotter.py.
The graphs will be plotted using predetermined settings.

If you want to change the visualisation of the plot,
you can use the commandline to change the values of the axes as well as the amplitude of the wavefunction.
Type --help for further informations.

The arguments to be called will be displayed in the list below:

* --a = to set the amplitude of the wavefunction
* --xmin = for the x-axes minimum of the plot of the wavefunction
* --ymin = for the y-axes minimum of the plot of the wavefunction
* --xmax = for the x-axes maximum of the plot of the wavefunction
* --ymax = for the y-axes maximum of the plot of the wavefunction
* --sigmaxmin = to set x-axes minimum of the sigma plot
* --sigmaymin = to set y-axes minimum of the sigma plot
* --sigmaxmax = to set x-axes maximum of the sigma plot
* --sigmaymax = to set y-axes maximum of the sigma plot 

Please note, if one area is changed (for example xmin) the other variables (ymin, xmax, ymax)
have to be changes as well, otherwise a failure-message will appear. The same applies to the 
sigma-values. The amplitude of the wavefunction is independent.
