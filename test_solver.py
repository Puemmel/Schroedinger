"""
Testing the functionality of the solver by 
using predefined expected values files
"""
ExpTest = open("expvalues.dat", "r")

#putting data from created expected values list into a list
ExpCalc = []
for i in ExpTest:
    ExpCalc.append(i.split())
ExpTest.close()

#getting first entry of input with name of calculation
f = open("schroedinger.inp", "r")
InpTest = []
for x in f:
    InpTest.append(x.split())
f.close()

#adding name to variable
TEST_VARIABLE = " ".join(InpTest[0])

#definig reference expected values list depending on name of calculation
def rexp(arg) -> list:
    result = []
    r_t = open(arg, "r")
    for i_x in r_t:
        result.append(i_x.split())
    return result

#writing list entries of expected values into one column
flat_list_exp = []
for sublist in ExpCalc:
    for item in sublist:
        flat_list_exp.append(item)

#writing list entries of ref. expected values into one column
def rexp_flatlist(arg) -> list:
    flat_list_rexp = []
    for slist in rexp(arg):
        for ritem in slist:
            flat_list_rexp.append(ritem)
    return flat_list_rexp

def test_answer1() -> None:
    if TEST_VARIABLE == "Unendlich tiefer Potentialkopf":
        for i in range(len(flat_list_exp)): 
            assert flat_list_exp[i] == rexp_flatlist("RefExp1.dat")[i]

def test_answer1() -> None:
    if TEST_VARIABLE == "Endlich tiefer Potentialkopf":
        for i in range(len(flat_list_exp)): 
            assert flat_list_exp[i] == rexp_flatlist("RefExp2.dat")[i]

def test_answer1() -> None:
    if TEST_VARIABLE == "Harmonischer Oszillator":
        for i in range(len(flat_list_exp)): 
            assert flat_list_exp[i] == rexp_flatlist("RefExp3.dat")[i]

def test_answer1() -> None:
    if TEST_VARIABLE == "Doppelter Potentialtopf (linear)":
        for i in range(len(flat_list_exp)): 
            assert flat_list_exp[i] == rexp_flatlist("RefExp4.dat")[i]

def test_answer1() -> None:
    if TEST_VARIABLE == "Doppelter Potentialkopf (natÃ¼rlicher kubischer Spline)":
        for i in range(len(flat_list_exp)): 
            assert flat_list_exp[i] == rexp_flatlist("RefExp5.dat")[i]

def test_answer1() -> None:
    if TEST_VARIABLE == "Asymmetrischer Potentialtopf":
        for i in range(len(flat_list_exp)): 
            assert flat_list_exp[i] == rexp_flatlist("RefExp6.dat")[i]