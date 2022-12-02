"""
Testing the functionality of the schrodinger_solver by
using predefined potential and expected values files
"""
import numpy as np
import pytest

from schrodinger_solver import writepotential, schrodinger_solver

directories = [('Case1/', 'Case1/RefPot.dat'),('Case2/', 'Case2/RefPot.dat'),
               ('Case3/', 'Case3/RefPot.dat'),('Case4/', 'Case4/RefPot.dat'),
               ('Case5/', 'Case5/RefPot.dat'),('Case6/', 'Case6/RefPot.dat')]


@pytest.mark.parametrize("test_input,expected", directories)
def test_potential(test_input, expected):
    "Test calculated potentials by interpolator"
    pot = []
    with open (expected, "r", encoding="utf-8") as file1:
        for i in file1:
            pot.append(i.split())
        file1.close()
    ypot = []
    for i, j in enumerate(pot):
        ypot.append(float(j[1]))
    assert np.all(np.abs((np.array(writepotential(test_input)) - ypot)) < 1e-10)

directories_solver = [('Case1/', 'Case1/RefExp.dat'),('Case2/', 'Case2/RefExp.dat'),
               ('Case3/', 'Case3/RefExp.dat'),('Case4/', 'Case4/RefExp.dat'),
               ('Case5/', 'Case5/RefExp.dat'),('Case6/', 'Case6/RefExp.dat')]

@pytest.mark.parametrize("test_input,expected", directories_solver)
def test_solver(test_input, expected):
    "Test calculated expected values by interpolator"
    pot = []
    with open (expected, "r", encoding="utf-8") as file1:
        for i in file1:
            pot.append(i.split())
        file1.close()
    ypot = []
    for i, j in enumerate(pot):
        ypot.append(float(j[1]))
    solution, eigenvalues, sigma, expx, xval1  = schrodinger_solver(test_input)
    assert np.all(np.abs((np.array(expx) - ypot)) < 1e-10)
