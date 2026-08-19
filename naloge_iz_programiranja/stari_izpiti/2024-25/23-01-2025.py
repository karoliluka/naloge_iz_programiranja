from collections import defaultdict
from email.policy import default
from itertools import pairwise

def povezave(pot):
    odseki = set()
    seznam = [ime for ime in pot.split("-")]
    for ime1, ime2 in zip(seznam, seznam[1:]):
        odseki.add((ime1, ime2))
    return odseki

def popularni(poti, k):
    slovar_odsekov = defaultdict(int)
    for pot in poti:
        for odsek in povezave(pot):
            slovar_odsekov[odsek] += 1

    seznam_terk = []
    for odsek, stevilo_odsekov in slovar_odsekov.items():
        seznam_terk.append((odsek, stevilo_odsekov))

    sortiran_seznam_terk = sorted(seznam_terk, key=lambda odsek: odsek[1], reverse=True)

    mnozica_odsekov = set()

    i = 0
    while i < k and i < len(sortiran_seznam_terk):
        mnozica_odsekov.add(sortiran_seznam_terk[i][0])
        i += 1

    return mnozica_odsekov

def casi(pot):
    razdalje = {}
    od = None
    for kos in pot.split("-"):
        if not kos:
            dolzina += 1
        else:
            if od is not None:
                razdalje[(od, kos)] = dolzina
            od = kos
            dolzina = 1
    return razdalje

def krozenje(pot):
    tocke = pot.split("-")
    for i in range(2, len(tocke) // 2 + 1):
        if len(tocke) % i != 0:
            continue
        prva = tocke[:i]
        for j in range(i, len(tocke), i):
            if sum(x != y for x, y in zip(tocke[j:], prva)) > 1:
                break
        else:
            return True
    return False

def detektiv(odkod, kam, odhodi):
    if odkod == kam:
        return True
    for naslednji in odhodi.get(odkod, []):
        if detektiv(naslednji, kam, odhodi):
            return True
    return False

def vsebuje_zaporedje(seznam, podseznam):
    # ali se podseznam pojavi znotraj seznama kot strnjeno (zaporedno) zaporedje
    n = len(podseznam)
    for i in range(len(seznam) - n + 1):
        if seznam[i:i+n] == podseznam:
            return True
    return False


class Strava:
    def __init__(self, odseki):
        self.popularnost = {}
        for odsek in odseki:
            self.popularnost[odsek] = 0

    def dodaj(self, pot):
        for odsek in self.popularnost:
            if odsek in pot:
                self.popularnost[odsek] += 1

    def najpopularnejsi(self):
        naj_ods = None
        for ods in self.popularnost:
            if naj_ods is None or self.popularnost[ods] > self.popularnost[naj_ods]:
                naj_ods = ods
        return naj_ods









import unittest
import copy

class Test(unittest.TestCase):
    def test_1_a_povezave(self):
        self.assertEqual({("Ana", "Berta"), ("Berta", "Cilka"), ("Cilka", "Berta"),
                          ("Berta", "Dani"), ("Dani", "Berta"), ("Berta", "Ema")},
                         povezave("Ana-Berta-Cilka-Berta-Dani-Berta-Ema"))
        self.assertEqual({("Ana", "Berta")}, povezave("Ana-Berta"),
                         )
        self.assertEqual(set(), povezave("Ana"))

    def test_1_b_popularni(self):
        self.assertEqual({("Ana", "Berta")},
                         popularni(["Ana-Berta"], 1))
        self.assertEqual({("Ana", "Berta")},
                         popularni(["Ana-Berta", "Ana-Berta-Cilka"], 1))
        self.assertEqual({("Ana", "Berta"), ("Berta", "Cilka")},
                         popularni(["Ana-Berta", "Ana-Berta-Cilka"], 2))
        self.assertEqual({("Ana", "Berta"), ("Berta", "Cilka")},
                         popularni(["Ana-Berta", "Ana-Berta-Cilka"], 5))
        self.assertEqual({("Ana", "Berta"), ("Berta", "Cilka")},
                         popularni(["Ana-Berta", "Ana-Berta-Cilka", "Berta-Cilka-Ana"], 2))

        self.assertEqual({('Cilka', 'Berta'), ('Berta', 'Cilka'), ('Ana', 'Berta')},
                         popularni(["Ana-Berta-Cilka-Berta-Dani-Berta-Ema",
                                    "Berta-Ema-Dani-Berta-Ana-Cilka-Berta",
                                    "Ana-Berta-Cilka-Ema",
                                    "Ana-Ema-Ana-Ema-Ana-Ema-Ana-Ema-Ana-Ema-Ana-Ema-Ana-Ema-Ana-Ema",
                                    "Cilka-Berta-Cilka",
                                    "Ana-Berta-Cilka-Berta-Dani-Berta-Ema",
                                    "Berta-Cilka-Dani-Ema-Ana-Berta",
                                    "Ema-Dani-Ema-Dani-Ema-Berta"], 3))

    def test_2_a_casi_brez_ponovitev(self):
        self.assertEqual({("Ana", "Berta"): 4, ("Berta", "Dani"): 2, ("Dani", "Cilka"): 6,
                          ("Cilka", "Ema"): 7},
                         casi("Ana----Berta--Dani------Cilka-------Ema"))

    def test_2_b_casi_s_ponovitvami(self):
        self.assertEqual({("Ana", "Berta"): 4, ("Berta", "Dani"): 2, ("Dani", "Cilka"): 6,
                      ("Cilka", "Berta"): 3, ("Berta", "Ema"): 7, ("Ema", "Berta"): 1,
                      ("Berta", "Ana"): 2},
                     casi("Ana----Berta--Dani------Cilka---Berta-------Ema-Berta--Ana"))

    def test_3_a_krozenje_tocno(self):
        self.assertTrue(krozenje("Ana-Berta-Cilka-Ana-Berta-Cilka-Ana-Berta-Cilka-Ana-Berta-Cilka"))
        self.assertTrue(krozenje(("A-B-C-D-E-F-G-H-" * 30)[:-1]))
        self.assertTrue(krozenje(("Ana-Berta-" * 10)[:-1]))
        self.assertFalse(krozenje("Ana-Berta-Cilka-Ana-Ana-Berta-Cilka-Ana-Berta-Cilka"))
        self.assertFalse(krozenje("Ana-Berta-Cilka-Ana-Ema-Dani-Cilka-Ana-Berta-Cilka"))

    def test_3_b_krozenje_priblizno(self):
        self.assertTrue(krozenje("Ana-Berta-Cilka-Ana-Berta-Dani-Ana-Ema-Cilka-Ema-Berta-Cilka"))
        self.assertTrue(krozenje("Ana-Berta-Cilka-Ana-Berta-Dani-Ana-Berta-Ema-Ana-Berta-Cilka"))
        self.assertFalse(krozenje("Ana-Berta-Cilka-Ana-Cilka-Berta-Ana-Berta-Ema-Ana-Berta-Cilka"))

    @staticmethod
    def args4():
        return ()

    try:
        if detektiv.__code__.co_argcount == 4:
            @staticmethod
            def args4():
                return (set(), )
    except NameError:
        pass


    def test_4_a_detektiv_preprostejsi(self):
        povezave = {
            "Ana": {"Berta"},
            "Berta": {"Dani", "Cilka", "Franci"},
            "Cilka": {"Ema", "Franci", "Iva"},
            "Dani": {"Cilka"},
            "Ema": {"Iva", "Helga"},
            "Franci": {"Greta", "Iva"},
            "Jana": {"Klara"},
        }

        self.assertTrue(detektiv("Ana", "Ana", povezave, *self.args4()))
        self.assertTrue(detektiv("Ana", "Berta", povezave, *self.args4()))
        self.assertTrue(detektiv("Ana", "Dani", povezave, *self.args4()))
        self.assertTrue(detektiv("Dani", "Ema", povezave, *self.args4()))
        self.assertTrue(detektiv("Dani", "Greta", povezave, *self.args4()))
        self.assertTrue(detektiv("Jana", "Klara", povezave, *self.args4()))

        self.assertFalse(detektiv("Dani", "Klara", povezave, *self.args4()))
        self.assertFalse(detektiv("Ana", "Klara", povezave, *self.args4()))
        self.assertFalse(detektiv("Ana", "Jana", povezave, *self.args4()))
        self.assertFalse(detektiv("Franci", "Dani", povezave, *self.args4()))
        self.assertFalse(detektiv("Klara", "Jana", povezave, *self.args4()))

    if args4() != ():
        def test_4_b_detektiv_krozni(self):
            povezave = {
                "Ana": {"Berta"},
                "Berta": {"Dani", "Cilka", "Franci"},
                "Cilka": {"Ema", "Franci", "Iva", "Ana"},
                "Dani": {"Cilka", "Ana"},
                "Ema": {"Iva", "Helga"},
                "Franci": {"Greta", "Iva", "Dani"},
                "Greta": {"Franci"},
                "Jana": {"Klara"},
                "Klara": {"Jana"}
            }
            povezave_bak = copy.deepcopy(povezave)

            self.assertTrue(detektiv("Ana", "Ana", povezave, set()))
            self.assertEqual(povezave, povezave_bak, "Funkcija spreminja slovar povezave. Poredna, poredna!")
            self.assertTrue(detektiv("Ana", "Berta", povezave, set()))
            self.assertTrue(detektiv("Ana", "Dani", povezave, set()))
            self.assertTrue(detektiv("Dani", "Ema", povezave, set()))
            self.assertTrue(detektiv("Dani", "Greta", povezave, set()))
            self.assertTrue(detektiv("Jana", "Klara", povezave, set()))
            self.assertTrue(detektiv("Franci", "Dani", povezave, set()))
            self.assertTrue(detektiv("Greta", "Ana", povezave, set()))
            self.assertTrue(detektiv("Klara", "Jana", povezave, set()))
            self.assertTrue(detektiv("Jana", "Klara", povezave, set()))

            self.assertFalse(detektiv("Dani", "Klara", povezave, set()))
            self.assertFalse(detektiv("Ana", "Klara", povezave, set()))
            self.assertFalse(detektiv("Ana", "Jana", povezave, set()))
            self.assertFalse(detektiv("Iva", "Cilka", povezave, set()))
            self.assertFalse(detektiv("Iva", "Ana", povezave, set()))
            self.assertFalse(detektiv("Helga", "Ana", povezave, set()))
            self.assertFalse(detektiv("Jana", "Ana", povezave, set()))
            self.assertFalse(detektiv("Klara", "Ana", povezave, set()))


    def test_5_strava(self):
        s = Strava(["Ana-Berta-Dani-Ema", "Ana-Berta-Cilka", "Berta-Cilka", "Cilka-Ema-Dani-Ana-Helga", "Helga-Greta-Ema"])
        s.dodaj("Ema-Ana-Berta-Dani-Ema")
        self.assertEqual("Ana-Berta-Dani-Ema", s.najpopularnejsi())
        s.dodaj("Ana-Berta-Cilka")
        s.dodaj("Ema-Berta-Cilka-Ana")
        self.assertEqual("Berta-Cilka", s.najpopularnejsi())
        s.dodaj("Berta-Cilka-Helga-Greta-Ema")
        s.dodaj("Ana-Berta-Dani-Helga-Greta-Ema")
        s.dodaj("Helga-Greta-Ema")
        s.dodaj("Helga-Greta-Ema-Dani-Ema")
        self.assertEqual("Helga-Greta-Ema", s.najpopularnejsi())


if __name__ == "__main__":
    unittest.main()
