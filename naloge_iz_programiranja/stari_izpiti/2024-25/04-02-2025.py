


import unittest
import random
from collections import defaultdict, Counter
from itertools import pairwise


def se_dotika(ovira1, ovira2):
    x0, y0, x1, y1 = ovira1
    a0, b0, a1, b1 = ovira2
    return ((x0 <= a0 <= x1) or (a0 <= x0 <= a1)) and ((y0 <= b0 <= y1) or (b0 <= y0 <= b1))

def poisci_oviro(x, y, ovire):
    for x0, y0, x1, y1 in ovire:
        if x0 <= x < x1 and y0 <= y < y1:
            return (x0, y0, x1, y1)
    return None

def mozna_pot(x, y, pot, ovire):
    for char in pot:
        if char == ">":
            x += 1
        elif char == "<":
            x -= 1
        elif char == "v":
            y += 1
        else:
            y -= 1

        if poisci_oviro(x, y, ovire):
            return False
        else:
            continue
    return True

def zdruzljivi(ovira1, ovira2):
    x0, y0, x1, y1 = ovira1
    a0, b0, a1, b1 = ovira2

    # navpično sosednji (ena nad drugo): rob se dotika, x-razpona se popolnoma ujemata
    if (y1 == b0 or b1 == y0) and x0 == a0 and x1 == a1:
        return True

    # vodoravno sosednji (ena poleg druge): rob se dotika, y-razpona se popolnoma ujemata
    if (x1 == a0 or a1 == x0) and y0 == b0 and y1 == b1:
        return True

    return False

def zdruzi(ovira1, ovira2):
    x0, y0, x1, y1 = ovira1
    a0, b0, a1, b1 = ovira2
    return min(x0, a0), min(y0, b0), max(x1, a1), max(y1, b1)

def poenostavi(ovire):
    i = 0
    while i < len(ovire) - 1:
        if zdruzljivi(ovire[i], ovire[i + 1]):
            ovire[i] = zdruzi(ovire[i], ovire[i + 1])
            del ovire[i + 1]
        else:
            i += 1

def kisel_dez(ovire, plohe):
    slovar = defaultdict(int)
    for ovira in ovire:
        for ploha in plohe:
            x, y = ploha
            x0, y0, x1, y1 = ovira
            if x0 <= x < x1 and y0 <= y < y1:
                slovar[ovira] += 1

    mnozica_neuporabnih = set()
    for ovira, st in slovar.items():
        if st >= 3:
            mnozica_neuporabnih.add(ovira)

    return set(ovire) - mnozica_neuporabnih

def _brez_blata(trenutna, cilj, dovoljene_ovire, obiskane):
    if trenutna == cilj:
        return True

    obiskane.add(trenutna)
    for ovira in dovoljene_ovire:
        if se_dotika(trenutna, ovira) and ovira not in obiskane:
            if _brez_blata(ovira, cilj, dovoljene_ovire, obiskane):
                return True
    return False

def brez_blata(start, cilj, dovoljene_ovire):
    return _brez_blata(start, cilj, dovoljene_ovire, set())


class Ovira:
    def __init__(self, x0, y0, x1, y1):
        self.x0 = x0
        self.y0 = y0
        self.x1 = x1
        self.y1 = y1
        self.stevilo_ploh = 0

    def ploscina(self):
        return (self.x1 - self.x0) * (self.y1 - self.y0)

    def ploha(self, x, y):
        if self.x0 <= x < self.x1 and self.y0 <= y < self.y1:
            self.stevilo_ploh += 1

    def uporabna(self):
        if self.stevilo_ploh < 3:
            return True
        return False

    def razdeli_x(self, x):
        if self.x0 < x < self.x1:
            n1 = Ovira(self.x0, self.y0, x, self.y1)
            n2 = Ovira(x, self.y0, self.x1, self.y1)
            return n1, n2
        return None

    def razdeli_y(self, y):
        if self.y0 < y < self.y1:
            n1 = Ovira(self.x0, self.y0, self.x1, y)
            n2 = Ovira(self.x0, y, self.x1, self.y1)
            return n1, n2
        return None








ovire_list = [
    (3, 7, 5, 9),  # 0
    (2, 7, 3, 9),

    (8, 7, 10, 8),
    (9, 8, 10, 9),

    (6, 0, 7, 1),

    (0, 5, 2, 6), # 5
    (2, 5, 3, 6),

    (9, 4, 10, 5),

    (7, 1, 8, 2),
    (8, 1, 10, 2),
    (7, 2, 10, 3),  # 10

    (6, 5, 7, 6),
    (7, 5, 8, 6),
    (6, 6, 7, 7),

    (2, 3, 5, 4),
    (2, 1, 5, 3), # 15
    (1, 1, 2, 4),

    (7, 9, 8, 10),
    (6, 9, 7, 10)
]

o0, o1, o2, o3, o4, o5, o6, o7, o8, o9, o10, \
    o11, o12, o13, o14, o15, o16, o17, o18 = ovire_list

ovire = set(ovire_list)

class Test(unittest.TestCase):
    def test_0_se_dotika(self):
        self.assertTrue(se_dotika(o4, o8))
        self.assertTrue(se_dotika(o8, o4))
        self.assertTrue(se_dotika(o8, o9))
        self.assertTrue(se_dotika(o9, o8))
        self.assertTrue(se_dotika(o8, o10))
        self.assertTrue(se_dotika(o10, o8))
        self.assertTrue(se_dotika(o12, o13))
        self.assertTrue(se_dotika(o13, o12))

        self.assertFalse(se_dotika(o0, o2))
        self.assertFalse(se_dotika(o4, o9))
        self.assertFalse(se_dotika(o5, o15))
        self.assertFalse(se_dotika(o6, o16))
        self.assertFalse(se_dotika(o5, o16))

        self.assertTrue(se_dotika((8, 3, 9, 7), o2))
        self.assertTrue(se_dotika(o2, (8, 3, 9, 7)))
        self.assertTrue(se_dotika(o10, (8, 3, 9, 7)))
        self.assertTrue(se_dotika((8, 3, 9, 7), o10))

    def test_1(self):
        self.assertTrue(mozna_pot(0, 0, ">>>>>v>vv>>vvv<v<<^<<<<<", ovire))
        self.assertTrue(mozna_pot(3, 4, "<", ovire))
        self.assertTrue(mozna_pot(3, 4, "", ovire))

        self.assertFalse(mozna_pot(3, 4, "^", ovire))
        self.assertFalse(mozna_pot(3, 4, "vvv", ovire))
        self.assertFalse(mozna_pot(2, 4, "vv", ovire))
        self.assertFalse(mozna_pot(5, 5, ">", ovire))

        self.assertFalse(mozna_pot(0, 0, ">>>v>>v>vv>>vvv<v<<^<<<<<", ovire))
        self.assertFalse(mozna_pot(0, 0, ">>>>>v<>vv>>vvv<v<<^<<<<<", ovire))
        self.assertFalse(mozna_pot(0, 0, ">>>>>v>>vv>>vvv<v<<^<<<<<", ovire))
        self.assertFalse(mozna_pot(0, 0, ">>>>>v>vvvv>>vvv<v<<^<<<<<", ovire))

    def test_2a_zdruzljivi(self):
        self.assertTrue(zdruzljivi(o0, o1))
        self.assertTrue(zdruzljivi(o1, o0))
        self.assertTrue(zdruzljivi(o11, o13))
        self.assertTrue(zdruzljivi(o13, o11))

        self.assertFalse(zdruzljivi(o0, o2))
        self.assertFalse(zdruzljivi(o12, o13))
        self.assertFalse(zdruzljivi(o13, o12))
        self.assertFalse(zdruzljivi(o15, o16))
        self.assertFalse(zdruzljivi(o16, o15))
        self.assertFalse(zdruzljivi(o16, o14))
        self.assertFalse(zdruzljivi(o14, o16))
        self.assertFalse(zdruzljivi(o9, o10))
        self.assertFalse(zdruzljivi(o10, o9))
        self.assertFalse(zdruzljivi(o8, o10))
        self.assertFalse(zdruzljivi(o10, o8))

    def test_2b_zdruzi(self):
        self.assertEqual((2, 7, 5, 9), zdruzi(o0, o1))
        self.assertEqual((2, 7, 5, 9), zdruzi(o1, o0))

        self.assertEqual((6, 9, 8, 10), zdruzi(o18, o17))
        self.assertEqual((6, 9, 8, 10), zdruzi(o17, o18))

        self.assertEqual((2, 1, 5, 4), zdruzi(o15, o14))
        self.assertEqual((2, 1, 5, 4), zdruzi(o14, o15))
        o14_15 = zdruzi(o14, o15)
        self.assertEqual((1, 1, 5, 4), zdruzi(o14_15, o16))
        self.assertEqual((1, 1, 5, 4), zdruzi(o16, o14_15))

        self.assertEqual((6, 9, 8, 10), zdruzi(o17, o18))
        self.assertEqual((6, 9, 8, 10), zdruzi(o18, o17))

    def test_2c_poenostavi(self):
        o = ovire_list.copy()
        poenostavi(o)
        self.assertEqual(
            [(2, 7, 5, 9),
             o2, o3, o4,
             (0, 5, 3, 6),
             o7, # 5
             (7, 1, 10, 3),
             (6, 5, 8, 6),
             o13,
             (1, 1, 5, 4),
             (6, 9, 8, 10)],
            o
        )

    def test_3(self):
        plohe = [
            (7, 2), (7, 2), (8, 2), (8, 2),  # o10
            (2, 1), (3, 1), (4, 2),  # o15
            (6, 0), (6, 0), (6, 0),  # o4
            (2, 3), (2, 3),  # o14, a ostane
            (5, 6),  # o11, ostane
            (8, 7), (9, 7),  # o2
            (7, 9),
            (0, 0),
            (4, 6),
        ]
        for _ in range(10):
            random.shuffle(plohe)
            o = ovire.copy()
            ostanek = kisel_dez(o, plohe)
            self.assertEqual(o, ovire, "Funkcija ne sme spreminjati podane množice temveč vrniti novo!")
            self.assertEqual(ostanek, ovire - {o10, o15, o4})

    def test_4_brez_blata(self):
        o = ovire | {(8, 3, 9, 7)}
        self.assertTrue(brez_blata(o3, o4, o))
        self.assertTrue(brez_blata(o4, o3, o))
        self.assertTrue(brez_blata(o4, o13, o))
        self.assertTrue(brez_blata(o13, o4, o))

        self.assertFalse(brez_blata(o4, o16, o))
        self.assertFalse(brez_blata(o16, o4, o))
        self.assertFalse(brez_blata(o16, o0, o))
        self.assertFalse(brez_blata(o0, o16, o))
        self.assertFalse(brez_blata(o0, o7, o))
        self.assertFalse(brez_blata(o7, o0, o))

    def test_5a_ovira(self):
        ovira5 = Ovira(2, 1, 5, 3)
        self.assertTrue(ovira5.uporabna())
        ovira5.ploha(2, 1)
        self.assertTrue(ovira5.uporabna())
        ovira5.ploha(5, 3)
        ovira5.ploha(10, 8)
        ovira5.ploha(3, 7)
        self.assertTrue(ovira5.uporabna())
        ovira5.ploha(2, 2)
        self.assertTrue(ovira5.uporabna())
        ovira5.ploha(4, 2)
        self.assertFalse(ovira5.uporabna())
        ovira5.ploha(4, 2)
        self.assertFalse(ovira5.uporabna())

    def test_5b_ovira(self):
        ovira5 = Ovira(2, 1, 5, 3)

        self.assertEqual(6, ovira5.ploscina())
        o5a, o5b = ovira5.razdeli_x(3)
        self.assertEqual(2, o5a.ploscina())
        self.assertEqual(4, o5b.ploscina())

        self.assertEqual(6, ovira5.ploscina())
        o5a, o5b = ovira5.razdeli_y(2)
        self.assertEqual(3, o5a.ploscina())
        self.assertEqual(3, o5b.ploscina())

        self.assertIsNone(ovira5.razdeli_x(0))
        self.assertIsNone(ovira5.razdeli_x(2))
        self.assertIsNone(ovira5.razdeli_x(5))
        self.assertIsNone(ovira5.razdeli_x(6))

        self.assertIsNone(ovira5.razdeli_y(1))
        self.assertIsNone(ovira5.razdeli_y(3))


if __name__ == "__main__":
    unittest.main()
