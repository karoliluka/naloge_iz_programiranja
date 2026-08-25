from collections import Counter, defaultdict
from itertools import combinations


def v_karanteno(aktivnosti, okuzene):
    okuzene_aktivnosti = set()
    for ime_osebe, activities in aktivnosti.items():
        for okuzena in okuzene:
            if ime_osebe == okuzena:
                okuzene_aktivnosti |= set(activities)

    okuzene_osebe = set()
    for okuzena_aktivnost in okuzene_aktivnosti:
        for ime_osebe, activities in aktivnosti.items():
            if okuzena_aktivnost in activities:
                okuzene_osebe.add(ime_osebe)

    okuzene_osebe |= set(okuzene)
    return okuzene_osebe

def trojke(s, n):
    stevec = Counter(s[i:i+3] for i in range(len(s) - 2))
    urejene = sorted(stevec, key=lambda t: (stevec[t], t), reverse=True)
    return urejene[:n]

def statistika(podatki, drzava, n):
    for podatek in podatki.split("\n"):
        ime_drzave = podatek.strip().split(":")[0]
        okuzeni = podatek.strip().split(":")[1]
        seznam_podatkov = [int(x) for x in okuzeni.strip().split(",")]
        if ime_drzave == drzava:
            return sum(seznam_podatkov[-n:])
    return 0

def okuzeni(dan, oseba, okuzbe):
    if not okuzbe[oseba]:
        return {oseba}

    mnozica_okuzenih = {oseba}
    for ime, slovar_okuzenih in okuzbe.items():
        if ime == oseba:
            for ime_okuzene, dan_okuzbe in slovar_okuzenih.items():
                if dan_okuzbe <= dan:
                    mnozica_okuzenih |= okuzeni(dan, ime_okuzene, okuzbe)
    return mnozica_okuzenih

class Oseba:
    def __init__(self):
        self.aktivnosti = []  # seznam VSEH (aktivnost, cas) parov, brez prepisovanja

    def aktivnost(self, kaj, kdaj):
        self.aktivnosti.append((kaj, kdaj))

    def vse_aktivnosti(self):
        return {kaj for kaj, kdaj in self.aktivnosti}

    def mozna_okuzba(self, druga_oseba):
        return bool(set(self.aktivnosti) & set(druga_oseba.aktivnosti))

class VarnaOseba(Oseba):
    def __init__(self, mnozica_maskiranih_aktivnosti):
        super().__init__()
        self.mnozica_maskiranih_aktivnosti = mnozica_maskiranih_aktivnosti

    def mozna_okuzba(self, druga_oseba):
        skupni = set(self.aktivnosti) & set(druga_oseba.aktivnosti)
        for aktivnost, cas in skupni:
            if aktivnost not in druga_oseba.mnozica_maskiranih_aktivnosti:
                return True
        return False


import unittest

class Test(unittest.TestCase):
    def test_01_stiki(self):
        aktivnosti = {
            "Ana": ["kava", "trgovina", "kava", "burek"],
            "Berta": ["telovadba", "frizer"],
            "Cilka": ["telovadba"],
            "Dani": [],
            "Ema": ["kava", "telovadba"],
            "Fanči": ["frizer"],
            "Greta": ["lokostrelstvo", "kolesarjenje"]
        }
        self.assertEqual(
            {"Ana", "Berta", "Cilka", "Ema", "Fanči"},
            v_karanteno(aktivnosti, ["Ana", "Berta"]))
        self.assertEqual(
            {"Berta", "Cilka", "Ema", "Fanči"},
            v_karanteno(aktivnosti, ["Berta"]))
        self.assertEqual(
            {"Dani", "Greta"},
            v_karanteno(aktivnosti, ["Dani", "Greta"]))
        self.assertEqual(
            {"Dani"},
            v_karanteno(aktivnosti, ["Dani"]))
        self.assertEqual(
            {"Greta"},
            v_karanteno(aktivnosti, ["Greta"]))

    def test_02_pogoste_trojke(self):
        self.assertEqual(
            ['acg', 'tac', 'cga', 'gta', 'gat'],
            trojke("acgtacgatacgacg", 5)
        )

        self.assertEqual(
            ['acg', 'tac'],
            trojke("acgtacgatacgacg", 2)
        )

        self.assertEqual(
            ['cga', 'tcg', 'atc', 'gat', 'gtg'],
            trojke("acagtgcagcatcgatcgacatcgagtggggctacgatcgatcgatcgac", 5)
        )
        self.assertEqual(
            ['cga', 'acg', 'gac'],
            trojke("acgacgacgacga", 5)
        )
        self.assertEqual(
            ['cga', 'acg', 'gac'],
            trojke("acgacgacgacga", 5)
        )

        self.assertEqual(
            ['taa', 'aaa'],
            trojke('taaa', 2)
        )

        self.assertEqual(
            ['aaa', 'taa'],
            trojke('taaaa', 2)
        )

        spike = "tgtttgtttttcttgttttattgccactagtctctagtcagtgtgttaatcttacaaccagaactcaattaccccctgcatacactaattctttcacacgtggtgtttattaccctgacaaagttttcagatcctcagttttacattcaactcaggacttgttcttacctttcttttccaatgttacttggttccatgctatacatgtctctgggaccaatggtactaagaggtttgataaccctgtcctaccatttaatgatggtgtttattttgcttccactgagaagtctaacataataagaggctggatttttggtactactttagattcgaagacccagtccctacttattgttaataacgctactaatgttgttattaaagtctgtgaatttcaattttgtaatgatccatttttgggtgtttattaccacaaaaacaacaaaagttggatggaaagtgagttcagagtttattctagtgcgaataattgcacttttgaatatgtctctcagccttttcttatggaccttgaaggaaaacagggtaatttcaaaaatcttagggaatttgtgtttaagaatattgatggttattttaaaatatattctaagcacacgcctattaatttagtgcgtgatctccctcagggtttttcggctttagaaccattggtagatttgccaataggtattaacatcactaggtttcaaactttacttgctttacatagaagttatttgactcctggtgattcttcttcaggttggacagctggtgctgcagcttattatgtgggttatcttcaacctaggacttttctattaaaatataatgaaaatggaaccattacagatgctgtagactgtgcacttgaccctctctcagaaacaaagtgtacgttgaaatccttcactgtagaaaaaggaatctatcaaacttctaactttagagtccaaccaacagaatctattgttagatttcctaatattacaaacttgtgcccttttggtgaagtttttaacgccaccagatttgcatctgtttatgcttggaacaggaagagaatcagcaactgtgttgctgattattctgtcctatataattccgcatcattttccacttttaagtgttatggagtgtctcctactaaattaaatgatctctgctttactaatgtctatgcagattcatttgtaattagaggtgatgaagtcagacaaatcgctccagggcaaactggaaagattgctgattataattataaattaccagatgattttacaggctgcgttatagcttggaattctaacaatcttgattctaaggttggtggtaattataattacctgtatagattgtttaggaagtctaatctcaaaccttttgagagagatatttcaactgaaatctatcaggccggtagcacaccttgtaatggtgttgaaggttttaattgttactttcctttacaatcatatggtttccaacccactaatggtgttggttaccaaccatacagagtagtagtactttcttttgaacttctacatgcaccagcaactgtttgtggacctaaaaagtctactaatttggttaaaaacaaatgtgtcaatttcaacttcaatggtttaacaggcacaggtgttcttactgagtctaacaaaaagtttctgcctttccaacaatttggcagagacattgctgacactactgatgctgtccgtgatccacagacacttgagattcttgacattacaccatgttcttttggtggtgtcagtgttataacaccaggaacaaatacttctaaccaggttgctgttctttatcaggatgttaactgcacagaagtccctgttgctattcatgcagatcaacttactcctacttggcgtgtttattctacaggttctaatgtttttcaaacacgtgcaggctgtttaataggggctgaacatgtcaacaactcatatgagtgtgacatacccattggtgcaggtatatgcgctagttatcagactcagactaattctcctcggcgggcacgtagtgtagctagtcaatccatcattgcctacactatgtcacttggtgcagaaaattcagttgcttactctaataactctattgccatacccacaaattttactattagtgttaccacagaaattctaccagtgtctatgaccaagacatcagtagattgtacaatgtacatttgtggtgattcaactgaatgcagcaatcttttgttgcaatatggcagtttttgtacacaattaaaccgtgctttaactggaatagctgttgaacaagacaaaaacacccaagaagtttttgcacaagtcaaacaaatttacaaaacaccaccaattaaagattttggtggttttaatttttcacaaatattaccagatccatcaaaaccaagcaagaggtcatttattgaagatctacttttcaacaaagtgacacttgcagatgctggcttcatcaaacaatatggtgattgccttggtgatattgctgctagagacctcatttgtgcacaaaagtttaacggccttactgttttgccacctttgctcacagatgaaatgattgctcaatacacttctgcactgttagcgggtacaatcacttctggttggacctttggtgcaggtgctgcattacaaataccatttgctatgcaaatggcttataggtttaatggtattggagttacacagaatgttctctatgagaaccaaaaattgattgccaaccaatttaatagtgctattggcaaaattcaagactcactttcttccacagcaagtgcacttggaaaacttcaagatgtggtcaaccaaaatgcacaagctttaaacacgcttgttaaacaacttagctccaattttggtgcaatttcaagtgttttaaatgatatcctttcacgtcttgacaaagttgaggctgaagtgcaaattgataggttgatcacaggcagacttcaaagtttgcagacatatgtgactcaacaattaattagagctgcagaaatcagagcttctgctaatcttgctgctactaaaatgtcagagtgtgtacttggacaatcaaaaagagttgatttttgtggaaagggctatcatcttatgtccttccctcagtcagcacctcatggtgtagtcttcttgcatgtgacttatgtccctgcacaagaaaagaacttcacaactgctcctgccatttgtcatgatggaaaagcacactttcctcgtgaaggtgtctttgtttcaaatggcacacactggtttgtaacacaaaggaatttttatgaaccacaaatcattactacagacaacacatttgtgtctggtaactgtgatgttgtaataggaattgtcaacaacacagtttatgatcctttgcaacctgaattagactcattcaaggaggagttagataaatattttaagaatcatacatcaccagatgttgatttaggtgacatctctggcattaatgcttcagttgtaaacattcaaaaagaaattgaccgcctcaatgaggttgccaagaatttaaatgaatctctcatcgatctccaagaacttggaaagtatgagcagtatataaaatggccatggtacatttggctaggttttatagctggcttgattgccatagtaatggtgacaattatgctttgctgtatgaccagttgctgtagttgtctcaagggctgttgttcttgtggatcctgctgcaaatttgatgaagacgactctgagccagtgctcaaaggagtcaaattacattacacataa"
        self.assertEqual(
            ['ttt', 'att', 'ttg', 'aat', 'aaa'],
            trojke(spike, 5)
        )

        self.assertEqual(
            ['ttt', 'att', 'ttg', 'aat', 'aaa', 'tta', 'caa', 'aca'],
            trojke(spike, 8)
        )

    def test_03_statistika(self):
        podatki = """Slovenija:31,20,25,14,50,60
Hrvaška:150,170,200,220,221
Madžarska:100,70,35"""
        self.assertEqual(124, statistika(podatki, "Slovenija", 3))
        self.assertEqual(60, statistika(podatki, "Slovenija", 1))
        self.assertEqual(200, statistika(podatki, "Slovenija", 6))
        self.assertEqual(205, statistika(podatki, "Madžarska", 3))
        self.assertEqual(205, statistika(podatki, "Madžarska", 5))
        self.assertEqual(0, statistika(podatki, "Zanzibar", 5))

    def test_04_okuzeni(self):
        okuzbe = {
            "Ana": {"Berta": 6, "Cilka": 12, "Dani": 6},
            "Berta": {},
            "Cilka": {"Ema": 18, "Fanči": 30},
            "Dani": {"Greta": 9},
            "Ema": {"Helga": 24, "Iva": 36, "Jana": 27},
            "Fanči": {},
            "Greta": {"Klara": 12},
            "Helga": {},
            "Iva": {},
            "Jana": {},
            "Klara": {}
        }
        self.assertEqual(
            {"Ana", "Berta", "Cilka", "Dani", "Greta", "Klara"},
            okuzeni(15, "Ana", okuzbe))
        self.assertEqual(
            {"Ana", "Berta", "Dani"},
            okuzeni(6, "Ana", okuzbe))
        self.assertEqual(
            {"Ana", "Berta", "Cilka", "Dani", "Ema", "Fanči", "Greta", "Helga", "Jana", "Klara"},
            okuzeni(30, "Ana", okuzbe))
        self.assertEqual(
            set(okuzbe),
            okuzeni(300, "Ana", okuzbe))
        self.assertEqual(
            {"Ana"},
            okuzeni(3, "Ana", okuzbe))

        self.assertEqual(
            {"Cilka", "Ema", "Helga"},
            okuzeni(26, "Cilka", okuzbe)
        )
        self.assertEqual(
            {"Cilka", "Ema", "Helga", "Jana"},
            okuzeni(28, "Cilka", okuzbe)
        )
        self.assertEqual(
            {"Cilka", "Ema", "Helga", "Jana"},
            okuzeni(27, "Cilka", okuzbe)
        )
        self.assertEqual(
            {"Dani", "Greta", "Klara"},
            okuzeni(30, "Dani", okuzbe)
        )
        self.assertEqual(
            {"Dani", "Greta"},
            okuzeni(10, "Dani", okuzbe)
        )

    def test_05_sledilnik_oseba(self):
        ana = Oseba()
        ana.aktivnost("kava", 15)
        ana.aktivnost("trgovina", 22)
        ana.aktivnost("kava", 25)
        self.assertEqual({"kava", "trgovina"}, ana.vse_aktivnosti())

        berta = Oseba()
        berta.aktivnost("kava", 12)
        berta.aktivnost("kava", 15)
        berta.aktivnost("frizer", 22)
        self.assertEqual({"kava", "frizer"}, berta.vse_aktivnosti())

        cilka = Oseba()
        cilka.aktivnost("trgovina", 25)
        cilka.aktivnost("frizer", 22)
        cilka.aktivnost("kava", 21)
        self.assertEqual({"kava", "trgovina", "frizer"}, cilka.vse_aktivnosti())

        self.assertTrue(ana.mozna_okuzba(berta))
        self.assertTrue(berta.mozna_okuzba(ana))

        self.assertTrue(cilka.mozna_okuzba(berta))
        self.assertTrue(berta.mozna_okuzba(cilka))

        self.assertFalse(ana.mozna_okuzba(cilka))
        self.assertFalse(cilka.mozna_okuzba(ana))

    def test_05_sledilnik_varna_oseba(self):
        ana = VarnaOseba({"trgovina", "frizer"})
        ana.aktivnost("kava", 15)
        ana.aktivnost("trgovina", 22)
        ana.aktivnost("kava", 25)
        self.assertEqual({"kava", "trgovina"}, ana.vse_aktivnosti())

        berta = VarnaOseba({"frizer"})
        berta.aktivnost("kava", 12)
        berta.aktivnost("kava", 25)
        berta.aktivnost("frizer", 22)
        self.assertEqual({"kava", "frizer"}, berta.vse_aktivnosti())

        cilka = VarnaOseba({"trgovina"})
        cilka.aktivnost("trgovina", 25)
        cilka.aktivnost("frizer", 22)
        cilka.aktivnost("kava", 21)
        self.assertEqual({"kava", "trgovina", "frizer"}, cilka.vse_aktivnosti())

        self.assertTrue(ana.mozna_okuzba(berta))
        self.assertTrue(berta.mozna_okuzba(ana))

        self.assertFalse(cilka.mozna_okuzba(berta))
        self.assertTrue(berta.mozna_okuzba(cilka))

        self.assertFalse(ana.mozna_okuzba(cilka))
        self.assertFalse(cilka.mozna_okuzba(ana))


if __name__ == "__main__":
    unittest.main()
