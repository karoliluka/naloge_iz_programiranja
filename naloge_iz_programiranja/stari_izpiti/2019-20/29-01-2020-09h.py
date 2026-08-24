import unittest
import warnings
from collections import Counter, defaultdict
from enum import unique

from risar import cakaj


def brisi_ponovitve(s):
    temp_seznam = []
    for x in s:
        st_dovoljenih_ponovitev_x = x
        if temp_seznam.count(x) < st_dovoljenih_ponovitev_x:
            temp_seznam.append(x)
        else:
            continue
    s[:] = temp_seznam

def najvecji_v_vseh(s):
    if not s:
        return None

    skupni = set(s[0])
    for podseznam in s[1:]:
        skupni &= set(podseznam)
        if not skupni:
            return None

    return max(skupni) if skupni else None

def vrstni_red(ime_datoteke):
    terke_tekmovalcev = []
    with open(ime_datoteke, "r") as datoteka:
        for vrstica in datoteka:
            ime_tekmovalca = vrstica.strip().split(": ")[0]
            cas_tekmovalca = vrstica.strip().split(": ")[1]
            minute_tekmovalca, sekunde_tekmovalca = cas_tekmovalca.split(":")
            skupen_cas = (int(minute_tekmovalca) * 60) + int(sekunde_tekmovalca)
            terke_tekmovalcev.append((ime_tekmovalca, skupen_cas))

    sortirane_terke = sorted(terke_tekmovalcev, key=lambda terka: terka[1])
    seznam_tekmovalcev = [ime for ime, cas in sortirane_terke]
    return seznam_tekmovalcev

def preveri_vsoto(s, n):
    if not s:
        return n == 0
    return preveri_vsoto(s[1:], n - s[0])

class Cakalnica:
    def __init__(self):
        self.seznam_cakajocih = []
        self.skupni_cas = 0
        self.stevilo_oseb = 0

    def prihod(self, ime, cas):
        self.seznam_cakajocih.append((ime , cas))

    def cakajocih(self):
        return len(self.seznam_cakajocih)

    def naslednji(self, cas):
        if not self.seznam_cakajocih:
            return None
        else:
            ime_osebe, cas_prihoda = self.seznam_cakajocih.pop(0)
            cakanje = cas - cas_prihoda
            self.skupni_cas += cakanje
            self.stevilo_oseb += 1
        return ime_osebe

    def skupni_cas_cakanja(self):
        return self.skupni_cas

    def povprecni_cas_cakanja(self):
        if self.stevilo_oseb == 0:
            return 0
        return self.skupni_cas / self.stevilo_oseb






class Test(unittest.TestCase):
    def setUp(self) -> None:
        warnings.simplefilter("ignore", ResourceWarning)

    def test_01_brisi_ponovitve(self):
        a = [1, 3, 4, 1, 3, 2, 2, 3, 5, 3, 2, 4]
        self.assertIsNone(brisi_ponovitve(a), "Funkcija naj ne vrne ničesar")
        self.assertEqual([1, 3, 4, 3, 2, 2, 3, 5, 4], a)

        a = [3, 1, 3, 3, 2, 3, 4, 3, 3, 3, 5, 3, 6]
        brisi_ponovitve(a)
        self.assertEqual([3, 1, 3, 3, 2, 4, 5, 6], a)

    def test_02_najvecji_v_vseh(self):
        self.assertEqual(3, najvecji_v_vseh([[5, 1, 2, 3], [3, 1, 8], [42, 5, 3, 1]]))
        self.assertIsNone(najvecji_v_vseh([[5, 1, 2, 3], [4, 1, 8], [42, 5, 3, 2]]))
        self.assertIsNone(najvecji_v_vseh([]))

        a = list(range(1_000_000)) + list(range(2_000_000, 2_100_000))
        b = list(range(500_000, 1_500_000))
        self.assertEqual(999_999, najvecji_v_vseh([a, b]))

    def test_03_vrstni_red(self):
        with open("f1.txt", "wt") as f:
            f.write("""Ana Anžič: 5:12
Berta Bertolin: 4:48
Cilka Centrih: 5:05
Dani Dolinar: 10:12
Ema Evelina Estrih: 4:45""")
        self.assertEqual(
            ["Ema Evelina Estrih", "Berta Bertolin", "Cilka Centrih", "Ana Anžič", "Dani Dolinar"],
            vrstni_red("f1.txt"))

        with open("f1.txt", "wt") as f:
            f.write("""Ana Anžič: 5:12
Berta Bertolin: 4:45
Cilka Centrih: 5:05
Dani Dolinar: 10:12
Ema Evelina Estrih: 4:45""")
        self.assertEqual(
            ["Berta Bertolin", "Ema Evelina Estrih", "Cilka Centrih", "Ana Anžič", "Dani Dolinar"],
            vrstni_red("f1.txt"))

    def test_04_preveri_vsoto(self):
        try:
            preveri_vsoto(list(range(1111)), 4_000_000)
            self.fail("Funkcija mora biti rekurzivna")
        except RecursionError:
            pass
        self.assertTrue(preveri_vsoto([5, 1, 2, 5, 6], 19))
        self.assertFalse(preveri_vsoto([5, 1, 2, 5, 6], 22))
        self.assertFalse(preveri_vsoto([5, 1, 2, 5, 6], 0))
        self.assertFalse(preveri_vsoto([], 19))
        self.assertTrue(preveri_vsoto([], 0))

    def test_05_cakalnica(self):
        cakalnica = Cakalnica()
        self.assertEqual(0, cakalnica.cakajocih())
        self.assertEqual(0, cakalnica.skupni_cas_cakanja())
        self.assertIsNone(cakalnica.naslednji(8.00))

        self.assertIsNone(cakalnica.prihod("Dani", 8.50))
        cakalnica.prihod("Berta", 9.00)
        cakalnica.prihod("Cilka", 9.25)
        self.assertEqual(3, cakalnica.cakajocih())
        self.assertEqual(0, cakalnica.skupni_cas_cakanja())

        self.assertEqual("Dani", cakalnica.naslednji(9.75))
        self.assertEqual(2, cakalnica.cakajocih())
        self.assertAlmostEqual(1.25, cakalnica.skupni_cas_cakanja())
        self.assertAlmostEqual(1.25, cakalnica.povprecni_cas_cakanja())

        self.assertEqual("Berta", cakalnica.naslednji(10))
        self.assertEqual(1, cakalnica.cakajocih())
        self.assertAlmostEqual(1.25 + 1, cakalnica.skupni_cas_cakanja())
        self.assertAlmostEqual((1.25 + 1) / 2, cakalnica.povprecni_cas_cakanja())

        self.assertEqual("Cilka", cakalnica.naslednji(10.15))
        self.assertEqual(0, cakalnica.cakajocih())
        self.assertAlmostEqual(1.25 + 1 + 0.9, cakalnica.skupni_cas_cakanja())
        self.assertAlmostEqual((1.25 + 1 + 0.9) / 3, cakalnica.povprecni_cas_cakanja())

        self.assertIsNone(cakalnica.naslednji(10.15))
        self.assertEqual(0, cakalnica.cakajocih())
        self.assertAlmostEqual(1.25 + 1 + 0.9, cakalnica.skupni_cas_cakanja())
        self.assertAlmostEqual((1.25 + 1 + 0.9) / 3, cakalnica.povprecni_cas_cakanja())


if __name__ == "__main__":
    unittest.main()
