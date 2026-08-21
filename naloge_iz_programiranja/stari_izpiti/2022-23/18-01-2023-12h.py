from collections import defaultdict
from itertools import pairwise


def skupni_odsek(pot1, pot2):
    je_zacetek = False
    seznam_dolzin = []
    dolzina = 0

    for char1, char2 in zip(pot1, pot2):
        if char1 == char2 and je_zacetek is False:
            dolzina += 1
            je_zacetek = True
        elif char1 == char2 and je_zacetek is True:
            dolzina += 1
        elif char1 != char2 and je_zacetek is True:
            seznam_dolzin.append(dolzina)
            dolzina = 0
            je_zacetek = False

    if je_zacetek:
        seznam_dolzin.append(dolzina)

    if seznam_dolzin:
        return max(seznam_dolzin)
    return 0

def vecji_frajer(pot1, pot2, zemljevid):
    stevilo_prvi = defaultdict(int)
    for krizisce in pairwise(pot1):
        for vescina in zemljevid[krizisce]:
            stevilo_prvi[vescina] += 1

    stevilo_drugi = defaultdict(int)
    for krizisce in pairwise(pot2):
        for vescina in zemljevid[krizisce]:
            stevilo_drugi[vescina] += 1

    for vescina, stevilo in stevilo_drugi.items():
        if stevilo_prvi[vescina] < stevilo:
            return False

    for vescina in (set(stevilo_prvi) | set(stevilo_drugi)):
        if stevilo_prvi[vescina] > stevilo_drugi[vescina]:
            return True
    return False

def koristne_vescine(tocka, zemljevid):
    rezultat = set()
    for (izvor, cilj) in zemljevid:
        if izvor == tocka and cilj > tocka:
            rezultat |= zemljevid[(izvor, cilj)]
            rezultat |= koristne_vescine(cilj, zemljevid)
    return rezultat

def preberi_zemljevid_vescin(ime_datoteke):
    slovar = defaultdict(set)
    with open(ime_datoteke, "r", encoding="utf-8") as datoteka:
        for vrstica in datoteka:
            if len(vrstica.strip().split(": ")) == 2:
                vescina = vrstica.strip().split(": ")[0]
                krizisca = vrstica.strip().split(": ")[1]
                seznam_krizisc = krizisca.split(", ")
                for krizisce in seznam_krizisc:
                    prvo = krizisce.split("-")[0]
                    drugo = krizisce.split("-")[1]
                    slovar[(prvo, drugo)].add(vescina)
    return slovar


# Rešitev naloge 5 mora biti napisana pod tem razredom, sicer ne bo delovala!

class Kolesar:
    def __init__(self, lokacija, zemljevid, vescine):
        self.lokacija_ = lokacija
        self.zemljevid = zemljevid
        self.vescine = vescine

    def premik(self, kam):
        if self.zemljevid.get((self.lokacija_, kam), {None}) <= self.vescine:
            self.lokacija_ = kam
        else:
            self.lokacija_ = None

    def lokacija(self):
        return self.lokacija_

class Frajer(Kolesar):
    def __init__(self, zacetna_tocka, zemljevid, mnozica_vescin):
        super().__init__(zacetna_tocka, zemljevid, mnozica_vescin)
        self.stevilo_zivljenj = 3
        self.uporabljene_vescine = set()

    def premik(self, kam):
        if self.lokacija_ is None:
            return  # ze dokoncno oblezal - nic vec se ne zgodi

        prejsnja_lokacija = self.lokacija_
        super().premik(kam)  # poklici PODEDOVANO metodo, ne self.premik!

        if self.lokacija_ is None:
            # premik ni uspel
            self.stevilo_zivljenj -= 1
            if self.stevilo_zivljenj > 0:
                self.lokacija_ = prejsnja_lokacija  # obnovi - se lahko poskusa znova
            # ce je stevilo_zivljenj == 0, ostane None - dokoncno je oblezal
        else:
            # premik je uspel - zabelezi uporabljene vescine na tej povezavi
            self.uporabljene_vescine |= self.zemljevid[(prejsnja_lokacija, kam)]

    def zivljenja(self):
        return self.stevilo_zivljenj

    def uporabljene(self):
        return self.uporabljene_vescine


import unittest
import random
import warnings
import os

A, B, C, D, E, F, G, H, I, J, K, L, M, N, O, P, R, S, T, U, V = "ABCDEFGHIJKLMNOPRSTUV"

proto_zemljevid = {
    (A, B): "gravel trava",
    (A, V): "pešci lonci",
    (B, C): "bolt lonci",
    (B, V): "",
    (C, R): "stopnice pešci lonci",
    (D, F): "stopnice pešci",
    (D, R): "pešci",
    (E, I): "trava lonci",
    (F, G): "trava črepinje",
    (G, H): "črepinje pešci",
    (G, I): "avtocesta",
    (H, J): "robnik bolt",
    (I, M): "avtocesta",
    (I, P): "gravel",
    (I, R): "stopnice robnik",
    (J, K): "",
    (J, L): "gravel bolt",
    (K, M): "stopnice bolt",
    (L, M): "robnik pešci",
    (M, N): "rodeo",
    (N, P): "gravel",
    (O, P): "gravel",
    (P, S): "",
    (R, U): "trava pešci",
    (R, V): "pešci lonci",
    (S, T): "robnik trava",
    (T, U): "gravel trava",
    (U, V): "robnik lonci trava"
}

zemljevid = {k: set(v.split()) for k, v in proto_zemljevid.items()} | {k[::-1]: set(v.split()) for k, v in proto_zemljevid.items()}


class Test(unittest.TestCase):
    def setUp(self):
        warnings.simplefilter("ignore", ResourceWarning)

    def test_1_skupni_odsek(self):
        #                                      vvvvv
        self.assertEqual(5, skupni_odsek("ABCDEFGHIJKLMNOP",
                                         "BCDEMFGHIJXOAEFD"))
        #                                  vv  vvvvv   vvv
        self.assertEqual(5, skupni_odsek("ABCDEFGHIJKLMNOP",
                                         "XBDEMFGHIJXOANOP"))
        #                                  vv  vv vv   vvv
        self.assertEqual(3, skupni_odsek("ABCDEFGLIJKLMNOP",
                                         "XBDEMFGHIJXOANOP"))
        #                                 vvvv vv vv   vvv
        self.assertEqual(4, skupni_odsek("ABCDEFGLIJKLMNOP",
                                         "ABCDMFGHIJXOANOP"))
        #                                 vv v vv vv   vvv
        self.assertEqual(3, skupni_odsek("ABXDEFGLIJKLMNOPABC",
                                         "ABCDMFGHIJXOANOP"))
        #                                 vv v vv vv   vvv
        self.assertEqual(3, skupni_odsek("ABXDEFGLIJKLMNOP",
                                         "ABCDMFGHIJXOANOPABC"))
        #
        self.assertEqual(0, skupni_odsek("ABXDEFGLIJKLMNOP",
                                         ""))
        #                                 v
        self.assertEqual(1, skupni_odsek("ABXDEFGLIJKLMNOP",
                                         "AFHDJEX"))
        #                                   v
        self.assertEqual(1, skupni_odsek("ABXDEFGLIJKLMNOP",
                                         "LAXYJEX"))
        #                                       v
        self.assertEqual(1, skupni_odsek("ABRDEFXLIJKLMNOP",
                                         "LAXDJEX"))
        #                                       v
        self.assertEqual(1, skupni_odsek("ABRDEFX",
                                         "LAXDJEXLIJKLMNOP"))

    def test_2_vecji_frajer(self):
        # prvi ima en p več
        self.assertTrue(vecji_frajer("RDFGI", "IGFD", zemljevid))
        # prvi ima a, ki ga drugi nima
        self.assertTrue(vecji_frajer("RDFGI", "GFDR", zemljevid))
        # drugi ima en p več
        self.assertFalse(vecji_frajer("IGFD", "RDFGI", zemljevid))
        # drugi ima a, ki ga prvi nima
        self.assertFalse(vecji_frajer("GFDR", "RDFGI", zemljevid))
        # prvi ima a, ki ga drugi nima, vendar ima drugi dodatni č
        self.assertFalse(vecji_frajer("RDFGI", "DFGH", zemljevid))
        # in obratno
        self.assertFalse(vecji_frajer("DFGH", "RDFGI", zemljevid))
        # izenačena sta
        self.assertFalse(vecji_frajer("OPIE", "OPIE", zemljevid))
        self.assertFalse(vecji_frajer("OPIE", "EIPN", zemljevid))
        self.assertFalse(vecji_frajer("MN", "NM", zemljevid))

        self.assertTrue(vecji_frajer("ABCRU", "AB", zemljevid))
        self.assertTrue(vecji_frajer("ABCRU", "A", zemljevid))
        self.assertTrue(vecji_frajer("ABCRU", "", zemljevid))

        self.assertFalse(vecji_frajer("AB", "ABCRU", zemljevid))
        self.assertFalse(vecji_frajer("A", "ABCRU", zemljevid))
        self.assertFalse(vecji_frajer("", "ABCRU", zemljevid))

    def test_3_preberi_zemljevid_vescin(self):
        vx2 = vx = f"vescina{random.randint(0, 1000)}"
        while vx2 == vx:
            vx2 = f"vescina{random.randint(0, 1000)}"
        kx = "".join(random.choice("GHIJKLMNOPQRSTUVWXYZ") for _ in range(5))
        fname = f"zemljevid{random.randint(1000, 9999)}.txt"
        try:
            with open(fname, "wt") as f:
                f.write(f"""grava: A-B, B-C
travel: A-B
avtocesta: B-C
pesek: A-B, A-C, D-{kx}
crepinje: B-C, A-E
pesci: A-E
{vx}: D-{kx}
{vx2}:
""")

            self.assertEqual({(A, B): {"grava", "travel", "pesek"},
                              (A, C): {"pesek"},
                              (B, C): {"grava", "crepinje", "avtocesta"},
                              (A, E): {"crepinje", "pesci"},
                              (D, kx): {"pesek", vx}}, preberi_zemljevid_vescin(fname))
        finally:
            os.remove(fname)

    def test_4_koristne_vescine(self):
        self.assertEqual(set(), koristne_vescine("V", zemljevid))
        self.assertEqual({'trava', 'robnik', 'lonci'},
                         koristne_vescine("U", zemljevid))
        self.assertEqual({'gravel', 'trava', 'robnik', 'lonci'},
                         koristne_vescine("P", zemljevid))
        self.assertEqual({'rodeo', 'lonci', 'trava', 'gravel', 'robnik'},
                         koristne_vescine("M", zemljevid))
        self.assertEqual({'robnik', 'bolt', 'lonci', 'pešci', 'stopnice', 'trava', 'gravel'},
                         koristne_vescine("A", zemljevid))
        self.assertEqual({'avtocesta', 'gravel', 'lonci', 'pešci', 'robnik', 'rodeo', 'stopnice', 'trava'},
                         koristne_vescine("E", zemljevid))

    def test_5_frajer(self):
        ana = Frajer("A", zemljevid, {"gravel", "trava", "pešci", "lonci", "bolt"})

        self.assertEqual("A", ana.lokacija())
        self.assertEqual(set(), ana.uporabljene())
        ana.premik("B")
        self.assertEqual(3, ana.zivljenja())
        self.assertEqual("B", ana.lokacija())
        self.assertEqual({"gravel", "trava"}, ana.uporabljene())
        self.assertEqual(3, ana.zivljenja())
        ana.premik("A")
        self.assertEqual("A", ana.lokacija())
        self.assertEqual({"gravel", "trava"}, ana.uporabljene())
        self.assertEqual(3, ana.zivljenja())
        ana.premik("V")
        self.assertEqual("V", ana.lokacija())
        self.assertEqual({"gravel", "trava", "pešci", "lonci"}, ana.uporabljene())
        self.assertEqual(3, ana.zivljenja())
        ana.premik("R")
        self.assertEqual("R", ana.lokacija())
        self.assertEqual({"gravel", "trava", "pešci", "lonci"}, ana.uporabljene())
        ana.premik("C")  # pade po stopnicah in izgubi eno življenje!
        self.assertEqual("R", ana.lokacija())  # ostane v R
        self.assertEqual({"gravel", "trava", "pešci", "lonci"}, ana.uporabljene())
        self.assertEqual(2, ana.zivljenja())
        ana.premik("B")  # ojoj, še eno življenje - iz R v B ni poti!
        self.assertEqual("R", ana.lokacija())  # ostane v R
        self.assertEqual({"gravel", "trava", "pešci", "lonci"}, ana.uporabljene())
        self.assertEqual(1, ana.zivljenja())
        ana.premik("V")  # to pa gre
        self.assertEqual("V", ana.lokacija())
        self.assertEqual({"gravel", "trava", "pešci", "lonci"}, ana.uporabljene())
        self.assertEqual(1, ana.zivljenja())
        ana.premik("B")
        self.assertEqual("B", ana.lokacija())
        self.assertEqual({"gravel", "trava", "pešci", "lonci"}, ana.uporabljene())
        self.assertEqual(1, ana.zivljenja())
        ana.premik("C")
        self.assertEqual("C", ana.lokacija())
        self.assertEqual({"gravel", "trava", "pešci", "lonci", "bolt"}, ana.uporabljene())
        self.assertEqual(1, ana.zivljenja())
        ana.premik("R")   # Pade pod stopnicah. Zdaj je bilo tretjič, zato je konec
        self.assertIsNone(ana.lokacija())
        self.assertEqual({"gravel", "trava", "pešci", "lonci", "bolt"}, ana.uporabljene())
        self.assertEqual(0, ana.zivljenja())
        ana.premik("V")   # Leži pod stopnicami in se ne premakne
        self.assertIsNone(ana.lokacija())
        self.assertEqual({"gravel", "trava", "pešci", "lonci", "bolt"}, ana.uporabljene())
        self.assertEqual(0, ana.zivljenja())


if __name__ == "__main__":
    unittest.main()

