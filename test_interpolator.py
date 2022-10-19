import interpolator as pol

"""
Testing the functionality of the interpolator by 
using predefined potential files
"""

PotTest = open("Potential.dat", "r")

#Writing the datapoints from the potential.dat into a list
PotCalc = []
for i in PotTest:
        PotCalc.append(i.split())
PotTest.close()

TestVariable = []
f = open("schroedinger.inp", "r")

#Getting the name of the schroedingerfile from first line in input file
InpTest = []
for x in f:
    InpTest.append(x.split())
f.close() 
TestVariable.append(" ".join(InpTest[0]))

#argument ist the reference file depending on the Inputname of Schroedinger file in first line
def rpot(arg):
    r = []
    rpot = open(arg, "r")
    for i in rpot: 
        r.append(i.split())
    return r

def test_answer1():
    pol.interpol("schroedinger.inp")
    if TestVariable == "Unendlich tiefer Potentialkopf":
        for i in range(len(PotCalc)): 
            for j in range(len(PotCalc)):
                assert rpot("RefPot1.dat")[i][j] == PotCalc[i][j]

def test_answer2():
    pol.interpol("schroedinger.inp")
    if TestVariable == "Endlich tiefer Potentialkopf":
        for i in range(len(PotCalc)): 
            for j in range(len(PotCalc)):
                assert rpot("RefPot2.dat")[i][j] == PotCalc[i][j]

def test_answer3():
    pol.interpol("schroedinger.inp")
    if TestVariable == "Harmonischer Oszillator":
        for i in range(len(PotCalc)): 
            for j in range(len(PotCalc)):
                assert rpot("RefPot2.dat")[i][j] == PotCalc[i][j]

def test_answer4():
    pol.interpol("schroedinger.inp")
    if TestVariable == "Doppelter Potentialtopf (linear)":
        for i in range(len(PotCalc)): 
            for j in range(len(PotCalc)):
                assert rpot("RefPot2.dat")[i][j] == PotCalc[i][j]

def test_answer5():
    pol.interpol("schroedinger.inp")
    if TestVariable == "Doppelter Potentialkopf (natÃ¼rlicher kubischer Spline)":
        for i in range(len(PotCalc)): 
            for j in range(len(PotCalc)):
                assert rpot("RefPot2.dat")[i][j] == PotCalc[i][j]

def test_answer5():
    pol.interpol("schroedinger.inp")
    if TestVariable == "Asymmetrischer Potentialtopf":
        for i in range(len(PotCalc)): 
            for j in range(len(PotCalc)):
                assert rpot("RefPot2.dat")[i][j] == PotCalc[i][j]
