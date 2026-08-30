import unittest
import random
from collections import defaultdict
from itertools import combinations


def menjave(razpored, zamenjave):
    mnozica_na_0 = {razpored[0]}
    for i, j in zamenjave:
        razpored[i], razpored[j] = razpored[j], razpored[i]
        mnozica_na_0.add(razpored[0])
    return mnozica_na_0

def najblizji_par(s):
    moznosti = (tuple(sorted((a, b))) for a, b in combinations(s, 2))
    return min(moznosti, key=lambda par: (abs(par[0] - par[1]), par))

def pari(s):
    preostali = list(s)
    rezultat = []
    while len(preostali) >= 2:
        a, b = najblizji_par(preostali)
        rezultat.append((a, b))
        preostali.remove(a)
        preostali.remove(b)
    return rezultat

def bomboni(s, t):
    prazne = set()
    ana_stevilo = 0
    berta_stevilo = 0
    dolzina = max(len(s), len(t))

    for k in range(dolzina):
        box_ana = s[k] if k < len(s) else None
        box_berta = t[k] if k < len(t) else None

        if box_ana is not None and box_berta is not None and box_ana == box_berta:
            prazne.add(box_ana)  # mama vzame bombon - noben od njiju ga ne dobi
            continue

        if box_ana is not None and box_ana not in prazne:
            prazne.add(box_ana)
            ana_stevilo += 1

        if box_berta is not None and box_berta not in prazne:
            prazne.add(box_berta)
            berta_stevilo += 1

    return ana_stevilo, berta_stevilo

def izmenicna_vsota(s):
    if not s:
        return 0
    return s[0] + izmenicna_vsota(s[1:]) * (-1)

class Naloge:
    def __init__(self):
        self.roki = {}          # ime_naloge -> rok, SAMO se caka
        self.stevilo_zamujenih = 0

    def dodaj(self, ime_naloge, rok):
        self.roki[ime_naloge] = rok

    def opravi(self, ime_naloge, cas):
        rok = self.roki.pop(ime_naloge)
        if cas > rok:
            self.stevilo_zamujenih += 1

    def naslednja_naloga(self):
        if not self.roki:
            return None
        return min(self.roki, key=self.roki.get)

    def cakajocih(self):
        return len(self.roki)

    def zamujenih(self):
        return self.stevilo_zamujenih

class Test(unittest.TestCase):
    def test_menjave(self):
        razpored = ["Ana", "Berta", "Cilka", "Dani", "Ema", "Fanči", "Greta"]
        na0 = menjave(razpored, [(0, 4)])
        self.assertEqual(["Ema", "Berta", "Cilka", "Dani", "Ana", "Fanči", "Greta"], razpored)
        self.assertEqual({"Ana", "Ema"}, na0)

        razpored = ["Ana", "Berta", "Cilka", "Dani", "Ema", "Fanči", "Greta"]
        na0 = menjave(razpored, [(0, 4), (1, 2), (0, 2)])
        self.assertEqual(["Berta", "Cilka", "Ema", "Dani", "Ana", "Fanči", "Greta"], razpored)
        self.assertEqual({"Ana", "Ema", "Berta"}, na0)

        razpored = ["Ana", "Berta", "Cilka", "Dani", "Ema", "Fanči", "Greta"]
        na0 = menjave(razpored, [])
        self.assertEqual(["Ana", "Berta", "Cilka", "Dani", "Ema", "Fanči", "Greta"], razpored)
        self.assertEqual({"Ana"}, na0)

    def test_pari(self):
        self.assertEqual((5, 7), najblizji_par([2, -2, 5, 10, 7, 20]))
        self.assertEqual((5, 7), najblizji_par([2, -2, 7, 10, 5, 20]))
        self.assertEqual((-4, -2), najblizji_par([-4, -2, 7, 10, 5, 20]))
        self.assertEqual((-4, -2), najblizji_par([7, 10, -4, -2, 5, 20]))
        self.assertEqual((-4, -2), najblizji_par([7, 10, -4, 5, 20, -2]))
        self.assertEqual((-4, -2), najblizji_par([7, 10, -4, 5, 20, -2]))
        s = [7, 10, -4, 5, 20, -2]
        for _ in range(100):
            random.shuffle(s)
            self.assertEqual((-4, -2), najblizji_par(s), f"Napaka pri f{s}")
        self.assertEqual((5, 6.5), najblizji_par([2, -2, 5, 6.5, 10, 20]))
        self.assertEqual((5, 6.5), najblizji_par([2, -2, 6.5, 5, 10, 20]))

        self.assertEqual([(5, 6.5), (-2, 2), (10, 20)], pari([2, 5, 6.5, -2, 10, 20]))
        self.assertEqual([(5, 6.5), (-2, 2)], pari([2, 5, 6.5, -2, 10]))

    def test_zmage(self):
        s = [4, 1, 4, 7, 4, 3, 5, 6, 8, 5, 3, 2, 4, 6]
        t = [1, 3, 5, 4, 6, 1, 2]
        self.assertEqual((3, 5), bomboni(s, t))
        self.assertEqual((5, 3), bomboni(t, s))

        s = [4, 1, 2, 4, 7, 4, 3, 5, 6, 8, 5, 3, 2, 4, 6]
        t = [1, 3, 2, 5, 4, 6, 1, 2]
        self.assertEqual((3, 4), bomboni(s, t))

        s = [random.randint(1, 10000) for _ in range(10000)]
        t = [random.randint(1, 10000) for _ in range(10000)]
        bomboni(s, t)

    def test_izmenicna_vsota(self):
        self.assertEqual(0, izmenicna_vsota([]), 0)
        self.assertEqual(42, izmenicna_vsota([42]))
        self.assertEqual(42 - 5, izmenicna_vsota([42, 5]))
        self.assertEqual(4 - 1 + 7 - 3 + 6 - 1 + 7 - 6,
                         izmenicna_vsota([4, 1, 7, 3, 6, 1, 7, 6]))
        self.assertEqual(4 - 1 + 7 - 3 + 6 - 1 + 7 - 6 + 5,
                         izmenicna_vsota([4, 1, 7, 3, 6, 1, 7, 6, 5]))

    def test_opravila(self):
        opravila = Naloge()
        self.assertIsNone(opravila.naslednja_naloga())
        self.assertEqual(0, opravila.zamujenih())
        self.assertEqual(0, opravila.cakajocih())

        self.assertIsNone(opravila.dodaj("A", 42))
        opravila.dodaj("B", 30)
        opravila.dodaj("C", 50)
        opravila.dodaj("D", 35)
        self.assertEqual("B", opravila.naslednja_naloga())
        self.assertEqual(0, opravila.zamujenih())
        self.assertEqual(4, opravila.cakajocih())

        self.assertIsNone(opravila.opravi("D", 33))
        self.assertEqual("B", opravila.naslednja_naloga())
        self.assertEqual(0, opravila.zamujenih())
        self.assertEqual(3, opravila.cakajocih())

        opravila.opravi("B", 37)
        self.assertEqual("A", opravila.naslednja_naloga())
        self.assertEqual(1, opravila.zamujenih())
        self.assertEqual(2, opravila.cakajocih())

        opravila.dodaj("D", 40)
        self.assertEqual("D", opravila.naslednja_naloga())
        self.assertEqual(1, opravila.zamujenih())
        self.assertEqual(3, opravila.cakajocih())

        opravila.opravi("A", 42)
        self.assertEqual("D", opravila.naslednja_naloga())
        self.assertEqual(1, opravila.zamujenih())
        self.assertEqual(2, opravila.cakajocih())


if __name__ == "__main__":
    unittest.main()

