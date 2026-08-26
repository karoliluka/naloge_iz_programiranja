from collections import defaultdict


def preziveli(postavitev):
    slovar_pozicij = defaultdict(list)
    for figura, pozicija in postavitev:
        slovar_pozicij[pozicija].append(figura)

    mnozica_prezivelih = set()
    for pozicija, seznam_figur in slovar_pozicij.items():
        if len(seznam_figur) == 1:
            mnozica_prezivelih.add(seznam_figur[0])
        else:
            mnozica_prezivelih.add(seznam_figur[-1])

    return mnozica_prezivelih

def prosta_polja(kraljice):
    zasedena = set()
    for kraljica in kraljice:
        for x in range(1, 9):
            for y in range(1, 9):
                if y == kraljica[1] or x == kraljica[0] or abs(x - kraljica[0]) == abs(y - kraljica[1]):
                    zasedena.add((x, y))
    return 64 - len(zasedena)

def dostopnih_polj(koordinate, zasedena):
    x_t, y_t = koordinate
    stevec_dostopnih = 1  # polje, kjer top trenutno stoji

    for x in range(x_t + 1, 9):
        if (x, y_t) in zasedena:
            break
        stevec_dostopnih += 1

    for x in range(x_t - 1, 0, -1):
        if (x, y_t) in zasedena:
            break
        stevec_dostopnih += 1


    for y in range(y_t + 1, 9):
        if (x_t, y) in zasedena:
            break
        stevec_dostopnih += 1


    for y in range(y_t - 1, 0, -1):
        if (x_t, y) in zasedena:
            break
        stevec_dostopnih += 1

    return stevec_dostopnih

def sciti_kmeta(x1, y1, x2, y2, kmetje):
    zasciteni = [(x1 - 1, y1 + 1), (x1 + 1, y1 + 1)]

    for x, y in zasciteni:
        if (x, y) == (x2, y2):
            return True
        if (x, y) in kmetje:
            if sciti_kmeta(x, y, x2, y2, kmetje):
                return True

    return False

class Top:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.trenutne_koordinate = (self.x, self.y)
        self.prehodil = 0

    def premik(self, smer, polj):
        if smer == ">":
            self.x += polj
        elif smer == "<":
            self.x -= polj
        elif smer == "v":
            self.y -= polj
        else:
            self.y += polj

        self.trenutne_koordinate = (self.x, self.y)
        self.prehodil += polj

    def koordinate(self):
        return self.trenutne_koordinate

    def razdalja(self):
        return self.prehodil

class StarTop(Top):
    def __init__(self, x, y):
        super().__init__(x, y)
        self.prejsni_velik = False

    def premik(self, smer, polj):
        if polj > 3 and self.prejsni_velik is True:
            self.prejsni_velik = False
        elif polj > 3 and self.prejsni_velik is False:
            super().premik(smer, polj)
            self.prejsni_velik = True
        elif polj <= 3:
            super().premik(smer, polj)
            self.prejsni_velik = False

import unittest
class Testi(unittest.TestCase):
    def test_01_preziveli(self):
        self.assertEqual(preziveli({}), set())
        self.assertEqual(preziveli(
            [("kmet1", "a2"), ("kmet2", "b2"), ("kmet3", "c2"),
             ("lovec1", "c1"), ("top1", "a1"), ("konj2", "b2"),
             ("kraljica", "d1"), ("lovec2", "b2"), ("top2", "c2")]),
            {"kmet1", "lovec1", "top1", "kraljica", "lovec2", "top2"}
        )

    def test_02_prosta_polja(self):
        self.assertEqual(prosta_polja([]), 64)
        self.assertEqual(prosta_polja([(1, 1)]), 64 - 1 - 7 - 7 - 7)
        self.assertEqual(prosta_polja([(1, 1), (3, 1)]), 64 - 1 - 7 - 7 - 7 - 6 - 5)
        self.assertEqual(prosta_polja([(1, 1), (1, 3)]), 64 - 1 - 7 - 7 - 7 - 6 - 5)
        self.assertEqual(prosta_polja([(1, 1), (3, 3)]), 64 - 1 - 7 - 7 - 7 - 6 - 6 - 1 - 1)
        self.assertEqual(prosta_polja([(1, 1), (3, 5)]), 64 - 1 - 7 - 7 - 7 - 1 - 5 - 5 - 4 - 3)
        self.assertEqual(prosta_polja([(1, 1), (3, 7)]), 64 - 1 - 7 - 7 - 7 - 1 - 5 - 4 - 1 - 5 - 2)
        self.assertEqual(prosta_polja([(1, 1), (8, 8)]), 36 - 6)

    def test_03_dostopnih_polj(self):
        self.assertEqual(dostopnih_polj((3, 5), []), 15)
        figure = [(1, 2), (3, 5), (4, 2), (5, 3), (6, 2), (7, 3),
                  (8, 4), (6, 7), (1, 5), (6, 8)]
        self.assertEqual(dostopnih_polj((6, 5), figure), 8)
        self.assertEqual(dostopnih_polj((2, 5), figure), 8)
        self.assertEqual(dostopnih_polj((5, 2), figure), 2)
        self.assertEqual(dostopnih_polj((3, 8), figure), 7)

    def test_04_sciti_kmeta(self):
        kmetje = [(1, 3), (3, 5), (5, 3), (6, 4), (4, 2), (4, 4), (7, 3), (8, 4)]
        self.assertTrue(sciti_kmeta(4, 2, 5, 3, kmetje))
        self.assertTrue(sciti_kmeta(5, 3, 6, 4, kmetje))
        self.assertTrue(sciti_kmeta(4, 2, 6, 4, kmetje))
        self.assertTrue(sciti_kmeta(4, 2, 3, 5, kmetje))
        self.assertTrue(sciti_kmeta(4, 2, 6, 4, kmetje))
        self.assertTrue(sciti_kmeta(5, 3, 3, 5, kmetje))
        self.assertTrue(sciti_kmeta(5, 3, 4, 4, kmetje))
        self.assertTrue(sciti_kmeta(5, 3, 6, 4, kmetje))
        self.assertTrue(sciti_kmeta(4, 4, 3, 5, kmetje))
        self.assertTrue(sciti_kmeta(7, 3, 6, 4, kmetje))
        self.assertTrue(sciti_kmeta(7, 3, 6, 4, kmetje))
        self.assertTrue(sciti_kmeta(7, 3, 8, 4, kmetje))

        self.assertFalse(sciti_kmeta(1, 3, 3, 5, kmetje))
        self.assertFalse(sciti_kmeta(3, 5, 1, 3, kmetje))
        self.assertFalse(sciti_kmeta(5, 3, 4, 2, kmetje))
        self.assertFalse(sciti_kmeta(5, 3, 6, 2, kmetje))
        self.assertFalse(sciti_kmeta(4, 2, 1, 3, kmetje))
        self.assertFalse(sciti_kmeta(1, 3, 4, 2, kmetje))
        self.assertFalse(sciti_kmeta(3, 3, 4, 2, kmetje))

    def test_05a_top(self):
        t = Top(5, 3)
        self.assertEqual(t.koordinate(), (5, 3))
        self.assertEqual(t.razdalja(), 0)
        t.premik("^", 3)
        self.assertEqual(t.koordinate(), (5, 6))
        t.premik(">", 1)
        self.assertEqual(t.koordinate(), (6, 6))
        t.premik("v", 4)
        self.assertEqual(t.koordinate(), (6, 2))
        t.premik("<", 5)
        self.assertEqual(t.koordinate(), (1, 2))
        self.assertEqual(t.razdalja(), 13)

    def test_05b_star_top(self):
        self.assertEqual(StarTop.__bases__, (Top, ))
        t = StarTop(5, 3)
        self.assertEqual(t.koordinate(), (5, 3))
        self.assertEqual(t.razdalja(), 0)
        t.premik("^", 3)
        self.assertEqual(t.koordinate(), (5, 6))
        t.premik(">", 1)
        self.assertEqual(t.koordinate(), (6, 6))
        t.premik("v", 4)
        self.assertEqual(t.koordinate(), (6, 2))
        self.assertEqual(t.razdalja(), 8)
        t.premik("<", 5)
        self.assertEqual(t.koordinate(), (6, 2))
        self.assertEqual(t.razdalja(), 8)
        t.premik("<", 5)
        self.assertEqual(t.koordinate(), (1, 2))
        self.assertEqual(t.razdalja(), 13)


if __name__ == "__main__":
    unittest.main()
