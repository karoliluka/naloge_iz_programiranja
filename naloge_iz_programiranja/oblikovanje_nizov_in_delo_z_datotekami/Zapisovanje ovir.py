import os
import warnings
from random import randint
from datetime import datetime
import unittest

def zapisi_ovire(ime_datoteke, ovire):
    kljuci = [kljuc for kljuc, vrednosti in ovire.items()]
    urejeni_kljuci = sorted(kljuci)

    with open(ime_datoteke, "w") as datoteka:
        for kljuc in urejeni_kljuci:
            for vrstica, vrednosti in ovire.items():
                niz = ""
                if vrstica == kljuc:
                    vzorec_vrstica = f"{vrstica:03}:"
                    niz += vzorec_vrstica
                    for (x0, x1) in vrednosti:
                        koordinata = f"{x0:>4}-{x1:<4}"
                        niz += f"{koordinata}"
                    datoteka.write(niz + "\n")

def preberi_ovire(ime_datoteke):
    slovar = dict()
    with open(ime_datoteke) as datoteka:
        vsebina = datoteka.read()
        bloki = vsebina.strip().split("\n\n")

    for blok in bloki:
        seznam = []
        blok = blok.splitlines()
        y = blok[0]
        for (x0, x1) in zip(blok[1::2], blok[2::2]):
            seznam.append((int(x0), int(x1)))
        slovar[int(y)] = seznam
    return slovar

def zapisi_b(ime_datoteke, ovire):
    with open(ime_datoteke, "wb") as datoteka:
        for y, pari in ovire.items():
            datoteka.write(bytes([y, len(pari)]))
            for x0, x1 in pari:
                datoteka.write(bytes([x0, x1]))

def preberi_b(ime_datoteke):
    slovar = dict()
    with open(ime_datoteke, "rb") as datoteka:
        podatki = iter(datoteka.read())
        for y in podatki:
            stevilo_ovir = next(podatki)
            pari = []
            for _ in range(stevilo_ovir):
                x0 = next(podatki)
                x1 = next(podatki)
                pari.append((x0, x1))
            slovar[y] = pari
    return slovar

class Test01Zapis(unittest.TestCase):
    def setUp(self):
        warnings.simplefilter("ignore", ResourceWarning)

        self.ovire = {4: [(5, 6), (9, 11)],
                      13: [(5, 8), (9, 11), (17, 19), (22, 25), (90, 100)],
                      5: [(9, 11), (19, 20), (30, 34)]}

        self.ovire2 = self.ovire | {randint(100, 200): [(1, 2)]}
        with open("ovire.txt", "wt") as f:
            lf = "\n"
            f.write("\n\n".join(fr"{y}{lf}{lf.join(fr'{x0}{lf}{x1}' for x0, x1 in xs)}" for y, xs in self.ovire2.items()))

    def test_01_obvezna_zapisi_ovire(self):
        ime_datoteke = f"ovire{datetime.now().strftime('%m-%d-%H-%M-%S')}.txt"
        zapisi_ovire(ime_datoteke, self.ovire)
        with open(ime_datoteke) as f:
            self.assertEqual("""
004:   5-6      9-11
005:   9-11    19-20    30-34
013:   5-8      9-11    17-19    22-25    90-100
""".strip("\n"), "\n".join(map(str.rstrip, f)))

        self.ovire[101] = self.ovire[5]
        zapisi_ovire(ime_datoteke, self.ovire)
        with open(ime_datoteke) as f:
            self.assertEqual("""
004:   5-6      9-11
005:   9-11    19-20    30-34
013:   5-8      9-11    17-19    22-25    90-100
101:   9-11    19-20    30-34
""".strip("\n"), "\n".join(map(str.rstrip, f)))

        os.remove(ime_datoteke)


    def test_02_dodatna_preberi_ovire(self):
        self.assertEqual(preberi_ovire("ovire.txt"), self.ovire2)

class Test02BinarniZapis(unittest.TestCase):
    def setUp(self):
        warnings.simplefilter("ignore", ResourceWarning)

    def test(self):
        ovire = {4: [(5, 6), (9, 11)],
                 13: [(5, 8), (9, 11), (17, 19), (22, 25), (90, 100)],
                 5: [(9, 11), (19, 20), (30, 34)]}
        zapisi_b("ovire.bin", ovire)
        self.assertEqual(26, len(open("ovire.bin", "rb").read()))
        prebrane = preberi_b("ovire.bin")
        self.assertEqual(ovire, prebrane)

        ovire = {4: [(5, 6), (9, 11)]}
        zapisi_b("ovire.bin", ovire)
        self.assertEqual(6, len(open("ovire.bin", "rb").read()))
        prebrane = preberi_b("ovire.bin")
        self.assertEqual(ovire, prebrane)

        ovire = {}
        zapisi_b("ovire.bin", ovire)
        self.assertEqual(0, len(open("ovire.bin", "rb").read()))
        prebrane = preberi_b("ovire.bin")
        self.assertEqual(ovire, prebrane)


if __name__ == "__main__":
    unittest.main()
