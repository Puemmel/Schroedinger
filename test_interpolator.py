"""
Testing the functionality of the interpolator by 
using predefined potential files
"""
PotTest = open("Potential.dat", "r")

#putting data from created potential list into a list
PotCalc = []
for i in PotTest:
    PotCalc.append(i.split())
PotTest.close()

#getting first entry of input with name of calculation
f = open("schroedinger.inp", "r")
InpTest = []
for x in f:
    InpTest.append(x.split())
f.close()

#adding name to variable
TEST_VARIABLE = " ".join(InpTest[0])

#definig reference potential list depending on name of calculation
def rpot(arg) -> list:
    result = []
    r_t = open(arg, "r")
    for i_x in r_t:
        result.append(i_x.split())
    return result

#writing list entries of potential into one column
flat_list_pot = []
for sublist in PotCalc:
    for item in sublist:
        flat_list_pot.append(item)

#writing list entries of ref. potential into one column
def rpot_flatlist(arg) -> list:
    flat_list_rpot = []
    for slist in rpot(arg):
        for ritem in slist:
            flat_list_rpot.append(ritem)
    return flat_list_rpot

def test_answer1() -> None:
    if TEST_VARIABLE == "Unendlich tiefer Potentialkopf":
        for i in range(len(flat_list_pot)): 
            assert flat_list_pot[i] == rpot_flatlist("RefPot1.dat")[i]

def test_answer1() -> None:
    if TEST_VARIABLE == "Endlich tiefer Potentialkopf":
        for i in range(len(flat_list_pot)): 
            assert flat_list_pot[i] == rpot_flatlist("RefPot2.dat")[i]

def test_answer1() -> None:
    if TEST_VARIABLE == "Harmonischer Oszillator":
        for i in range(len(flat_list_pot)): 
            assert flat_list_pot[i] == rpot_flatlist("RefPot3.dat")[i]

def test_answer1() -> None:
    if TEST_VARIABLE == "Doppelter Potentialtopf (linear)":
        for i in range(len(flat_list_pot)): 
            assert flat_list_pot[i] == rpot_flatlist("RefPot4.dat")[i]

def test_answer1() -> None:
    if TEST_VARIABLE == "Doppelter Potentialkopf (natürlicher kubischer Spline)":
        for i in range(len(flat_list_pot)): 
            assert flat_list_pot[i] == rpot_flatlist("RefPot5.dat")[i]

def test_answer1() -> None:
    if TEST_VARIABLE == "Asymmetrischer Potentialtopf":
        for i in range(len(flat_list_pot)): 
            assert flat_list_pot[i] == rpot_flatlist("RefPot6.dat")[i]