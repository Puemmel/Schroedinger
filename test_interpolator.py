"""
Testing the functionality of the interpolator by
using predefined potential files
"""
import numpy as np
import pytest
from schrodinger_solver import schrodinger_interpol

directories = ['Case1/','Case2/', 'Case3/', 'Case4/', 'Case5/', 'Case6/']

@pytest.mark.parametrize("schrodinger_interpol", directories)
def test_potential(schrodinger_interpol):
        "Test calculated potentials by interpolator"
        expected = schrodinger_interpol
        reference = {directories}.RefPot
        assert np.all((expected - reference) < 1e-10)
