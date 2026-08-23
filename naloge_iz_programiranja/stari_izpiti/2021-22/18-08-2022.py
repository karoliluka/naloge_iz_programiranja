import unittest
from collections import defaultdict
from itertools import pairwise

def tocen(red, dejansko):
    for expected, actual in zip(red, dejansko):
        if actual - expected > 20:
            return False
    return True

def tocni(redi, dejanski):
    st_tocnih = 0
    if not redi or not dejanski:
        return 0

    for red, dejansko in zip(redi, dejanski):
        if not tocen(red, dejansko):
            continue
        else:
            st_tocnih += 1
    return st_tocnih

def enaki(linija1, linija2):
    if set(linija1) == set(linija2) or linija1[0] == linija2[0] and linija1[-1] == linija2[-1] and (set(linija1) < set(linija2) or set(linija2) < set(linija1)):
        return True
    return False

def enaki_red(linija1, linija2):
    if linija1[0] != linija2[0] or linija1[-1] != linija2[-1]:
        return False
    i2 = 0
    if len(linija1) < len(linija2):
        linija1, linija2 = linija2, linija1

    for postaja1 in linija1:
        if i2 < len(linija2) and linija2[i2] == postaja1:
            i2 += 1
    return i2 == len(linija2)

def zamujenih(vlak, cakajoci):
    stevilo = 1
    for train in cakajoci[vlak]:
        stevilo += zamujenih(train, cakajoci)
    return stevilo

class Sprevodnik:
    def __init__(self, zacetna_postaja, cenik):
        self.zacetna_postaja = zacetna_postaja
        self.cenik = cenik #slovar onlike {(par imen postaj) : cena_prevoza} -> {(A,B) : 15}
        self.trenutna_postaja = zacetna_postaja
        self.denar = 0
        self.st_potnikov = 0
        self.slovar_st_potnikov = defaultdict(int)

    def postaja(self, ime):
        self.trenutna_postaja = ime
        self.st_potnikov -= self.slovar_st_potnikov[ime]

    def potnik(self, kam):
        if (self.trenutna_postaja, kam) in self.cenik:
            self.denar += self.cenik[(self.trenutna_postaja, kam)]
            self.st_potnikov += 1
            self.slovar_st_potnikov[kam] += 1

    def blagajna(self):
        return self.denar

    def potnikov(self):
        return self.st_potnikov


class Test01(unittest.TestCase):
    def test_tocen_opcijsko(self):
        self.assertTrue(tocen([570, 590, 616, 620], [570, 590, 616, 620]))
        self.assertTrue(tocen([570, 590, 616, 620], [574, 610, 636, 640]))

        self.assertFalse(tocen([570, 590, 616, 620], [591, 590, 616, 620]))
        self.assertFalse(tocen([570, 590, 616, 620], [570, 611, 616, 620]))
        self.assertFalse(tocen([570, 590, 616, 620], [570, 590, 616, 641]))

    def test_tocni(self):
        self.assertEqual(0, tocni([], []))
        self.assertEqual(1, tocni([[570, 590, 616, 620]],
                                  [[570, 590, 616, 620]]))
        self.assertEqual(0, tocni([[570, 590, 616, 620]],
                                  [[570, 611, 616, 620]]))
        self.assertEqual(2, tocni([[570, 590, 616, 620], [1200, 1500], [800, 900, 1000], [700, 800]],
                                  [[570, 611, 616, 620], [1200, 1510], [810, 910, 1000], [800, 900]]))


class Test02(unittest.TestCase):
    def test_enaki(self):
        # Čisto enaki
        self.assertTrue(enaki(["A", "C", "D", "F", "G"],
                              ["A", "C", "D", "F", "G"]))

        # Druga je hitrejša
        self.assertTrue(enaki(["A", "C", "D", "F", "G"],
                              ["A", "G"]))
        self.assertTrue(enaki(["A", "C", "D", "F", "G"],
                              ["A", "D", "G"]))
        self.assertTrue(enaki(["A", "C", "D", "F", "G"],
                              ["A", "D", "F", "G"]))
        self.assertTrue(enaki(["A", "C", "D", "F", "G"],
                              ["A", "D", "G"]))
        self.assertTrue(enaki(["A", "C", "D", "F", "G"],
                              ["A", "C", "G"]))

        # Prva je hitrejša
        self.assertTrue(enaki(["A", "G"],
                              ["A", "C", "D", "F", "G"]))
        self.assertTrue(enaki(["A", "D", "G"],
                              ["A", "C", "D", "F", "G"]))
        self.assertTrue(enaki(["A", "D", "F", "G"],
                              ["A", "C", "D", "F", "G"]))

        # Pomešan red
        self.assertTrue(enaki(["A", "C", "F", "D", "G"],
                              ["A", "C", "D", "F", "G"]))
        self.assertTrue(enaki(["A", "C", "F", "D", "G"],
                              ["A", "D", "F", "G"]))

        # Neenaki končni postaji
        self.assertFalse(enaki(["A", "C", "D", "F", "G"],
                               ["A", "C", "D", "F"]))
        self.assertFalse(enaki(["A", "C", "D", "F"],
                               ["A", "C", "D", "F", "G"]))

        # Ena ima postajo, ki je druga nima in tudi obratno
        self.assertFalse(enaki(["A", "C", "G"],
                               ["A", "D", "G"]))
        self.assertFalse(enaki(["A", "C", "E", "F", "G"],
                               ["A", "D", "E", "G"]))
        self.assertFalse(enaki(["A", "B", "C", "E", "F", "G"],
                               ["A", "B", "C", "D", "E", "G"]))
        self.assertFalse(enaki(["A", "C", "D", "G"],
                               ["A", "D", "F", "G"]))


class Test03(unittest.TestCase):
    def test_enaki_red(self):
        # Čisto enaki
        self.assertTrue(enaki_red(["A", "C", "D", "F", "G"],
                              ["A", "C", "D", "F", "G"]))

        # Druga je hitrejša
        self.assertTrue(enaki_red(["A", "C", "D", "F", "G"],
                              ["A", "G"]))
        self.assertTrue(enaki_red(["A", "C", "D", "F", "G"],
                              ["A", "D", "G"]))
        self.assertTrue(enaki_red(["A", "C", "D", "F", "G"],
                              ["A", "D", "F", "G"]))
        self.assertTrue(enaki_red(["A", "C", "D", "F", "G"],
                              ["A", "D", "G"]))
        self.assertTrue(enaki_red(["A", "C", "D", "F", "G"],
                              ["A", "C", "G"]))

        # Prva je hitrejša
        self.assertTrue(enaki_red(["A", "G"],
                              ["A", "C", "D", "F", "G"]))
        self.assertTrue(enaki_red(["A", "D", "G"],
                              ["A", "C", "D", "F", "G"]))
        self.assertTrue(enaki_red(["A", "D", "F", "G"],
                              ["A", "C", "D", "F", "G"]))

        # Neenaki začetni postaji
        self.assertFalse(enaki_red(["A", "C", "D", "F", "G"],
                               ["C", "D", "F", "G"]))
        self.assertFalse(enaki_red(["C", "D", "F", "G"],
                               ["A", "C", "D", "F", "G"]))

        # Neenaki končni postaji
        self.assertFalse(enaki_red(["A", "C", "D", "F", "G"],
                               ["A", "C", "D", "F"]))
        self.assertFalse(enaki_red(["A", "C", "D", "F"],
                               ["A", "C", "D", "F", "G"]))

        # Ena ima postajo, ki je druga nima in tudi obratno
        self.assertFalse(enaki_red(["A", "C", "G"],
                               ["A", "D", "G"]))
        self.assertFalse(enaki_red(["A", "C", "E", "F", "G"],
                               ["A", "D", "E", "G"]))
        self.assertFalse(enaki_red(["A", "B", "C", "E", "F", "G"],
                               ["A", "B", "C", "D", "E", "G"]))
        self.assertFalse(enaki_red(["A", "C", "D", "G"],
                               ["A", "D", "F", "G"]))

        # Napačen vrstni red postaj
        self.assertFalse(enaki_red(["A", "B", "C", "D", "G"],
                               ["A", "D", "C", "B", "G"]))
        self.assertFalse(enaki_red(["A", "B", "C", "D", "E", "G"],
                               ["A", "B", "E", "D", "G"]))


class Test04(unittest.TestCase):
    def test_zamujenih(self):
        cakajoci = {
            "LP0001": ["LP1256", "LP1682", "LP3682"],
            "LP3416": [],
            "LP8722": [],
            "LP6316": [],
            "LP1682": [],
            "LP3682": ["LP8524", "IC021"],
            "IC204": [],
            "LP8524": ["EN123", "IC521", "LP6316"],
            "LP5567": [],
            "LP2222": ["EN753"],
            "IC021": ["LP2222", "IC204"],
            "LP5568": ["LP8722", "LP3416", "LP8721"],
            "IC521": ["LP5567", "LP5568"],
            "EN123": [],
            "EN753": [],
            "LP1256": ["EN456"],
            "LP8721": [],
            "LP1212": [],
            "EN456": ["LP1212"],
        }

        self.assertEqual(14, zamujenih("LP3682", cakajoci))
        self.assertEqual(1, zamujenih("LP3416", cakajoci))
        self.assertEqual(1, zamujenih("LP3682", {"LP3682": set(), "LP1234": {"LP3682"}}))


class Test05(unittest.TestCase):
    def test_sprevodnik(self):
        sprevodnik = Sprevodnik("A",
                                {("A", "B"): 3,
                                 ("A", "C"): 5,
                                 ("A", "D"): 8,
                                 ("A", "E"): 12,
                                 ("B", "C"): 3,
                                 ("B", "D"): 6,
                                 ("B", "E"): 10,
                                 ("C", "D"): 4,
                                 ("C", "E"): 8,
                                 ("D", "E"): 5
                                 })
        self.assertEqual(0, sprevodnik.blagajna())
        self.assertEqual(0, sprevodnik.potnikov())
        sprevodnik.potnik("C")  # smo na A, karta stane 5
        self.assertEqual(5, sprevodnik.blagajna())  # sprevodnik ima 5
        self.assertEqual(1, sprevodnik.potnikov())
        sprevodnik.potnik("E")  # smo na A, karta stane 12
        self.assertEqual(17, sprevodnik.blagajna())  # sprevodnik ima 17
        self.assertEqual(2, sprevodnik.potnikov())

        sprevodnik.postaja("B")  # smo na B
        self.assertEqual(17, sprevodnik.blagajna())  # še vedno ima 17
        self.assertEqual(2, sprevodnik.potnikov())
        sprevodnik.potnik("C")  # smo na B, karta stane 3
        self.assertEqual(20, sprevodnik.blagajna())
        self.assertEqual(3, sprevodnik.potnikov())

        sprevodnik.postaja("C")  # smo na C -> dva potnika izstopita
        self.assertEqual(20, sprevodnik.blagajna())
        self.assertEqual(1, sprevodnik.potnikov())

        sprevodnik.postaja("D")  # smo na D -> nič novega
        self.assertEqual(20, sprevodnik.blagajna())
        self.assertEqual(1, sprevodnik.potnikov())

        sprevodnik.postaja("E")  # smo na C -> še en potnik izstopi
        self.assertEqual(20, sprevodnik.blagajna())
        self.assertEqual(0, sprevodnik.potnikov())


if __name__ == "__main__":
    unittest.main()