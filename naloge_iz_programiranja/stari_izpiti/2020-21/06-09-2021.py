import unittest
from collections import defaultdict
from math import sqrt

from naloge_iz_programiranja.pisanje_funkcij.Naloge import osebe


def preblizu(x1, y1, x2, y2):
    if sqrt((x2 - x1)**2 + (y2 - y1)**2) < 1.5:
        return True
    return False

def koordinate(ime, osebe):
    for name, x, y in osebe:
        if ime == name:
            return x, y
    return None

def krsitelji(osebe):
    mnozica = set()
    slovar_terk = defaultdict(list) #terka oblika (ime1, (najblizja_ime1, razdalja_do_ime1))
    for ime1, x1, y1 in osebe:
        for ime2, x2, y2 in osebe:
            if ime1 != ime2:
                razdalja = sqrt((x2 - x1)**2 + (y2 - y1)**2)
                slovar_terk[ime1].append((ime2, razdalja))

    slovar_najblizjih = defaultdict(tuple)
    for ime, terke in slovar_terk.items():
        slovar_najblizjih[ime] = min(terke, key=lambda terka: terka[1])

    for ime, (ime2, razdalja) in slovar_najblizjih.items():
        if razdalja < 1.5:
            mnozica.add(ime)

    return mnozica

def kazni(osebe):
    slovar_imena_kazni = defaultdict(int) #slovar oblike ime_krsitelja : st_kazni
    slovar_terk = defaultdict(list)  # terka oblika (ime1, (najblizja_ime1, razdalja_do_ime1))
    for ime1, x1, y1 in osebe:
        for ime2, x2, y2 in osebe:
            if ime1 != ime2:
                razdalja = sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)
                slovar_terk[ime1].append((ime2, razdalja))

    for ime, terke in slovar_terk.items():
        seznam_preblizu = []
        for ime2, razdalja in terke:
            if razdalja < 1.5:
                seznam_preblizu.append(ime2)
        if seznam_preblizu:
            slovar_imena_kazni[ime] = len(seznam_preblizu)
        else:
            continue
    return slovar_imena_kazni

def okuzeni(ime, osebe):
    obiskane = {ime}
    za_obdelat = [ime]

    while za_obdelat:
        trenutna = za_obdelat.pop()
        x_trenutna, y_trenutna = koordinate(trenutna, osebe)

        for sosed_ime, x_sosed, y_sosed in osebe:
            if sosed_ime in obiskane:
                continue
            if y_sosed < y_trenutna and preblizu(x_trenutna, y_trenutna, x_sosed, y_sosed):
                obiskane.add(sosed_ime)
                za_obdelat.append(sosed_ime)

    return obiskane

def okuzeni(ime, osebe):
    x_ime, y_ime = koordinate(ime, osebe)
    obiskane = {ime}

    for sosed_ime, x_sosed, y_sosed in osebe:
        if sosed_ime not in obiskane and y_sosed < y_ime and preblizu(x_ime, y_ime, x_sosed, y_sosed):
            obiskane |= okuzeni(sosed_ime, osebe)

    return obiskane

def names(osebe):
    mnozica_oseb = set()
    for oseba in osebe:
        mnozica_oseb.add(oseba[0])
    return mnozica_oseb


def kihanje(imena, osebe):
    pristotni = {ime for ime, x, y in osebe}

    for kdo in imena:
        if kdo not in pristotni:
            continue

        x0, y0 = koordinate(kdo, osebe)
        odstrani = {ime2 for ime2, x2, y2 in osebe if ime2 in pristotni and preblizu(x0, y0, x2, y2)}
        pristotni -= odstrani

    return pristotni

class Prireditev:
    def __init__(self, min_razdalja):
        self.min_razdalja = min_razdalja
        self.sprejeti = []

    def prihod(self, ime, x, y):
        for ime_o, x_o, y_o in self.sprejeti:
            if sqrt((x_o - x) ** 2 + (y_o - y) ** 2) < self.min_razdalja:
                return

        self.sprejeti.append((ime, x, y))

    def udelezenci(self):
        return {ime for ime, x, y in self.sprejeti}



class Test(unittest.TestCase):
    osebe = [("Ana", 2, 4.5),
             ("Berta", 1, 3),
             ("Cilka", 1, 4),
             ("Dani", -1, 2),
             ("Ema", 1, 1),
             ("Fanči", 2, 0.5),
             ("Greta", -1, -1.5),
             ("Helga", 0, -1),
             ("Iva", 2, 0),
             ("Jana", 0, 0),
             ("Klara", 5, 1)
             ]

    def test_0_preblizu(self):
        self.assertTrue(preblizu(5, 3, 6, 2))
        self.assertTrue(preblizu(5, 2, 5, 2))
        self.assertTrue(preblizu(6, 2, 5, 3))
        self.assertTrue(preblizu(0, 0, 1.4, 0))
        self.assertFalse(preblizu(5, 3, 6, 1))

    def test_0_koordinate(self):
        self.assertEqual((-1, 2), koordinate("Dani", self.osebe))

    def test_1_krsitelji(self):
        self.assertEqual(
            set("Ana Berta Cilka Ema Fanči Greta Helga Iva Jana".split()),
            krsitelji(self.osebe)
        )
        self.assertEqual(
            set("Ana Berta Cilka Ema Fanči Greta Helga Iva Jana".split()),
            krsitelji(self.osebe[:-1])
        )
        self.assertEqual(
            set("Greta Helga Jana".split()),
            krsitelji(self.osebe[-5:])
        )
        self.assertEqual(
            set(),
            krsitelji(self.osebe[:2])
        )

    def test_2_kazni(self):
        self.assertEqual(
            {"Ana": 1, "Berta": 1, "Cilka": 2, "Ema": 3,
             "Fanči": 2, "Greta": 1, "Helga": 2, "Iva": 2, "Jana": 2},
            kazni(self.osebe)
        )

    def test_3_okuzenih(self):
        self.assertEqual(
            {"Ema", "Fanči", "Iva", "Jana", "Greta", "Helga"},
            okuzeni("Ema", self.osebe))
        self.assertEqual(
            {"Jana", "Greta", "Helga"},
            okuzeni("Jana", self.osebe))
        self.assertEqual(
            {"Ana", "Berta", "Cilka"},
            okuzeni("Ana", self.osebe))
        self.assertEqual(
            {"Berta"},
            okuzeni("Berta", self.osebe))
        self.assertEqual(
            {"Klara"},
            okuzeni("Klara", self.osebe))

    def test_4_kihanje(self):
        self.assertEqual(
            set("Ana Berta Cilka Dani Ema Fanči Greta Helga Iva Jana Klara".split()),
            kihanje([], self.osebe)
        )
        self.assertEqual(
            set("Ana Berta Cilka Dani Greta Helga Jana Klara".split()),
            kihanje(["Fanči"], self.osebe)
        )
        self.assertEqual(
            set("Ana Berta Cilka Dani Greta Helga Klara".split()),
            kihanje(["Ema"], self.osebe)
        )
        self.assertEqual(
            set("Ana Berta Cilka Dani Greta Helga Klara".split()),
            kihanje(["Ema", "Jana"], self.osebe)
        )
        self.assertEqual(
            set("Ana Berta Cilka Dani Greta Helga Klara".split()),
            kihanje(["Ema", "Fanči"], self.osebe)
        )
        self.assertEqual(
            set("Ana Berta Cilka Dani Greta Helga".split()),
            kihanje(["Ema", "Fanči", "Klara"], self.osebe)
        )
        self.assertEqual(
            set("Dani Greta Helga".split()),
            kihanje(["Ema", "Fanči", "Klara", "Cilka"], self.osebe)
        )
        self.assertEqual(
            set("Ana Berta Cilka Dani Fanči Greta Iva Klara".split()),
            kihanje(["Jana", "Helga", "Ema"], self.osebe)
        )
        self.assertEqual(
            set("Ana Berta Cilka Dani Klara".split()),
            kihanje(["Helga", "Ema", "Jana"], self.osebe)
        )

    def test_5_prireditev(self):
        g = Prireditev(1.5)
        for ime, x, y in self.osebe:
            g.prihod(ime, x, y)
        self.assertEqual(
            {"Ana", "Berta", "Dani", "Ema", "Greta", "Klara"},
            g.udelezenci()
        )

        g = Prireditev(1.5)
        for ime, x, y in self.osebe:
            if ime != "Ema":
                g.prihod(ime, x, y)
        self.assertEqual(
            {"Ana", "Berta", "Dani", "Fanči", "Greta", "Jana", "Klara"},
            g.udelezenci()
        )

        g = Prireditev(3)
        for ime, x, y in self.osebe:
            g.prihod(ime, x, y)
        self.assertEqual(
            {"Ana", "Dani", "Fanči", "Greta", "Klara"},
            g.udelezenci()
        )


if __name__ == "__main__":
    unittest.main()

