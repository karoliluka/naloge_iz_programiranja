import unittest
import random
from collections import defaultdict
from pdb import post_mortem


def prehodi(ovire):
    fake_ovire = sorted(ovire.copy())
    mnozica_koordinat = set()
    for ovira1, ovira2 in zip(fake_ovire, fake_ovire[1:]):
        y_1, x0_1, x1_1 = ovira1
        y_2, x0_2, x1_2 = ovira2
        if y_1 == y_2 and x1_1 + 2 == x0_2:
            mnozica_koordinat.add((y_1, x1_1 + 1))
    return mnozica_koordinat

def nadlezna_ovira(ovire, y, x, pot):
    slovar = defaultdict(int) #slovar oblike {ovira : st_prehodov}

    for char in pot:
        if char == ">":
            x += 1
        elif char == "<":
            x -= 1
        elif char == "v":
            y += 1
        elif char == "^":
            y -= 1

        for (y_o, x0_o, x1_o) in ovire:
            if y_o == y and x0_o <= x <= x1_o:
                slovar[(y_o, x0_o, x1_o)] += 1

    if len(slovar) == 0:
        return None
    else:
        return max(slovar, key=slovar.get)

def najdaljsi_skok(ovire, ovira):
    yo = ovira[0]
    naslednje = naprej(ovire, ovira)
    if not naslednje:
        return yo - 1  # nič ji ni vec v napoto - lahko poskoci direktno do vrha

    cene = []
    for n in naslednje:
        d = yo - n[0] - 1
        cene.append(max(d, najdaljsi_skok(ovire, n)))
    return min(cene)


def odstrani(ovire, stolpci):
    pomozen_seznam = []
    for stolpec in stolpci:
        for (y_o, x0_o, x1_o) in ovire:
            if x0_o <= stolpec <= x1_o:
                pomozen_seznam.append((y_o, x0_o, x1_o))

    nov_seznam = []
    for ovira in ovire:
        if ovira not in pomozen_seznam:
            nov_seznam.append(ovira)

    ovire[:] = nov_seznam

class Kolesar:
    def __init__(self, ovire, y, x):
        self.ovire = ovire
        self.y = y
        self.x = x
        self.stevilo_unicenih_ovir = 0
        self.kopija_ovir = ovire.copy()

    def premik(self, smer):
        if smer == ">":
            self.x += 1
        elif smer == "<":
            self.x -= 1
        elif smer == "v":
            self.y += 1
        elif smer == "^":
            self.y -= 1

        for i, (y_o, x0_o, x1_o) in enumerate(self.kopija_ovir):
            if y_o == self.y and x0_o <= self.x <= x1_o:
                self.stevilo_unicenih_ovir += 1
                del self.kopija_ovir[i]

    def lokacija(self):
        return self.y, self.x

    def uspesnost(self):
        return self.stevilo_unicenih_ovir




ovire = [(1, 1, 1), (1, 3, 3),
         (2, 1, 4), (2, 6, 7), (2, 11, 12),
         (3, 9, 9),
         (5, 3, 5), (5, 7, 10),
         (7, 4, 5), (7, 11, 11), (7, 13, 14),
         (9, 1, 1), (9, 3, 4), (9, 8, 10),
         (10, 6, 7), (10, 12, 12), (10, 14, 14),
         (11, 9, 9),
         (12, 1, 1), (12, 3, 4), (12, 10, 12),
         (14, 1, 3), (14, 8, 10)
         ]

kopija_ovir = ovire.copy()

def naprej(ovire, ovira):
    yo, xo0, xo1 = ovira
    return [(y, x0, x1) for y, x0, x1 in ovire
            if y < yo and (x0 <= xo0 <= x1 or xo0 <= x0 <= xo1)]


class Test(unittest.TestCase):
    def test_01_prehodi(self):
        self.assertEqual(
            {(1, 2), (2, 5), (5, 6), (7, 12), (9, 2), (10, 13), (12, 2)},
            prehodi(ovire))
        self.assertEqual(ovire, kopija_ovir, "ne spreminjaj podanega seznama ovir!")

        ovire2 = ovire.copy()
        random.shuffle(ovire2)
        self.assertEqual(
            {(1, 2), (2, 5), (5, 6), (7, 12), (9, 2), (10, 13), (12, 2)},
            prehodi(ovire2))
        ovire_k2 = ovire2.copy()
        self.assertEqual(ovire2, ovire_k2, "ne spreminjaj podanega seznama ovir!")

    def test_02_nadlezna_ovira(self):
        # prva točka ni na oviri. če jih je več, lahko vrne katerokoli
        self.assertEqual((7, 4, 5), nadlezna_ovira(ovire, 10, 4, "^^^^^^>vvv<<vvv<^<^^"))
        self.assertEqual((9, 3, 4), nadlezna_ovira(ovire, 6, 4, "vvv<"))
        self.assertEqual((5, 3, 5), nadlezna_ovira(ovire, 6, 4, "^"))
        self.assertIsNone(nadlezna_ovira(ovire, 6, 4, ">>^^"))
        self.assertEqual(ovire, kopija_ovir, "ne spreminjaj podanega seznama ovir!")

    def test_03_sprosti(self):
        # vrstni red mora biti ohranjen!
        global ovire

        self.assertIsNone(odstrani(ovire, [4]), "Funkcija naj ne vrača ničesar.")
        self.assertEqual(
            [(1, 1, 1), (1, 3, 3),
             (2, 6, 7), (2, 11, 12),
             (3, 9, 9),
             (5, 7, 10),
             (7, 11, 11), (7, 13, 14),
             (9, 1, 1), (9, 8, 10),
             (10, 6, 7), (10, 12, 12), (10, 14, 14),
             (11, 9, 9),
             (12, 1, 1), (12, 10, 12),
             (14, 1, 3), (14, 8, 10)
             ],
            sorted(ovire)
        )
        indeksi = list(map(kopija_ovir.index, ovire))
        self.assertEqual(sorted(indeksi), indeksi, "Vrstni red ovir se ne sme spremeniti!")
        ovire = kopija_ovir.copy()

        self.assertIsNone(odstrani(ovire, [4, 7, 11]))
        self.assertEqual(
            [(1, 1, 1), (1, 3, 3),
             (3, 9, 9),
             (7, 13, 14),
             (9, 1, 1), (9, 8, 10),
             (10, 12, 12), (10, 14, 14),
             (11, 9, 9),
             (12, 1, 1),
             (14, 1, 3), (14, 8, 10)
             ],
            sorted(ovire)
        )
        indeksi = list(map(kopija_ovir.index, ovire))
        self.assertEqual(sorted(indeksi), indeksi, "Vrstni red ovir se ne sme spremeniti!")
        ovire = kopija_ovir.copy()

        self.assertIsNone(odstrani(ovire, [4, 5]), "Funkcija naj ne vrača ničesar.")
        self.assertEqual(
            [(1, 1, 1), (1, 3, 3),
             (2, 6, 7), (2, 11, 12),
             (3, 9, 9),
             (5, 7, 10),
             (7, 11, 11), (7, 13, 14),
             (9, 1, 1), (9, 8, 10),
             (10, 6, 7), (10, 12, 12), (10, 14, 14),
             (11, 9, 9),
             (12, 1, 1), (12, 10, 12),
             (14, 1, 3), (14, 8, 10)
             ],
            sorted(ovire)
        )
        indeksi = list(map(kopija_ovir.index, ovire))
        self.assertEqual(sorted(indeksi), indeksi, "Vrstni red ovir se ne sme spremeniti!")
        ovire = kopija_ovir.copy()

        self.assertIsNone(odstrani(ovire, [15]), "Funkcija naj ne vrača ničesar.")
        self.assertEqual(ovire, kopija_ovir)
        indeksi = list(map(kopija_ovir.index, ovire))
        self.assertEqual(sorted(indeksi), indeksi, "Vrstni red ovir se ne sme spremeniti!")

        self.assertIsNone(odstrani(ovire, []), "Funkcija naj ne vrača ničesar.")
        self.assertEqual(ovire, kopija_ovir)
        indeksi = list(map(kopija_ovir.index, ovire))
        self.assertEqual(sorted(indeksi), indeksi, "Vrstni red ovir se ne sme spremeniti!")

    def test_04_najdaljsi_skok(self):
        self.assertEqual(0, najdaljsi_skok(ovire, (1, 3, 3)))
        self.assertEqual(0, najdaljsi_skok(ovire, (2, 1, 4)))
        self.assertEqual(0, najdaljsi_skok(ovire, (2, 1, 4)))
        self.assertEqual(2, najdaljsi_skok(ovire, (3, 9, 9)))
        self.assertEqual(1, najdaljsi_skok(ovire, (2, 6, 7)))
        self.assertEqual(2, najdaljsi_skok(ovire, (5, 7, 10)))
        self.assertEqual(3, najdaljsi_skok(ovire, (9, 8, 10)))
        self.assertEqual(3, najdaljsi_skok(ovire, (14, 8, 10)))
        self.assertEqual(6, najdaljsi_skok(ovire, (7, 13, 14)))
        self.assertEqual(6, najdaljsi_skok(ovire, (10, 14, 14)))
        self.assertEqual(7, najdaljsi_skok(ovire, (10, 12, 12)))
        self.assertEqual(3, najdaljsi_skok(ovire, (12, 10, 12)))

    def test_05_anarhist(self):
        k = Kolesar(ovire.copy(), 10, 4)

        self.assertEqual((10, 4), k.lokacija())
        self.assertEqual(0, k.uspesnost())

        k.premik("^")
        self.assertEqual((9, 4), k.lokacija())
        self.assertEqual(1, k.uspesnost())
        self.assertEqual(ovire, kopija_ovir, "kolesar sme spreminjati podani seznam ovir, ne pa vsebine (globalne) spremenljivke `ovire`")

        k.premik("^")
        self.assertEqual((8, 4), k.lokacija())
        self.assertEqual(1, k.uspesnost())

        k.premik("^")
        self.assertEqual((7, 4), k.lokacija())
        self.assertEqual(2, k.uspesnost())

        k.premik("^")
        self.assertEqual((6, 4), k.lokacija())
        self.assertEqual(2, k.uspesnost())

        k.premik("^")
        self.assertEqual((5, 4), k.lokacija())
        self.assertEqual(3, k.uspesnost())

        k.premik("^")
        self.assertEqual((4, 4), k.lokacija())
        self.assertEqual(3, k.uspesnost())

        k.premik(">")
        self.assertEqual((4, 5), k.lokacija())
        self.assertEqual(3, k.uspesnost())

        k.premik("v")
        self.assertEqual((5, 5), k.lokacija())
        self.assertEqual(3, k.uspesnost())

        k.premik("v")
        self.assertEqual((6, 5), k.lokacija())
        self.assertEqual(3, k.uspesnost())

        k.premik("v")
        self.assertEqual((7, 5), k.lokacija())
        self.assertEqual(3, k.uspesnost())

        k.premik("<")
        self.assertEqual((7, 4), k.lokacija())
        self.assertEqual(3, k.uspesnost())

        k.premik("<")
        self.assertEqual((7, 3), k.lokacija())
        self.assertEqual(3, k.uspesnost())

        k.premik("v")
        self.assertEqual((8, 3), k.lokacija())
        self.assertEqual(3, k.uspesnost())

        k.premik("v")
        self.assertEqual((9, 3), k.lokacija())
        self.assertEqual(3, k.uspesnost())

        k.premik("v")
        self.assertEqual((10, 3), k.lokacija())
        self.assertEqual(3, k.uspesnost())

        k.premik("<")
        self.assertEqual((10, 2), k.lokacija())
        self.assertEqual(3, k.uspesnost())

        k.premik("^")
        self.assertEqual((9, 2), k.lokacija())
        self.assertEqual(3, k.uspesnost())

        k.premik("<")
        self.assertEqual((9, 1), k.lokacija())
        self.assertEqual(4, k.uspesnost())

        k.premik("^")
        self.assertEqual((8, 1), k.lokacija())
        self.assertEqual(4, k.uspesnost())

        k.premik("^")
        self.assertEqual((7, 1), k.lokacija())
        self.assertEqual(4, k.uspesnost())


if __name__ == "__main__":
    unittest.main()
