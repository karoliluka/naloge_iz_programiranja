import unittest
from collections import defaultdict


def preberi_strele(ime_datoteke):
    seznam_trojk = []
    with open(ime_datoteke, "r", encoding="utf-8") as datoteka:
        for vrstica in datoteka:
            ime = vrstica.strip().split(": ")[0]
            x, y = float(vrstica.strip().split(": ")[1].strip().split(", ")[0]), float(vrstica.strip().split(": ")[1].strip().split(", ")[1])
            seznam_trojk.append((ime, x, y))
    return seznam_trojk

def najboljsi_strelec(streli, pravokotniki):
    slovar_strelcev = defaultdict(int)

    # zabelezimo vse strelce
    for ime, x, y in streli:
        slovar_strelcev[ime] += 0

    for ime, x, y in streli:
        for x1, y1, x2, y2 in pravokotniki:
            if x1 <= x <= x2 and y1 <= y <= y2:
                slovar_strelcev[ime] += 1
                break

    if not slovar_strelcev:
        return None

    return sorted(slovar_strelcev, key=lambda rez: (-slovar_strelcev[rez], rez))[0]

def odstrani_zadete(x, y, pravokotniki):
    kopija_pravokotnikov = pravokotniki.copy()
    for x1, y1, x2, y2 in kopija_pravokotnikov:
        if x1 <= x <= x2 and y1 <= y <= y2:
            pravokotniki.remove((x1, y1, x2, y2))

def vsi_dosegljivi(zacetek, prekrivanja):
    dosegljivi = {zacetek}
    for otrok in prekrivanja[zacetek]:
        dosegljivi |= vsi_dosegljivi(otrok, prekrivanja)
    return dosegljivi

def naj_levo(zacetek, pravokotniki, prekrivanja):
    mnozica_indeskov = vsi_dosegljivi(zacetek, prekrivanja)
    najmanjsi = float("inf")
    for indeks in mnozica_indeskov:
        x1 = pravokotniki[indeks][0]
        if x1 < najmanjsi:
            najmanjsi = x1
    return najmanjsi

class Turnir:
    def __init__(self, seznam_pravokotnikov):
        self.seznam_pravokotnikov = seznam_pravokotnikov
        self.seznam_strelov = []

    def strel(self, x, y):
        self.seznam_strelov.append((x, y))

    def zadetkov(self, x1, y1, x2, y2):
        st_zadetkov = 0
        for strel in self.seznam_strelov:
            if x1 <= strel[0] <= x2 and y1 <= strel[1] <= y2:
                st_zadetkov += 1
        return st_zadetkov

class Test(unittest.TestCase):
    pravokotniki = [(0, 1, 4, 3),
                    (0, 6, 1, 8),
                    (2, 2, 7, 6),
                    (3, 4, 6, 5),
                    (5, 1, 9, 7),
                    (8, 0, 10, 2),
                    (8, 3, 10, 5),
                    (8, 6, 11, 8)]

    def test_01_preberi_strele(self):
        self.assertEqual(
            preberi_strele("streli.txt"),
            [("Ana", 0.55, 3.14), ("Berta", 5.5, 4.5), ("Ana", 6.5, 6.5), ("Cilka", 10.3, 6.3)])

    def test_02_najboljsi_strelec(self):
        self.assertEqual(najboljsi_strelec(
            [("Ana", 1.5, 1.5), ("Berta", 4.4, 1.4), ("Berta", 6, 4), ("Ana", 9, 7)], self.pravokotniki),
            "Ana")
        self.assertEqual(najboljsi_strelec(
            [("Berta", 6, 4), ("Ana", 1.5, 1.5), ("Berta", 4.4, 1.4), ("Ana", 9, 7)], self.pravokotniki),
            "Ana")
        self.assertEqual(najboljsi_strelec(
            [("Ana", 1.5, 1.5), ("Berta", 4.4, 1.4), ("Berta", 6, 4), ("Ana", 9, 7), ("Berta", 9, 7)], self.pravokotniki),
            "Ana")
        self.assertEqual(najboljsi_strelec(
            [("Ana", 1.5, 1.5), ("Berta", 4.4, 1.4), ("Berta", 6, 4), ("Berta", 9, 7)], self.pravokotniki),
            "Berta")
        self.assertEqual(najboljsi_strelec(
            [("Ana", 1.5, 1.5), ("Berta", 4.4, 1.4), ("Berta", 6, 4), ("Berta", 9, 7), ("Ana", 9, 7)], self.pravokotniki),
            "Ana")

        self.assertEqual(najboljsi_strelec(
            [("Ana", 0, 0)], self.pravokotniki),
            "Ana")

    def test_03_odstrani_zadete(self):
        prav1 = self.pravokotniki[:]
        self.assertIsNone(odstrani_zadete(5.5, 4.5, prav1))
        self.assertEqual(prav1, self.pravokotniki[:2] + self.pravokotniki[5:])

        prav1 = self.pravokotniki[:]
        self.assertIsNone(odstrani_zadete(5.5, 5.5, prav1))
        self.assertEqual(prav1, self.pravokotniki[:2] + [self.pravokotniki[3]] + self.pravokotniki[5:])

        prav1 = self.pravokotniki[:]
        self.assertIsNone(odstrani_zadete(0, 0, prav1))
        self.assertEqual(prav1, self.pravokotniki)

        prav1 = self.pravokotniki[:]
        self.assertIsNone(odstrani_zadete(2.5, 2.5, prav1))
        self.assertEqual(prav1, self.pravokotniki[1:2] + self.pravokotniki[3:])

    def test_04_naj_levo(self):
        prekrivanja = {3: (2,), 2: (0, 4), 4: (5, 6, 7), 1: (), 0: (), 5: (),
                       6: (), 7: ()}
        pravokotniki = self.pravokotniki
        self.assertEqual(naj_levo(3, pravokotniki, prekrivanja), 0)
        self.assertEqual(naj_levo(4, pravokotniki, prekrivanja), 5)
        self.assertEqual(naj_levo(2, pravokotniki, prekrivanja), 0)
        self.assertEqual(naj_levo(0, pravokotniki, prekrivanja), 0)
        self.assertEqual(naj_levo(1, pravokotniki, prekrivanja), 0)
        self.assertEqual(naj_levo(5, pravokotniki, prekrivanja), 8)

        prekrivanja = {3: (2,), 2: (4, ), 4: (5, 6, 7), 1: (), 0: (2, ), 5: (),
                       6: (), 7: ()}
        self.assertEqual(naj_levo(3, pravokotniki, prekrivanja), 2)
        self.assertEqual(naj_levo(4, pravokotniki, prekrivanja), 5)
        self.assertEqual(naj_levo(2, pravokotniki, prekrivanja), 2)
        self.assertEqual(naj_levo(0, pravokotniki, prekrivanja), 0)
        self.assertEqual(naj_levo(1, pravokotniki, prekrivanja), 0)
        self.assertEqual(naj_levo(5, pravokotniki, prekrivanja), 8)

        prekrivanja = {3: (2,), 2: (4, ), 4: (6, 7), 1: (), 0: (2, ), 5: (4, ),
                       6: (), 7: ()}
        self.assertEqual(naj_levo(5, pravokotniki, prekrivanja), 5)

        prav1 = pravokotniki[:]
        prav1[0] = (2, 1, 4, 3)  # levi rob se premakne na 2
        prav1[2] = (1, 2, 6, 5)  # levi rob se premakne na 1
        prav1[3] = (3, 2, 6, 5)  # gornji rob gre na 2
        prekrivanja = {3: (0, 4), 4: (2, 6, 7), 2: (), 1: (), 0: (), 5: (4, ), 6: (), 7: ()}

        # črv mora iz 3 na 4 in potem na 2, ker se 0 ne dotika 2 (vmes je ... emm zrak)
        self.assertEqual(naj_levo(3, prav1, prekrivanja), 1)

        # 5 -> 4 -> 2
        self.assertEqual(naj_levo(5, prav1, prekrivanja), 1)

        # ne more nikamor
        self.assertEqual(naj_levo(6, prav1, prekrivanja), 8)

    def test_05_turnir(self):
        turnir = Turnir(self.pravokotniki)
        turnir.strel(2.5, 2.5)
        turnir.strel(1.5, 2.5)
        turnir.strel(5.5, 4.1)
        self.assertEqual(turnir.zadetkov(0, 1, 4, 3), 2)
        self.assertEqual(turnir.zadetkov(0, 6, 1, 8), 0)
        self.assertEqual(turnir.zadetkov(2, 2, 7, 6), 2)
        self.assertEqual(turnir.zadetkov(3, 4, 6, 5), 1)


if __name__ == "__main__":
    unittest.main()
