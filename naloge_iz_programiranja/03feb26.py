import warnings
import unittest
from collections import defaultdict
from email.headerregistry import DateHeader


def vse_aktivnosti(aktivnosti):
    mnozica_aktivnosti = set()
    for dan in aktivnosti:
        for aktivnost in dan:
            mnozica_aktivnosti.add(aktivnost)
    return mnozica_aktivnosti

def naj_veriga(aktivnosti, aktivnost):
    slovar_aktivnosti = defaultdict(list)
    stevec = 0
    zacetek_verige = False
    for dan in aktivnosti:
        if aktivnost in dan and zacetek_verige is False:
            stevec += 1
            zacetek_verige = True
        elif aktivnost in dan and zacetek_verige is True:
            stevec += 1
        elif aktivnost not in dan and zacetek_verige is True:
            slovar_aktivnosti[aktivnost].append(stevec)
            zacetek_verige = False
            stevec = 0

    for ime_aktivnosti, tabela in slovar_aktivnosti.items():
        return max(tabela)
    return None

def naj_aktivnost(aktivnosti):
    slovar_naj_aktivnosti = defaultdict(int)
    for dan in aktivnosti:
        for aktivnost in dan:
            slovar_naj_aktivnosti[aktivnost] = naj_veriga(aktivnosti, aktivnost)

    naj = 0
    ime_naj = ""
    for ime_aktivnosti, dolzina_verige in slovar_naj_aktivnosti.items():
        if dolzina_verige > naj:
            naj = dolzina_verige
            ime_naj = ime_aktivnosti

    return ime_naj, naj

def preberi_aktivnosti(ime_datoteke):
    seznam = []
    vrstice = []
    with open(ime_datoteke, "r", encoding="utf-8") as datoteka:
        for i, vrstica in enumerate(datoteka):
            vrstice.append(vrstica.strip())
            if vrstica.strip() == "---":
                indeks_preloma = i

    slovar_aktivnosti = defaultdict(str)
    for vrstica in vrstice[indeks_preloma + 1:]:
        znak, sport = vrstica.strip().split("=")[0], vrstica.strip().split("=")[1]
        slovar_aktivnosti[znak] = sport


    for vrstica in vrstice[:indeks_preloma]:
        mnozica_aktivnsoti = set()
        for char in vrstica.strip():
            mnozica_aktivnsoti.add(slovar_aktivnosti[char])
        seznam.append(mnozica_aktivnsoti)

    return seznam

class Spomeniki:
    def __init__(self):
        self.slovar_obiskov_spomenikov = defaultdict(list) #slovar kjer belezimo kateri kolesar je prisel na kateri spomenik
        return

    def obisci(self, kolesar, spomenik):
        self.slovar_obiskov_spomenikov[spomenik].append(kolesar)
        if len(self.slovar_obiskov_spomenikov[spomenik]) == 1:
            return True
        return False

    def obiskanost(self, spomenik):
        return len(set(self.slovar_obiskov_spomenikov[spomenik]))

    def spomenikov(self, kolesar):
        mnozica_spomenikov = set()
        for ime_spomenika, ime_kolesarjev in self.slovar_obiskov_spomenikov.items():
            if kolesar in ime_kolesarjev:
                mnozica_spomenikov.add(ime_spomenika)
        return len(mnozica_spomenikov)

    def prvaki(self):
        slovar = defaultdict(str)
        for ime_spomenika, imena_kolesarja in self.slovar_obiskov_spomenikov.items():
            slovar[ime_spomenika] = imena_kolesarja[0]
        return slovar

def podvig(visine, x, y):
    mx, my = x, y
    while True:
        for nx, ny in ((x, y - 1), (x + 1, y), (x, y + 1), (x - 1, y)):
            if 0 <= ny < len(visine) and 0 <= nx < len(visine[ny]) and visine[ny][nx] > visine[my][mx]:
                mx, my = nx, ny
        if mx == x  and my == y:
            return mx, my
        x, y = mx, my

def vrh(visine, x, y):
    naj_v = x, y, visine[y][x]
    for nx, ny in ((x, y - 1), (x + 1, y), (x, y + 1), (x - 1, y)): #gor, desno, dol, levo
        if 0 <= ny < len(visine) and 0 <= nx < len(visine[ny]) and visine[ny][nx] > visine[y][x]:
            tam_v = vrh(visine, nx, ny)
            if tam_v[2] > naj_v[2]:
                naj_v = tam_v
    return naj_v









class Test(unittest.TestCase):
    visine = [
        [12, 15, 32, 24, 24],
        [ 8, 12, 29],
        [ 3,  6, 24, 13, 11, 18],
        [-2, 25,  8, 10],
        [ 0,  1,  3,  9, 12, 16],
        [ 0,  2,  2],
        [ 0, 13, 12, 14, 16],
        [15, 14, 5]
    ]

    @classmethod
    def setUpClass(cls):
        with open("aktivnosti.txt", "w") as f:
            f.write("""
TKB
T
PKS
TPS
TK
TK
PS
---
T=tek
K=kolesarjenje
B=badminton
P=plavanje
S=sprehod
""".lstrip())

        with open("aktivnosti2.txt", "w") as f:
            f.write("""
TKBJ
TJ
PKSJ
TPSJ
TKJ
TKJ
PSJ
---
T=tek
K=kolesarjenje
B=badminton
P=plavanje
J=joga
S=sabljanje
""".lstrip())

    def setUp(self):
        warnings.simplefilter("ignore", ResourceWarning)

    def test_1_podvig(self):
        self.assertEqual((2, 0), podvig(self.visine, 0, 2))
        self.assertEqual((1, 3), podvig(self.visine, 1, 2))
        self.assertEqual((5, 4), podvig(self.visine, 3, 4))
        self.assertEqual((4, 6), podvig(self.visine, 2, 5))
        self.assertEqual((0, 7), podvig(self.visine, 2, 7))
        self.assertEqual((0, 7), podvig(self.visine, 0, 6))
        self.assertEqual((0, 7), podvig(self.visine, 0, 5))
        self.assertEqual((5, 2), podvig(self.visine, 4, 2))
        self.assertEqual((4, 6), podvig(self.visine, 2, 6))

    def test_2_vrh(self):
        self.assertEqual((2, 0, 32), vrh(self.visine, 0, 3))
        self.assertEqual((2, 0, 32), vrh(self.visine, 2, 3))
        self.assertEqual((0, 7, 15), vrh(self.visine, 0, 5))
        self.assertEqual((2, 0, 32), vrh(self.visine, 4, 2))
        self.assertEqual((4, 6, 16), vrh(self.visine, 2, 6))
        self.assertEqual((0, 7, 15), vrh(self.visine, 1, 6))

    aktivnosti = [
        {"tek", "kolesarjenje", "badminton"},
        {"tek"},
        {"plavanje", "kolesarjenje", "sprehod"},
        {"tek", "plavanje", "sprehod"},
        {"tek", "kolesarjenje"},
        {"tek", "kolesarjenje"},
        {"plavanje", "sprehod"},
    ]

    def test_3a_vse_aktivnosti(self):
        self.assertEqual(
            {"tek", "kolesarjenje", "badminton", "plavanje", "sprehod"},
            vse_aktivnosti(self.aktivnosti))

    def test_3b_naj_veriga(self):
        self.assertEqual(3, naj_veriga(self.aktivnosti, "tek"))
        self.assertEqual(2, naj_veriga(self.aktivnosti, "kolesarjenje"))
        self.assertEqual(2, naj_veriga(self.aktivnosti, "plavanje"))
        self.assertEqual(1, naj_veriga(self.aktivnosti, "badminton"))

    def test_3c_naj_aktivnost(self):
        self.assertEqual(("tek", 3), naj_aktivnost(self.aktivnosti))

    def test_4_preberi_aktivnosti(self):
        self.assertEqual(self.aktivnosti, preberi_aktivnosti("aktivnosti.txt"))
        self.assertEqual([
            akt  - {"sprehod"} | {"joga"} | ({"sabljanje"} if "sprehod" in akt else set())
            for akt in self.aktivnosti], preberi_aktivnosti("aktivnosti2.txt"))

    def test_5_spomenikki(self):
        s = Spomeniki()
        self.assertTrue(s.obisci("Ana", "Vršič"))
        self.assertFalse(s.obisci("Ana", "Vršič"))
        self.assertFalse(s.obisci("Ana", "Vršič"))
        self.assertFalse(s.obisci("Ana", "Vršič"))
        self.assertFalse(s.obisci("Berta", "Vršič"))
        self.assertTrue(s.obisci("Ana", "Blekova"))
        self.assertTrue(s.obisci("Cilka", "Tromeja"))
        self.assertFalse(s.obisci("Ana", "Tromeja"))
        self.assertFalse(s.obisci("Berta", "Tromeja"))
        self.assertFalse(s.obisci("Berta", "Tromeja"))
        self.assertFalse(s.obisci("Berta", "Tromeja"))

        self.assertEqual(3, s.obiskanost("Tromeja"))
        self.assertEqual(1, s.obiskanost("Blekova"))
        self.assertEqual(2, s.obiskanost("Vršič"))

        self.assertEqual(3, s.spomenikov("Ana"))
        self.assertEqual(2, s.spomenikov("Berta"))
        self.assertEqual(1, s.spomenikov("Cilka"))

        self.assertEqual({"Vršič": "Ana", "Blekova": "Ana", "Tromeja": "Cilka"}, s.prvaki())


if __name__ == "__main__":
    unittest.main()
