"""
Testing the functionality of the solver by
using predefined expected values files
"""

#putting data from created expected values list into a list
ExpCalc = []
with open("expvalues.dat", "r", encoding="utf-8") as ExpTest:
    for i in ExpTest:
        ExpCalc.append(i.split())
    ExpTest.close()

#getting first entry of input with name of calculation
InpTestZwei = []
with open("schroedinger.inp", "r", encoding="utf-8") as file1:
    for x in file1:
        InpTestZwei.append(x.split())
    file1.close()

#adding name to variable
TEST_VARIABLEZWEI = " ".join(InpTestZwei[0])

def rexp(arg) -> list:
    """definig reference expected values list depending on name of calculation"""
    result = []
    with open(arg, "r", encoding="utf-8") as r_t:
        for i_x in r_t:
            result.append(i_x.split())
        return result

#writing list entries of expected values into one column
flat_list_exp = []
for sublist in ExpCalc:
    for item in sublist:
        flat_list_exp.append(item)

def rexp_flatlist(arg) -> list:
    """writing list entries of ref. expected values into one column"""
    flat_list_rexp = []
    for slist in rexp(arg):
        for ritem in slist:
            flat_list_rexp.append(ritem)
    return flat_list_rexp

def test_expvaluesanswer1() -> None:
    """checking the first example of expacted values with reference file"""
    if TEST_VARIABLEZWEI == "Unendlich tiefer Potentialkopf":
        for j, k in enumerate(flat_list_exp):
            assert k == rexp_flatlist("RefExp1.dat")[j]

def test_expvaluesanswer2() -> None:
    """checking the second example of expacted values with reference file"""
    if TEST_VARIABLEZWEI == "Endlich tiefer Potentialkopf":
        for j, k in enumerate(flat_list_exp):
            assert k == rexp_flatlist("RefExp2.dat")[j]

def test_expvaluesanswer3() -> None:
    """checking the third example of expacted values with reference file"""
    if TEST_VARIABLEZWEI == "Harmonischer Oszillator":
        for j, k in enumerate(flat_list_exp):
            assert k == rexp_flatlist("RefExp3.dat")[j]

def test_expvaluesanswer4() -> None:
    """checking the fourth example of expacted values with reference file"""
    if TEST_VARIABLEZWEI == "Doppelter Potentialtopf (linear)":
        for j, k in enumerate(flat_list_exp):
            assert k == rexp_flatlist("RefExp4.dat")[j]

def test_expvaluesanswer5() -> None:
    """checking the fifth example of expacted values with reference file"""
    if TEST_VARIABLEZWEI == "Doppelter Potentialkopf (natÃ¼rlicher kubischer Spline)":
        for j, k in enumerate(flat_list_exp):
            assert k == rexp_flatlist("RefExp5.dat")[j]

def test_expvaluesanswer6() -> None:
    """checking the sixth example of expacted values with reference file"""
    if TEST_VARIABLEZWEI == "Asymmetrischer Potentialtopf":
        for j, k in enumerate(flat_list_exp):
            assert k == rexp_flatlist("RefExp6.dat")[j]
