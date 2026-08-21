import random
import unittest
from encodings.cp862 import encoding_map


def nestrinjanja(ovire1, ovire2):
    return set(ovire1) ^ set(ovire2)

def proste_ovire(ovire):
    mnozica_ovir = set()
    kopija_mnozice_ovir = set(ovire.copy())
    for i, ovira1 in enumerate(ovire):
        x0_1, x1_1, y_1 = ovira1
        for j, ovira2 in enumerate(ovire):
            x0_2, x1_2, y_2 = ovira2
            if i != j:
                if y_1 == y_2:
                    if (x0_1 <= x0_2 <= x1_1) or (x0_1 <= x1_2 <= x1_1) or (x0_2 <= x0_1 <= x1_2) or (x0_2 <= x1_1 <= x1_2):
                        mnozica_ovir.add(ovira1)
                        mnozica_ovir.add(ovira2)

    return list(kopija_mnozice_ovir - mnozica_ovir)

def dolzina_ovir(ime_datoteke):
    vsota = 0
    with open(ime_datoteke, "r", encoding="utf-8") as datoteka:
        for vrstica in datoteka:
            ovira = vrstica.strip().split(" ")[0]
            x0 = ovira.split("-")[0]
            x1 = ovira.split("-")[1]
            dolzina = int(x1) - int(x0) + 1
            vsota += dolzina
    return vsota

def zdruzi_ovire(ovire):
    if len(ovire) <= 1:
        return list(ovire)

    x0_1, x1_1, y_1 = ovire[0]
    x0_2, x1_2, y_2 = ovire[1]

    if y_1 == y_2 and x1_1 + 1 == x0_2:
        zdruzena = (x0_1, x1_2, y_1)
        return zdruzi_ovire([zdruzena] + ovire[2:])
    else:
        return [ovire[0]] + zdruzi_ovire(ovire[1:])

class Kolesarska:
    def __init__(self):
        self.ovire = set()

    def dodaj_oviro(self, x0, x1, y):
        self.ovire.add((x0, x1, y))

    def stevilo_ovir(self):
        return len(self.ovire)

    def prosto(self, x, y):
        for (x0, x1, y_o) in self.ovire:
            if y == y_o and x0 <= x <= x1:
                return False
        return True

class InteligentnaKolesarska(Kolesarska):
    def prosto(self, x, y):
        for (x0, x1, y_o) in self.ovire:
            if y == y_o and x0 <= x <= x1:
                return False
        self.dodaj_oviro(x, x + 1, y)
        return True




















ovire = [(1, 3, 6), (2, 4, 3),
         (3, 4, 9), (6, 9, 5), (9, 10, 2), (9, 10, 8),
         (4, 6, 7),
         ]


class Test(unittest.TestCase):
    def test_01_nestrinjanja(self):
        dodatne = [(3, 5, 1), (1, 2, 3)]
        ovire2 = ovire[1:-2] + dodatne
        self.assertEqual(set(ovire[:1] + ovire[-2:] + dodatne), nestrinjanja(ovire, ovire2))

    def test_02_proste_ovire(self):
        ovire = [(1, 3, 6), (2, 4, 3),
                 (3, 4, 9), (6, 9, 5), (9, 10, 2), (9, 10, 8),
                 (4, 6, 7),
                 (1, 2, 10), (5, 8, 10),
                 (5, 8, 13), (5, 8, 13),

                 (3, 5, 6),
                 (4, 6, 5), (8, 10, 5),
                 (1, 2, 3), (3, 3, 3), (4, 7, 3), (6, 8, 3)
                 ]
        for _ in range(5):
            random.shuffle(ovire)
            self.assertEqual(
                {(3, 4, 9), (9, 10, 2), (9, 10, 8), (4, 6, 7), (1, 2, 10), (5, 8, 10)},
                set(proste_ovire(ovire)))

    def test_03_dolzina_ovir(self):
        with open("ovire.txt", "wt", encoding="utf8") as f:
            f.write("".join(f"{x0}-{x1} {y}\n" for x0, x1, y in ovire))
        self.assertEqual(19, dolzina_ovir("ovire.txt"))

    def test_04_zdruzi_ovire(self):
        ovire = [(1, 3, 2), (4, 6, 2),
                 (4, 8, 5), (11, 13, 5),
                 (1, 3, 6),
                 (3, 5, 8), (6, 6, 8), (7, 10, 8)]
        self.assertEqual([(1, 6, 2), (4, 8, 5), (11, 13, 5), (1, 3, 6), (3, 10, 8)], zdruzi_ovire(ovire))

        ovire = [(1, 3, 2), (4, 6, 2),
                 (4, 8, 5), (11, 13, 5),
                 (1, 3, 6),
                 (3, 5, 8), (6, 6, 8), (7, 10, 8),
                 (3, 5, 10)]
        self.assertEqual([(1, 6, 2), (4, 8, 5), (11, 13, 5), (1, 3, 6), (3, 10, 8), (3, 5, 10)], zdruzi_ovire(ovire))

    def test_05_kolesarska(self):
        k = Kolesarska()

        self.assertEqual(0, k.stevilo_ovir())
        self.assertTrue(k.prosto(4, 8))
        self.assertTrue(k.prosto(4, 8))

        k.dodaj_oviro(3, 5, 7)
        self.assertEqual(1, k.stevilo_ovir())
        self.assertTrue(k.prosto(4, 8))
        self.assertTrue(k.prosto(4, 8))

        k.dodaj_oviro(1, 2, 8)
        self.assertEqual(2, k.stevilo_ovir())
        self.assertTrue(k.prosto(4, 8))
        self.assertTrue(k.prosto(4, 8))

        k.dodaj_oviro(3, 5, 8)
        self.assertEqual(3, k.stevilo_ovir())
        self.assertFalse(k.prosto(4, 8))

        # Test, da inteligentna kolesarska ne definira drugih metod kot `prosto`
        dodatne = [f"`{k}`" for k in InteligentnaKolesarska.__dict__
                   if not (k[:2] == "__" or k == "prosto")]
        self.assertTrue(
            not dodatne,
            f"Razred InteligentnaKolesarska naj definira samo metodo `prosto`,\n"
            f"ne pa tudi {','.join(dodatne)}")

        # Test, da se ovire dodajajo
        k2 = InteligentnaKolesarska()
        self.assertEqual(0, k2.stevilo_ovir())
        self.assertTrue(k2.prosto(4, 8))
        self.assertEqual(1, k2.stevilo_ovir())
        self.assertFalse(k2.prosto(4, 8))

        # Test, da inteligentna kolesarska sicer deluje kot normalna
        k = InteligentnaKolesarska()

        self.assertEqual(0, k.stevilo_ovir())

        k.dodaj_oviro(3, 5, 7)
        self.assertEqual(1, k.stevilo_ovir())
        self.assertTrue(k.prosto(4, 8))
        self.assertEqual(2, k.stevilo_ovir())


if __name__ == "__main__":
    unittest.main()
