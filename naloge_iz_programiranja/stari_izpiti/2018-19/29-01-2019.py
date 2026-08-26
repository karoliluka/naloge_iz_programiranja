import unittest
from collections import defaultdict


def preberi_pravokotnike(ime_datoteke):
    seznam_cetverk = []
    with open(ime_datoteke, "r", encoding="utf-8") as datoteka:
        for vrstica in datoteka:
            xs = vrstica.strip().split(" - ")[0]
            ys = vrstica.strip().split(" - ")[1]
            x0, y0 = xs.strip().split(",")[0], xs.strip().split(",")[1]
            x1, y1 = ys.strip().split(",")[0], ys.strip().split(",")[1]
            seznam_cetverk.append((int(x0), int(y0), int(x1), int(y1)))
    return seznam_cetverk

def nepokrito(pravokotniki, sirina, visina):
    unikati = set()
    for x0, y0, x1, y1 in pravokotniki:
        for x in range(x0, x1):
            for y in range(y0, y1):
                unikati.add((x, y))

    return  (sirina * visina) - len(unikati)

def odstrani_zgresene(streli, pravokotniki):
    mnozica_zadetih = set()
    for x_s, y_s in streli:
        for x0, y0, x1, y1 in pravokotniki:
            if x0 <= x_s <= x1 and y0 <= y_s <= y1:
                mnozica_zadetih.add((x_s, y_s))
    streli[:] = sorted(list(mnozica_zadetih))

def je_zlata(stevilka, barve, pravokotniki):
    if barve[stevilka] == 'zlata':
        return True

    if barve[stevilka] != 'zlata' and pravokotniki[stevilka] != ():
        for number in pravokotniki[stevilka]:
                if je_zlata(number, barve, pravokotniki):
                    return True
    return False

class Pravokotnik:
    def __init__(self, x0, y0, x1, y1):
        self.x0 = x0
        self.y0 = y0
        self.x1 = x1
        self.y1 = y1
        self.slovar_strelcev = defaultdict(int)
        self.st_zadetkov = 0

    def strel(self, x, y, ime_strelca):
        if self.x0 <= x <= self.x1 and self.y0 <= y <= self.y1:
            self.st_zadetkov += 1
            self.slovar_strelcev[ime_strelca] += 1
        self.slovar_strelcev[ime_strelca] += 0

    def vseh_zadetkov(self):
        return self.st_zadetkov

    def vseh_strelcev(self):
        return len(self.slovar_strelcev)

    def zadetkov(self, ime_strelca):
        return self.slovar_strelcev[ime_strelca]

class Test(unittest.TestCase):
    pravokotniki = [(0, 1, 4, 3),
                    (0, 6, 1, 8),
                    (2, 2, 7, 6),
                    (3, 4, 6, 5),
                    (5, 1, 9, 7),
                    (8, 0, 10, 2),
                    (8, 3, 10, 5),
                    (8, 6, 11, 8)]

    def test_01_preberi_pravokotnike(self):
        self.assertEqual(preberi_pravokotnike("pravokotniki.txt"), self.pravokotniki)

    def test_02_nepokritih(self):
        self.assertEqual(nepokrito(self.pravokotniki, 11, 8), 34)

    def test_03_odstrani_zgresene(self):
        streli = [(0.55, 0.4), (0.1, 5), (5.1, 3.2), (7.1, 7.1), (8.5, 3.5)]
        self.assertIsNone(odstrani_zgresene(streli, self.pravokotniki))
        self.assertEqual(streli, [(5.1, 3.2), (8.5, 3.5)])

    def test_04_je_zlata(self):
        prekritja = {3: (4, 5), 5: (1, ), 4: (6, 7, 8), 2: (), 1: (), 6: (), 7: (), 8: ()}
        barve = {1: "zlata", 2: "zlata", 3: "modra", 4: "rdeca", 5: "rumena",
                 6: "zelena", 7: "rumena", 8: "modra", 9: "zelena"}

        self.assertTrue(je_zlata(1, barve, prekritja))
        self.assertTrue(je_zlata(2, barve, prekritja))
        self.assertTrue(je_zlata(3, barve, prekritja))
        self.assertFalse(je_zlata(4, barve, prekritja))
        self.assertTrue(je_zlata(5, barve, prekritja))
        self.assertFalse(je_zlata(6, barve, prekritja))
        self.assertFalse(je_zlata(7, barve, prekritja))
        self.assertFalse(je_zlata(8, barve, prekritja))

        prekritja[3] = (5, 4)
        self.assertTrue(je_zlata(3, barve, prekritja))

        barve[8] = "zlata"
        barve[3] = "rumena"
        self.assertTrue(je_zlata(3, barve, prekritja))

        barve[8] = "modra"
        barve[6] = "zlata"
        self.assertTrue(je_zlata(3, barve, prekritja))

    def test_05_pravokotnik(self):
        pravokotnik = Pravokotnik(3, 2, 7, 6)
        self.assertEqual(pravokotnik.vseh_zadetkov(), 0)
        self.assertEqual(pravokotnik.vseh_strelcev(), 0)

        pravokotnik.strel(1, 1, "Ana")
        pravokotnik.strel(1, 2, "Ana")
        pravokotnik.strel(3.5, 1.5, "Ana")
        pravokotnik.strel(3.5, 7, "Ana")
        self.assertEqual(pravokotnik.vseh_zadetkov(), 0)
        self.assertEqual(pravokotnik.vseh_strelcev(), 1)
        self.assertEqual(pravokotnik.zadetkov("Ana"), 0)

        pravokotnik.strel(3.5, 4, "Ana")
        pravokotnik.strel(3.5, 4, "Ana")
        pravokotnik.strel(3.5, 4, "Berta")
        self.assertEqual(pravokotnik.vseh_zadetkov(), 3)
        self.assertEqual(pravokotnik.vseh_strelcev(), 2)
        self.assertEqual(pravokotnik.zadetkov("Ana"), 2)


if __name__ == "__main__":
    unittest.main()
