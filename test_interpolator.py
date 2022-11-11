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

def rpot(arg) -> list: #Rückgabetyp der Funktion, gibt eine Liste zurück! Datentyp #Arg: Parameter von rpot
    """Wir öffnen die Referenzdatei und schreiben die in diese Liste"""
    result = []
    with open(arg, "r", encoding="utf-8") as r_t:
        for i_x in r_t:
            result.append(i_x.split())
        return result

#writing list entries of potential into one column mit der zu überprüfenden Liste
flat_list_pot = []
for sublist in PotCalc:#Diese Liste ist die zu prüfende
    for item in sublist:
        flat_list_pot.append(item)

def rpot_flatlist(arg) -> list:#Rückgabetyp der Funktion, gibt eine Liste zurück! Datentyp 
    """writing list entries of ref. potential into one column  und machen diese dann 1D -> Einfacher durch die Liste der Werte zu iterieren""" # Versehentlich 2mal gemacht
    flat_list_rpot = []
    for slist in rpot(arg):#Arg: Parameter von rpot
        for ritem in slist:
            flat_list_rpot.append(ritem)
    return flat_list_rpot

def test_answer1() -> None: #Gibt keinen Datentyp zurück
    """checking the first example potential with reference file"""
    if TEST_VARIABLE == "Unendlich tiefer Potentialkopf":
        for j, k in enumerate(flat_list_pot):
            assert k == rpot_flatlist("RefPot1.dat")[j] #Hier fülle ich Arg mit der Referenzdatei

def test_answer2() -> None:#Gibt keinen Datentyp zurück
    """checking the second example potential with reference file"""
    if TEST_VARIABLE == "Endlich tiefer Potentialkopf":
        for j, k in enumerate(flat_list_pot):
            assert k == rpot_flatlist("RefPot2.dat")[j] #assert ist Teil der Testannahme und überprüft, ob die Werte gleich sind

def test_answer3() -> None:
    """checking the third example potential with reference file"""
    if TEST_VARIABLE == "Harmonischer Oszillator":
        for j, k in enumerate(flat_list_pot): #k ist das Element der Liste, j ist der Index des Elementes innerhalb der Liste -> J vergleicht ob der Index denselben k wert hat
            assert k == rpot_flatlist("RefPot3.dat")[j]

def test_answer4() -> None:
    """checking the fourth example potential with reference file"""
    if TEST_VARIABLE == "Doppelter Potentialtopf (linear)":
        for j, k in enumerate(flat_list_pot):
            assert k == rpot_flatlist("RefPot4.dat")[j]
            #Zwei Fließkommazahlen nicht mit == vergleichen
            #Variablen über alle möglichen tes

def test_answer5() -> None:
    """checking the fifth example potential with reference file"""
    if TEST_VARIABLE == "Doppelter Potentialkopf (natürlicher kubischer Spline)":
        for j, k in enumerate(flat_list_pot):
            assert k  == rpot_flatlist("RefPot5.dat")[j]

def test_answer6() -> None:
    """checking the sixth example potential with reference file"""
    if TEST_VARIABLE == "Asymmetrischer Potentialtopf":
        for j, k in enumerate(flat_list_pot):
            assert k == rpot_flatlist("RefPot6.dat")[j] 
