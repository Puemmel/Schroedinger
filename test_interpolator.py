"""
Testing the functionality of the interpolator by
using predefined potential files
"""
import numpy as np
import schrodinger_interpolator as SI
import schrodinger_solver as SV

directorys = ["Case1/", "Case2/", "Case3/", "Case4/", "Case5/", "Case6/"]

@pytest.mark.parametrize("schrodinger_interpol", directorys)
def test_potential(schrodinger_interpol):
        calc_pot = SI.schrodinger_interpol(i)
        assert np.all((calc_pot - "{i}/RefPot") < 1e-10)

@pytest.mark.parametrize()
def test_expected_values():
        calc_exp = SV.schrodinger_solver(i)
        assert np.all((calc_exp - "{i}/RefExp") < 1e-10)
