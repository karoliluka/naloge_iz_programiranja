
import warnings
import unittest
from collections import Counter, defaultdict

def podvig(visine, x, y):
    premiki = [(0, -1), (1, 0), (0, 1), (-1, 0)]  # ^, >, v, < (v tem vrstnem redu prednosti)
    while True:
        visina = visine[y][x]
        kandidati = []
        for dx, dy in premiki:
            nx, ny = x + dx, y + dy
            if 0 <= ny < len(visine) and 0 <= nx < len(visine[ny]):
                kandidati.append((visine[ny][nx], nx, ny))

        visji_sosedje = [k for k in kandidati if k[0] > visina]
        if not visji_sosedje:
            break  # noben sosed ni visji - kolesar obupa in ostane tu

        naj_visina = max(h for h, _, _ in visji_sosedje)
        for h, nx, ny in visji_sosedje:
            if h == naj_visina:
                x, y = nx, ny
                break  # prvi (po prioriteti ^,>,v,<) z najvisjo vrednostjo

    return x, y

def vrh(visine, x, y):
    premiki = [(0, -1), (1, 0), (0, 1), (-1, 0)]
    naj_x, naj_y, naj_visina = x, y, visine[y][x]

    for dx, dy in premiki:
        nx, ny = x + dx, y + dy
        if 0 <= ny < len(visine) and 0 <= nx < len(visine[ny]) and visine[ny][nx] > visine[y][x]:
            px, py, ph = vrh(visine, nx, ny)
            if ph > naj_visina:
                naj_x, naj_y, naj_visina = px, py, ph

    return naj_x, naj_y, naj_visina

def vse_aktivnosti(aktivnosti):
    mnozica_aktivnosti = set()
    for vec_aktivnosti in aktivnosti:
        for aktivnost in vec_aktivnosti:
            mnozica_aktivnosti.add(aktivnost)
    return mnozica_aktivnosti

def naj_veriga(aktivnosti, aktivnost):
    je_delal = False
    seznam = []
    stevilo_dni = 0
    for vec_aktivnosti in aktivnosti:
        if aktivnost in vec_aktivnosti and je_delal is False:
            stevilo_dni += 1
            je_delal = True
        elif aktivnost in vec_aktivnosti and je_delal:
            stevilo_dni += 1
            continue
        elif aktivnost not in vec_aktivnosti and je_delal is True:
            je_delal = False
            seznam.append(stevilo_dni)
            stevilo_dni = 0
    return max(seznam)

def naj_aktivnost(aktivnosti):
    slovar = Counter()
    for vec_aktivnosti in aktivnosti:
        for aktivnost in vec_aktivnosti:
            slovar[aktivnost] += 1
    naj = max(slovar)
    return naj, naj_veriga(aktivnosti, naj)

def preberi_aktivnosti(ime_datoteke):
    indeks_preloma = 0
    seznam = []
    slovar = dict()
    koncni_seznam = []
    with open(ime_datoteke, "r") as datoteka:
        for i, vrstica in enumerate(datoteka):
            seznam.append(vrstica.strip())
            if vrstica.strip() == "---":
                indeks_preloma = i

        for niz in seznam[indeks_preloma + 1:]:
            crka, sport = niz.split("=")
            slovar[crka] = sport

        for niz in seznam[:indeks_preloma]:
            mnozica_sportov = set()
            for char in niz:
                mnozica_sportov.add(slovar[char])
            koncni_seznam.append(mnozica_sportov)
    return koncni_seznam

class Spomeniki:
    def __init__(self):
        self.obiskovalci_ki_so_prisli_na_nek_spomenik = defaultdict(list) #npr. "Vršič" : "Ana", "Berta", "Cilka", ...
        self.stevilo_obiskovalcev_nekega_spomenika = defaultdict(int) #npr. "Vršič" : 3, "Triglav" : 10, ...

    def obisci(self, kolesar, spomenik):
        self.obiskovalci_ki_so_prisli_na_nek_spomenik[spomenik].append(kolesar)
        self.stevilo_obiskovalcev_nekega_spomenika[spomenik] += 1
        if self.stevilo_obiskovalcev_nekega_spomenika[spomenik] == 1:
            return True
        return False

    def obiskanost(self, spomenik):
        return len(set(self.obiskovalci_ki_so_prisli_na_nek_spomenik[spomenik]))

    def spomenikov(self, kolesar):
        stevilo = 0
        for spomenik, kolesarji in self.obiskovalci_ki_so_prisli_na_nek_spomenik.items():
            if kolesar in kolesarji:
                stevilo += 1
        return stevilo

    def prvaki(self):
        slovar_prvakov = dict()
        for spomenik, kolesarji in self.obiskovalci_ki_so_prisli_na_nek_spomenik.items():
            slovar_prvakov[spomenik] = kolesarji[0]
        return slovar_prvakov





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
