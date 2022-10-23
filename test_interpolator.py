"""
Testing the functionality of the interpolator by
using predefined potential files
"""
#putting data from created potential list into a list
PotCalc = []
with open("Potential.dat", "r", encoding="utf-8") as PotTest:
    for i in PotTest:
        PotCalc.append(i.split())
    PotTest.close()

#getting first entry of input with name of calculation
InpTest = []
with open("schroedinger.inp", "r", encoding="utf-8") as file1:
    for x in file1:
        InpTest.append(x.split())
    file1.close()

#adding name to variable
TEST_VARIABLE = " ".join(InpTest[0])

def rpot(arg) -> list:
    """definig reference potential list depending on name of calculation"""
    result = []
    with open(arg, "r", encoding="utf-8") as r_t:
        for i_x in r_t:
            result.append(i_x.split())
        return result

#writing list entries of potential into one column
flat_list_pot = []
for sublist in PotCalc:
    for item in sublist:
        flat_list_pot.append(item)

def rpot_flatlist(arg) -> list:
    """writing list entries of ref. potential into one column"""
    flat_list_rpot = []
    for slist in rpot(arg):
        for ritem in slist:
            flat_list_rpot.append(ritem)
    return flat_list_rpot

def test_answer1() -> None:
    """checking the first example potential with reference file"""
    if TEST_VARIABLE == "Unendlich tiefer Potentialkopf":
        for j in range(len(flat_list_pot)):
            assert flat_list_pot[j] == rpot_flatlist("RefPot1.dat")[j]

def test_answer2() -> None:
    """checking the second example potential with reference file"""
    if TEST_VARIABLE == "Endlich tiefer Potentialkopf":
        for j in range(len(flat_list_pot)):
            assert flat_list_pot[j] == rpot_flatlist("RefPot2.dat")[j]

def test_answer3() -> None:
    """checking the third example potential with reference file"""
    if TEST_VARIABLE == "Harmonischer Oszillator":
        for j in range(len(flat_list_pot)):
            assert flat_list_pot[j] == rpot_flatlist("RefPot3.dat")[j]

def test_answer4() -> None:
    """checking the fourth example potential with reference file"""
    if TEST_VARIABLE == "Doppelter Potentialtopf (linear)":
        for j in range(len(flat_list_pot)):
            assert flat_list_pot[j] == rpot_flatlist("RefPot4.dat")[j]

def test_answer5() -> None:
    """checking the fifth example potential with reference file"""
    if TEST_VARIABLE == "Doppelter Potentialkopf (natürlicher kubischer Spline)":
        for j in range(len(flat_list_pot)):
            assert flat_list_pot[j] == rpot_flatlist("RefPot5.dat")[j]

def test_answer6() -> None:
    """checking the sixth example potential with reference file"""
    if TEST_VARIABLE == "Asymmetrischer Potentialtopf":
        for j in range(len(flat_list_pot)):
            assert flat_list_pot[j] == rpot_flatlist("RefPot6.dat")[j]
