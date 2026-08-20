import unittest
import warnings
import random
from collections import defaultdict


def nabava(stari, novi):
    slovar_nabavit = defaultdict(int)
    slovar_starih = defaultdict(int)  # kljuc je dolzina ovire, vrednosti pa stevilo ovir dolzine dolzina npr. 5 : 3 -> 3 ovire dolzine 5
    for (x0, x1, y) in stari:
        dolzina = x1 - x0 + 1
        slovar_starih[dolzina] += 1

    slovar_novih = defaultdict(int)
    for (x0, x1, y) in novi:
        dolzina = x1 - x0 + 1
        slovar_novih[dolzina] += 1

    for ime_ovire, stevilo in slovar_novih.items():
        if ime_ovire in slovar_starih:
            if stevilo > slovar_starih[ime_ovire]:
                slovar_nabavit[ime_ovire] += stevilo - slovar_starih[ime_ovire]
        else:
            slovar_nabavit[ime_ovire] = stevilo
    return slovar_nabavit

def rekonstrukcija(kocke):
    slovar_kock = defaultdict(list)
    for (y, x) in kocke:
        slovar_kock[y].append(x)

    urejen_slovar_kock = sorted(slovar_kock.items(), key=lambda kocka: kocka[0])

    rezultat = []
    for y, stolpci in urejen_slovar_kock:
        stolpci = sorted(stolpci)
        zacetek = stolpci[0]
        prejsni = stolpci[0]

        for stolpec in stolpci[1:]:
            if stolpec == prejsni + 1:
                prejsni = stolpec
            else:
                rezultat.append((zacetek, prejsni, y))
                zacetek = stolpec
                prejsni = stolpec

        rezultat.append((zacetek, prejsni, y))
    return rezultat

def dekodiraj_vrstico(vrstica):
    seznam = []
    zacetek_ovire = False
    for i, char in enumerate(vrstica, start=1):
        if char == "<" and zacetek_ovire is False:
            zacetek = i
            zacetek_ovire = True
        elif char == ">" and zacetek_ovire is True:
            seznam.append((zacetek, i))
            zacetek = 0
            zacetek_ovire = False
    return seznam

def preberi(ime_datoteke):
    seznam_ovir = []
    with open(ime_datoteke, "r", encoding="utf-8") as datoteka:
        for i, vrstica in enumerate(datoteka, start=1):
            for terka in dekodiraj_vrstico(vrstica.strip()):
                if terka:
                    x0 = terka[0]
                    x1 = terka[1]
                    seznam_ovir.append((x0, x1, i))
    return seznam_ovir

def vrhovi(skladovnica, ovira, visina):
    ovire = set()
    if ovira not in skladovnica:
        if visina <= 0:
            ovire.add(ovira)
    else:
        for nadovira in skladovnica[ovira]:
            ovire |= vrhovi(skladovnica, nadovira, visina - 1)
    return ovire



class Ovire:
    def __init__(self, mnozica_ovir):
        self.mnozica_ovir = mnozica_ovir #množica oblike (x0, x1, y)
        self.kopija_mnozica_ovir = mnozica_ovir.copy()
        self.vsi_zadetki = 0
        self.slovar_ovir = defaultdict(int)
        for ovira in self.kopija_mnozica_ovir:
            self.slovar_ovir[ovira] = 0

    def strel(self, x, y):
        for x0, x1, y_o in self.kopija_mnozica_ovir:
            if x0 <= x <= x1 and y == y_o:
                self.vsi_zadetki += 1
                self.slovar_ovir[(x0, x1, y_o)] += 1
                if self.slovar_ovir[(x0, x1, y_o)] == 3:
                    del self.slovar_ovir[(x0, x1, y_o)]
                    self.kopija_mnozica_ovir.remove((x0, x1, y_o))
                return True
        return False

    def zadetkov(self):
        return self.vsi_zadetki

    def vse_ovire(self):
        return self.kopija_mnozica_ovir

    def zmaga(self):
        if not self.kopija_mnozica_ovir:
            return True
        return False



with open("ovire.txt", "wt", encoding="utf-8") as f:
    f.write("""
...<-->........
<->......<--->.
...............
...<-->..<--->.
...............
...<-->........
<->..<>...<--->.
""".lstrip())

class Test(unittest.TestCase):
    def setUp(self):
        warnings.simplefilter("ignore", ResourceWarning)

    def test_1_nabava(self):
        self.assertEqual(nabava([], []), {})
        self.assertEqual(nabava([(1, 1, 1)], [(1, 1, 1)]), {})
        self.assertEqual(nabava([(1, 1, 1)], [(3, 3, 2)]), {})
        self.assertEqual(nabava([(5, 8, 3)], [(6, 9, 4)]), {})
        self.assertEqual(nabava([(1, 1, 1), (5, 8, 3)], [(3, 3, 8), (6, 9, 4)]), {})

        self.assertEqual(nabava([], [(1, 1, 2)]), {1: 1})
        self.assertEqual(nabava([], [(4, 8, 3)]), {5: 1})
        self.assertEqual(nabava([], [(1, 1, 2), (4, 8, 3)]), {1: 1, 5: 1})
        self.assertEqual(nabava([], [(1, 1, 2), (5, 9, 10), (4, 8, 3)]), {1: 1, 5: 2})
        self.assertEqual(nabava([(1, 1, 1)], [(1, 1, 2), (5, 9, 10), (4, 8, 3)]), {5: 2})
        self.assertEqual(nabava([], [(1, 1, 2), (10, 14, 7), (5, 9, 10), (4, 8, 3)]), {1: 1, 5: 3})
        self.assertEqual(nabava([(9, 13, 5)], [(1, 1, 2), (10, 14, 7), (5, 9, 10), (4, 8, 3)]), {1: 1, 5: 2})
        self.assertEqual(nabava([(1, 3, 1), (9, 13, 5)], [(1, 1, 2), (10, 14, 7), (5, 9, 10), (4, 8, 3)]), {1: 1, 5: 2})
        self.assertEqual(nabava([(1, 3, 1), (9, 13, 5)], [(1, 1, 2), (10, 14, 7), (5, 9, 10), (4, 8, 3)]), {1: 1, 5: 2})
        self.assertEqual(nabava([(1, 3, 1), (2, 2, 3), (9, 13, 5)], [(1, 1, 2), (10, 14, 7), (5, 9, 10), (4, 8, 3)]), {5: 2})

    def test_2_rekonstrukcija(self):
        self.assertEqual([], rekonstrukcija([]))
        self.assertEqual(
            [(3, 3, 1)],
            rekonstrukcija([(1, 3)])
        )

        self.assertEqual(
            [(3, 4, 1)],
            rekonstrukcija([(1, 3), (1, 4)]))

        self.assertEqual(
            [(3, 4, 1)],
            rekonstrukcija([(1, 4), (1, 3)]))

        self.assertEqual(
            [(3, 5, 1)],
            rekonstrukcija([(1, 3), (1, 4), (1, 5)]))

        self.assertEqual(
            [(3, 5, 1)],
            rekonstrukcija([(1, 5), (1, 3), (1, 4)]))

        self.assertEqual(
            [(3, 5, 1), (3, 4, 2)],
            rekonstrukcija([(1, 5), (1, 3), (1, 4), (2, 3), (2, 4)]))

        self.assertEqual(
            [(3, 5, 1), (3, 4, 2)],
            rekonstrukcija([(1, 5), (1, 3), (1, 4), (2, 4), (2, 3)]))

        self.assertEqual(
            [(1, 2, 1), (2, 4, 2), (4, 4, 3)],
            rekonstrukcija([(1, 1), (1, 2), (2, 2), (2, 3), (2, 4), (3, 4)]))
        # isto kot zgoraj, le pomešano
        self.assertEqual(
            [(1, 2, 1), (2, 4, 2), (4, 4, 3)],
            rekonstrukcija([(2, 3), (1, 1), (2, 2), (2, 4), (1, 2), (3, 4)]))

        self.assertEqual(
            [(1, 2, 1), (2, 4, 2), (4, 5, 3)],
            rekonstrukcija([(1, 1), (1, 2), (2, 2), (2, 3), (2, 4), (3, 4), (3, 5)]))
        # isto kot zgoraj, le pomešano
        self.assertEqual(
            [(1, 2, 1), (2, 4, 2), (4, 5, 3)],
            rekonstrukcija([(3, 5), (1, 1), (2, 4), (3, 4), (1, 2), (2, 2), (2, 3)]))

        self.assertEqual(
            [(1, 2, 1), (2, 4, 2), (4, 5, 3), (5, 5, 4)],
            rekonstrukcija([(1, 1), (1, 2), (2, 2), (2, 3), (2, 4), (3, 4), (3, 5), (4, 5)]))
        # isto kot zgoraj, le pomešano
        self.assertEqual(
            [(1, 2, 1), (2, 4, 2), (4, 5, 3), (5, 5, 4)],
            rekonstrukcija([(1, 1), (2, 4), (3, 4), (1, 2), (2, 2), (2, 3), (3, 5), (4, 5)]))

        kocke = [(1, 2), (1, 3), (1, 4), (1, 8), (1, 9), (1, 10),
                 (2, 5),
                 (3, 2), (3, 3), (3, 4), (3, 8), (3, 9), (3, 10),
                 (4, 5),
                 (5, 1), (5, 2), (5, 3), (5, 7), (5, 8), (5, 9),
                 (6, 4),
                 (7, 1), (7, 2), (7, 3), (7, 7), (7, 8), (7, 9)]

        for _ in range(10):
            random.shuffle(kocke)
            self.assertEqual(
                [(2, 4, 1), (8, 10, 1), (5, 5, 2), (2, 4, 3), (8, 10, 3), (5, 5, 4),
                 (1, 3, 5), (7, 9, 5), (4, 4, 6), (1, 3, 7), (7, 9, 7)],
                rekonstrukcija(kocke))

    def test_3a_dekodiraj_vrstico(self):
        self.assertEqual([], dekodiraj_vrstico("........"))
        self.assertEqual([(1, 2)], dekodiraj_vrstico("<>......"))
        self.assertEqual([(3, 4)], dekodiraj_vrstico("..<>......"))
        self.assertEqual([(3, 6)], dekodiraj_vrstico("..<-->....."))
        self.assertEqual([(3, 6), (10, 15)], dekodiraj_vrstico("..<-->...<---->.."))
        self.assertEqual([(3, 6), (10, 15), (18, 19)], dekodiraj_vrstico("..<-->...<---->..<>"))
        self.assertEqual([(1, 2), (4, 7), (11, 16), (19, 20)], dekodiraj_vrstico("<>.<-->...<---->..<>"))

    def test_3b_preberi(self):
        self.assertEqual([(4, 7, 1),
                          (1, 3, 2),
                          (10, 14, 2),
                          (4, 7, 4),
                          (10, 14, 4),
                          (4, 7, 6),
                          (1, 3, 7),
                          (6, 7, 7),
                          (11, 15, 7)], preberi("ovire.txt"))

    def test_4_vrhovi(self):
        """
               T
          j    l         z      B  A
          w i oo  pp     s      gg n
          c r uu vvv     x y    qq mm
          aaa bbbbbb     ttt ee fffff
          dddddddddd     hhhhhhhhhhhh
        ..............................
        """
        skladovnica = {
            ".": "dh",
            "d": "ab",
            "h": "tef",
            "a": "cr",
            "b": "uv",
            "t": "xy",
            "f": "qm",
            "c": "w",
            "r": "i",
            "u": "o",
            "v": "p",
            "x": "s",
            "q": "g",
            "m": "n",
            "w": "j",
            "o": "l",
            "s": "z",
            "g": "B",
            "n": "A",
            "l": "T"
        }
        self.assertEqual(set("jiTp"), vrhovi(skladovnica, "d", 0))
        self.assertEqual(set("jiTp"), vrhovi(skladovnica, "d", -2))
        self.assertEqual(set("jiTp"), vrhovi(skladovnica, "d", 3))
        self.assertEqual(set("jT"), vrhovi(skladovnica, "d", 4))
        self.assertEqual(set("T"), vrhovi(skladovnica, "d", 5))
        self.assertEqual(set(), vrhovi(skladovnica, "d", 6))

        self.assertEqual(set("T"), vrhovi(skladovnica, "u", 2))
        self.assertEqual(set("Tp"), vrhovi(skladovnica, "b", 2))
        self.assertEqual(set("T"), vrhovi(skladovnica, "b", 3))

        self.assertEqual({'i', 'A', 'p', 'T', 'B', 'z', 'j', 'e', 'y'}, vrhovi(skladovnica, ".", 2))
        self.assertEqual({'i', 'A', 'p', 'T', 'B', 'z', 'j', 'y'}, vrhovi(skladovnica, ".", 3))
        self.assertEqual({'i', 'A', 'p', 'T', 'B', 'z', 'j'}, vrhovi(skladovnica, ".", 4))
        self.assertEqual({'A', 'T', 'B', 'z', 'j'}, vrhovi(skladovnica, ".", 5))
        self.assertEqual({'T'}, vrhovi(skladovnica, ".", 6))
        self.assertEqual(set(), vrhovi(skladovnica, ".", 7))

    def test_5_potapljanje(self):
        zacetne = {(1, 2, 5), (2, 4, 2), (5, 10, 4)}
        kopija = zacetne.copy()
        ovire = Ovire(zacetne)
        self.assertEqual(zacetne, ovire.vse_ovire())
        self.assertEqual(0, ovire.zadetkov())

        ovire2 = Ovire(set())
        self.assertEqual(0, ovire2.zadetkov())
        self.assertEqual(set(), ovire2.vse_ovire())
        self.assertTrue(ovire2.zmaga())

        self.assertFalse(ovire.strel(1, 1))
        self.assertEqual(zacetne, ovire.vse_ovire())
        self.assertEqual(0, ovire.zadetkov())

        self.assertTrue(ovire.strel(3, 2))
        self.assertEqual(zacetne, ovire.vse_ovire())
        self.assertEqual(1, ovire.zadetkov())
        self.assertFalse(ovire.zmaga())

        self.assertTrue(ovire.strel(2, 5))
        self.assertEqual(zacetne, ovire.vse_ovire())
        self.assertEqual(2, ovire.zadetkov())

        self.assertTrue(ovire.strel(3, 2))
        self.assertEqual(zacetne, ovire.vse_ovire())
        self.assertEqual(3, ovire.zadetkov())

        self.assertTrue(ovire.strel(4, 2))
        self.assertEqual({(1, 2, 5), (5, 10, 4)}, ovire.vse_ovire())
        self.assertEqual(4, ovire.zadetkov())

        self.assertFalse(ovire.strel(4, 2))
        self.assertEqual({(1, 2, 5), (5, 10, 4)}, ovire.vse_ovire())
        self.assertEqual(4, ovire.zadetkov())

        self.assertFalse(ovire.strel(2, 2))
        self.assertEqual({(1, 2, 5), (5, 10, 4)}, ovire.vse_ovire())
        self.assertEqual(4, ovire.zadetkov())

        self.assertFalse(ovire.zmaga())
        self.assertEqual(kopija, zacetne)

        self.assertEqual(0, ovire2.zadetkov())
        self.assertEqual(set(), ovire2.vse_ovire())
        self.assertTrue(ovire2.zmaga())

        self.assertTrue(ovire.strel(5, 4))
        self.assertEqual({(1, 2, 5), (5, 10, 4)}, ovire.vse_ovire())
        self.assertEqual(5, ovire.zadetkov())

        self.assertTrue(ovire.strel(10, 4))
        self.assertEqual({(1, 2, 5), (5, 10, 4)}, ovire.vse_ovire())
        self.assertEqual(6, ovire.zadetkov())

        self.assertFalse(ovire.strel(4, 2))
        self.assertEqual({(1, 2, 5), (5, 10, 4)}, ovire.vse_ovire())
        self.assertEqual(6, ovire.zadetkov())

        self.assertTrue(ovire.strel(1, 5))
        self.assertEqual({(1, 2, 5), (5, 10, 4)}, ovire.vse_ovire())
        self.assertEqual(7, ovire.zadetkov())

        self.assertTrue(ovire.strel(1, 5))
        self.assertEqual({(5, 10, 4)}, ovire.vse_ovire())
        self.assertEqual(8, ovire.zadetkov())

        self.assertFalse(ovire.strel(1, 5))
        self.assertEqual({(5, 10, 4)}, ovire.vse_ovire())
        self.assertEqual(8, ovire.zadetkov())

        self.assertFalse(ovire.zmaga())

        self.assertTrue(ovire.strel(7, 4))
        self.assertEqual(set(), ovire.vse_ovire())
        self.assertEqual(9, ovire.zadetkov())

        self.assertTrue(ovire.zmaga())

        self.assertFalse(ovire.strel(7, 4))
        self.assertEqual(set(), ovire.vse_ovire())
        self.assertEqual(9, ovire.zadetkov())

        self.assertTrue(ovire.zmaga())

        self.assertEqual(0, ovire2.zadetkov())
        self.assertEqual(set(), ovire2.vse_ovire())
        self.assertTrue(ovire2.zmaga())


if __name__ == "__main__":
    unittest.main()