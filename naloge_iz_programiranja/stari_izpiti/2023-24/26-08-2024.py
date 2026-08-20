
import unittest
from operator import index


def po_urah(a):
    seznam = []
    vsota = 0
    x = 0
    for ura in range(1, 25):
        for prehod in range(x, 60 * ura):
            vsota += a[prehod]
        seznam.append(vsota)
        x += 60
        vsota = 0
    return seznam

def naj_ura(a):
    seznam = po_urah(a)
    terke = []
    for i, prehodi in enumerate(seznam):
        terke.append((i, prehodi))
    return max(terke, key=lambda terka: terka[1])[0]

def naj_ura(a):
    return max([i for i in enumerate(po_urah(a))], key=lambda ura: ura[1])[0]

def brez_prehodov(a):
    st_0 = 0
    for prehod in a:
        if prehod == 0:
            st_0 += 1
    return st_0

def brez_prehodov(a):
    return sum(1 for el in a if el == 0)

def obdobje_brez(a):
    zacetek_obdobja = False
    dolzina_obdobja = 0
    dolzine = []
    for i, prehod in enumerate(a):
        if prehod == 0 and zacetek_obdobja is False:
            dolzina_obdobja += 1
            start = i
            zacetek_obdobja = True
        elif prehod == 0 and zacetek_obdobja is True:
            dolzina_obdobja += 1
            continue
        elif prehod != 0 and zacetek_obdobja is True:
            zacetek_obdobja = False
            dolzine.append((start, i - 1, dolzina_obdobja))
            dolzina_obdobja = 0

    #tole je pomembno saj azjema robni primer, kjer je najdaljse obdobje od nekega i-ja do konca seznama!
    if zacetek_obdobja:
        dolzine.append((start, len(a) - 1, dolzina_obdobja))

    najvecje_obdobje = max(dolzine, key=lambda podatki: podatki[2])
    return najvecje_obdobje[0:2]

def obremenitve(imena, porocila):
    return






class Test(unittest.TestCase):
    a = [0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 1,
         2, 0, 0, 2, 0, 0, 2, 2, 2, 0, 1, 0, 0, 0, 2, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 1, 1, 0, 0, 0,
         0, 2, 0, 0, 2, 0, 0, 2, 0, 0, 0, 2, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 1, 0, 1, 2, 1, 1, 1, 0,
         0, 1, 0, 0, 2, 2, 1, 1, 0, 3, 0, 1, 2, 1, 0, 1, 0, 0, 0, 0, 3, 1, 1, 2, 1, 2, 1, 1, 0, 2, 2, 0, 1, 2, 1, 1,
         1, 0, 2, 1, 1, 1, 1, 1, 2, 1, 1, 2, 1, 1, 1, 0, 0, 2, 1, 0, 4, 2, 1, 3, 1, 1, 1, 1, 0, 1, 1, 2, 0, 1, 1, 1,
         1, 1, 1, 0, 2, 1, 0, 1, 2, 2, 1, 2, 1, 2, 1, 1, 0, 1, 1, 1, 0, 1, 1, 1, 2, 2, 1, 2, 1, 2, 0, 2, 2, 4, 2, 3,
         1, 2, 3, 0, 1, 1, 3, 1, 1, 2, 2, 0, 2, 3, 2, 2, 2, 0, 0, 1, 1, 1, 1, 2, 4, 1, 0, 2, 2, 3, 2, 1, 1, 2, 2, 2,
         2, 1, 2, 1, 2, 3, 3, 1, 2, 3, 2, 2, 2, 2, 1, 0, 4, 2, 2, 2, 2, 1, 2, 3, 1, 2, 1, 2, 2, 2, 2, 3, 2, 3, 2, 0,
         3, 0, 3, 0, 1, 1, 2, 3, 3, 0, 3, 4, 2, 3, 1, 3, 2, 2, 1, 2, 2, 2, 2, 1, 1, 1, 2, 4, 3, 3, 2, 0, 2, 1, 1, 2,
         4, 2, 3, 3, 0, 2, 1, 4, 3, 2, 2, 0, 2, 3, 2, 2, 1, 2, 0, 4, 4, 2, 1, 3, 1, 2, 2, 2, 2, 4, 2, 3, 2, 3, 3, 2,
         3, 4, 2, 1, 4, 2, 3, 5, 3, 2, 3, 5, 3, 4, 1, 2, 5, 3, 5, 4, 4, 2, 3, 3, 5, 3, 4, 3, 3, 3, 3, 4, 4, 4, 4, 4,
         4, 4, 4, 5, 3, 4, 3, 3, 2, 4, 4, 4, 2, 2, 5, 4, 4, 4, 3, 3, 3, 3, 4, 3, 4, 4, 7, 4, 6, 5, 4, 5, 4, 4, 1, 4,
         5, 5, 4, 6, 3, 4, 3, 5, 4, 5, 4, 5, 4, 2, 4, 5, 5, 3, 2, 4, 5, 3, 4, 4, 6, 4, 7, 4, 4, 5, 3, 6, 5, 7, 5, 4,
         5, 7, 5, 5, 5, 5, 4, 7, 5, 6, 5, 3, 4, 7, 7, 5, 6, 4, 5, 4, 7, 5, 4, 7, 7, 6, 7, 4, 5, 8, 5, 8, 6, 7, 6, 3,
         6, 7, 4, 7, 6, 5, 6, 6, 5, 5, 6, 5, 7, 7, 7, 6, 7, 6, 8, 7, 5, 6, 8, 7, 7, 6, 6, 8, 6, 6, 6, 6, 7, 8, 6, 6,
         8, 7, 6, 6, 7, 6, 6, 6, 7, 6, 8, 8, 9, 9, 9, 9, 7, 9, 8, 7, 9, 7, 7, 8, 8, 8, 7, 7, 7, 9, 9, 7, 8, 6, 9, 8,
         7, 8, 8, 7, 8, 8, 9, 8, 7, 7, 8, 7, 7, 7, 8, 9, 9, 7, 6, 6, 9, 7, 6, 8, 9, 8, 8, 8, 9, 7, 9, 6, 7, 8, 9,
         10, 8, 7, 9, 7, 8, 10, 7, 8, 10, 8, 10, 8, 7, 8, 10, 10, 7, 10, 8, 7, 9, 9, 9, 10, 7, 9, 9, 9, 8, 9, 10,
         10, 9, 10, 9, 7, 10, 9, 8, 11, 9, 9, 10, 8, 9, 9, 11, 11, 11, 9, 10, 11, 9, 9, 8, 10, 9, 9, 10, 11, 8, 12,
         10, 10, 10, 8, 9, 9, 10, 10, 9, 9, 9, 12, 10, 8, 9, 10, 11, 9, 10, 10, 10, 9, 8, 9, 9, 12, 9, 9, 8, 8, 8,
         8, 8, 9, 11, 9, 8, 8, 10, 10, 8, 8, 8, 9, 8, 7, 8, 8, 8, 9, 7, 10, 10, 7, 8, 9, 10, 7, 8, 9, 9, 6, 9, 9, 9,
         8, 8, 9, 8, 8, 9, 10, 9, 10, 9, 8, 9, 6, 7, 9, 8, 9, 9, 6, 8, 7, 7, 6, 8, 10, 9, 8, 7, 6, 7, 9, 8, 10, 9,
         6, 8, 8, 7, 9, 8, 10, 7, 6, 7, 10, 9, 8, 7, 8, 8, 7, 9, 9, 8, 9, 8, 6, 7, 7, 8, 8, 8, 8, 9, 9, 7, 9, 6, 8,
         8, 8, 6, 8, 7, 8, 7, 8, 8, 6, 8, 8, 6, 7, 8, 5, 7, 7, 8, 8, 8, 8, 7, 7, 7, 7, 8, 7, 6, 7, 6, 8, 5, 8, 7, 6,
         8, 8, 9, 8, 6, 7, 7, 7, 7, 8, 6, 7, 7, 7, 7, 6, 8, 7, 7, 6, 7, 7, 8, 7, 7, 7, 6, 8, 7, 7, 5, 6, 7, 8, 7, 5,
         5, 6, 6, 8, 7, 7, 7, 7, 7, 7, 6, 6, 6, 6, 5, 7, 7, 6, 7, 6, 7, 6, 5, 7, 7, 6, 7, 7, 6, 7, 9, 6, 9, 7, 7, 8,
         7, 6, 6, 6, 6, 10, 8, 5, 9, 6, 6, 8, 7, 8, 7, 8, 8, 9, 9, 7, 8, 9, 6, 7, 8, 8, 7, 8, 8, 7, 7, 7, 8, 9, 8,
         7, 8, 8, 8, 7, 8, 8, 8, 9, 8, 8, 8, 10, 12, 7, 8, 10, 9, 7, 7, 7, 8, 10, 7, 8, 9, 8, 8, 7, 6, 8, 8, 9, 9,
         9, 9, 9, 9, 7, 9, 9, 8, 9, 10, 7, 9, 8, 10, 8, 9, 7, 8, 8, 10, 10, 8, 8, 8, 10, 9, 10, 10, 9, 9, 9, 10, 11,
         8, 7, 10, 9, 8, 9, 9, 12, 9, 10, 8, 10, 11, 9, 10, 10, 11, 9, 7, 10, 11, 10, 9, 10, 10, 9, 9, 7, 10, 9, 9,
         10, 9, 9, 8, 10, 8, 11, 8, 6, 8, 9, 8, 8, 10, 6, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 8, 9, 8, 9, 10, 8, 9, 7, 9,
         7, 7, 9, 6, 8, 10, 9, 9, 7, 7, 8, 9, 9, 8, 9, 8, 6, 8, 7, 9, 8, 7, 8, 10, 9, 6, 7, 6, 9, 8, 9, 8, 8, 7, 8,
         8, 8, 8, 7, 7, 7, 8, 6, 9, 7, 6, 5, 8, 7, 8, 7, 8, 8, 8, 5, 8, 8, 7, 5, 8, 7, 8, 7, 7, 7, 5, 6, 7, 7, 7, 7,
         7, 5, 7, 7, 6, 6, 8, 6, 5, 6, 8, 7, 6, 7, 7, 6, 7, 6, 8, 6, 8, 7, 5, 6, 5, 7, 6, 5, 6, 8, 7, 5, 6, 4, 6, 5,
         6, 6, 8, 7, 5, 4, 6, 8, 4, 5, 7, 4, 7, 7, 6, 6, 5, 6, 6, 5, 5, 7, 6, 5, 5, 5, 7, 5, 5, 6, 8, 5, 5, 5, 6, 5,
         5, 6, 4, 5, 6, 6, 5, 2, 6, 5, 4, 4, 3, 5, 7, 6, 6, 5, 4, 5, 5, 7, 4, 3, 7, 5, 4, 6, 4, 5, 5, 4, 4, 6, 5, 4,
         3, 4, 4, 5, 5, 4, 3, 4, 4, 5, 5, 5, 5, 4, 4, 4, 4, 3, 4, 5, 3, 3, 5, 3, 4, 4, 5, 4, 4, 3, 4, 4, 5, 3, 5, 5,
         5, 4, 2, 4, 4, 3, 2, 3, 5, 5, 3, 4, 5, 2, 4, 3, 4, 1, 3, 2, 2, 4, 3, 3, 3, 3, 2, 3, 4, 2, 2, 3, 4, 2, 4, 0,
         3, 3, 3, 1, 2, 2, 3, 3, 2, 1, 2, 3, 3, 2, 2, 2, 1, 1, 1, 2, 2, 2, 3, 1, 1, 0, 2, 0, 1, 1, 3, 1, 0, 0, 0, 2,
         2, 3, 3, 2, 1, 1, 2, 1, 2, 2, 1, 2, 1, 2, 2, 1, 1, 2, 1, 0, 2, 1, 2, 0, 1, 2, 0, 1, 0, 2, 0, 1, 2, 1, 1, 0,
         0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 1, 0]

    po_urah = [20, 34, 66, 82, 114, 125, 204, 272, 364, 453, 522,
               556, 494, 452, 407, 443, 514, 544, 464, 381, 317, 231, 118, 36]

    def test_1_statistika(self):
        self.assertEqual(list(self.po_urah), list(po_urah(self.a)))
        self.assertEqual(11, naj_ura(self.a))
        self.assertEqual(153, brez_prehodov(self.a))

    def test_2_obdobje_brez(self):
        #                                      0  1  2  3  4  5  6  7  8  9  0  1  2
        self.assertEqual((5, 8), obdobje_brez([0, 0, 1, 2, 3, 0, 0, 0, 0, 1, 2, 0, 0]))
        self.assertEqual((0, 2), obdobje_brez([0, 0, 0, 2, 3, 1, 2, 0, 0, 1, 2, 0, 0]))
        self.assertEqual((7, 12), obdobje_brez([0, 0, 0, 2, 3, 1, 2, 0, 0, 0, 0, 0, 0]))
        self.assertEqual((1421, 1436), obdobje_brez(self.a))

    def test_3_obremenitve(self):
        imena = ["Anina ulica", "Bertin trg", "Cilkina cesta", "Ulica Dani Beznikove"]
        porocila = [10, 2, 5, 10, 3, 5, 3, 4, 5, 2, 3, 4, 2, 1, 2, 6, 8, 1, 2, 3]
        self.assertEqual("Anina ulica", obremenitve(imena, porocila))

        porocila = [3, 5, 3, 4, 3, 6, 3, 4]
        self.assertEqual("Bertin trg", obremenitve(imena, porocila))

        imena = ["Anina ulica", "Bertin trg"]
        self.assertEqual("Bertin trg", obremenitve(imena, porocila))

        imena = list("abcdefghi")
        porocila = list(range(len(imena) * 5))
        self.assertEqual("i", obremenitve(imena, porocila))

    def test_4_zlata_minuta(self):
        self.assertTrue(zlata_minuta(42, self.a))
        self.assertFalse(zlata_minuta(420, self.a))
        self.assertTrue(zlata_minuta(421, self.a))
        self.assertTrue(zlata_minuta(1017, self.a))
        self.assertTrue(zlata_minuta(1018, self.a))
        self.assertTrue(zlata_minuta(952, self.a))
        self.assertTrue(zlata_minuta(953, self.a))
        self.assertFalse(zlata_minuta(1000, self.a))

    def test_5a_senzor(self):
        anina = Senzor(42)
        bertin = Senzor(55)

        anina.prehod("+")
        anina.prehod("+")
        anina.prehod("-")
        anina.prehod("+")
        bertin.prehod("+")

        self.assertEqual((3, 1), anina.prehodov())
        self.assertEqual((1, 0), bertin.prehodov())

    def test_5b_nadzorni_sistem(self):
        anina = Senzor(42)
        bertin = Senzor(55)
        cilkina = Senzor(66)

        nadzor = NadzorniSistem([anina, bertin, cilkina])
        nadzor.prehod(42, "+")
        nadzor.prehod(55, "-")
        nadzor.prehod(55, "+")
        nadzor.prehod(42, "+")
        nadzor.prehod(42, "+")
        nadzor.prehod(55, "-")
        anina.prehod("-")

        self.assertEqual((3, 1), nadzor.prehodov(42))
        self.assertEqual((1, 2), nadzor.prehodov(55))
        self.assertEqual((0, 0), nadzor.prehodov(66))

        self.assertEqual((3, 1), anina.prehodov())


if __name__ == "__main__":
    unittest.main()
