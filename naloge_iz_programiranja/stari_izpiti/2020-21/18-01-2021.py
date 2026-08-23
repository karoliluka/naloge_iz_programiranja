import unittest
from collections import defaultdict, Counter


def valovi(po_dnevih):
    nov_seznam = []
    zacetek_vala = False
    vsota_vala = 0
    indeks_vala = 0
    for i, dan in enumerate(po_dnevih):
        if dan > 0 and zacetek_vala is False:
            vsota_vala += dan
            zacetek_vala = True
        elif dan > 0 and zacetek_vala is True:
            vsota_vala += dan
        elif dan == 0 and zacetek_vala is True:
            nov_seznam.append(vsota_vala)
            zacetek_vala = False
            vsota_vala = 0
            indeks_vala = i

    if zacetek_vala:
        nov_seznam.append(sum(po_dnevih[indeks_vala:]))

    return nov_seznam

def sledilnik(dnevi):
    mnozica_zaprtih = set()
    mnozica_odprtih = set()
    st_zaprtnih = []
    for dan in dnevi:
        mnozica_zaprtih |= set(dan[0])
        mnozica_odprtih |= set(dan[1])
        mnozica_zaprtih -= mnozica_odprtih
        st_zaprtnih.append(len(mnozica_zaprtih))
    return max(st_zaprtnih)

def okuzeni(oseba, cas, druzenja):
    mnozica_okuzenih = set([oseba])
    for person, date in druzenja[oseba]:
        if person != oseba and date > cas:
            mnozica_okuzenih |= okuzeni(person, date, druzenja)
    return mnozica_okuzenih

def identifikator(pozitivni, negativni, fragmenti):
    slovar_pozitivnih = Counter()
    slovar_negativnih = Counter()
    for fragment in fragmenti:
        for pozitiven in pozitivni:
            if fragment in pozitiven:
                slovar_pozitivnih[fragment] += 1


    for fragment in fragmenti:
        for negativen in negativni:
            if fragment in negativen:
                slovar_negativnih[fragment] += 1

    return max(fragmenti, key=lambda f: slovar_pozitivnih[f] - slovar_negativnih[f])

class Virus:
    def __init__(self, zacetna_mrna):
        self.zacetna_mrna = zacetna_mrna
        self.trentuna_mrna = zacetna_mrna

    def izbij(self, fragment):
        self.trentuna_mrna = self.trentuna_mrna.replace(fragment, "")

    def ostanek(self):
        return self.trentuna_mrna

    def mrtev(self):
        if not self.trentuna_mrna:
            return True
        return False

class Test(unittest.TestCase):
    def test_01_valovi(self):
        self.assertEqual([12, 5, 13], valovi([1, 5, 6, 0, 0, 0, 2, 3, 0, 5, 8, 0]))
        self.assertEqual([12, 5, 13], valovi([1, 5, 6, 0, 0, 0, 2, 3, 0, 5, 8]))
        self.assertEqual([12, 5, 13], valovi([0, 0, 1, 5, 6, 0, 0, 0, 2, 3, 0, 5, 8]))
        self.assertEqual([11, 11], valovi([0, 0, 5, 6, 0, 5, 6]))
        self.assertEqual([5, 11], valovi([0, 0, 5, 0, 5, 6]))
        self.assertEqual([5], valovi([0, 0, 5, 0,]))
        self.assertEqual([5], valovi([5, 0,]))
        self.assertEqual([5], valovi([5]))
        self.assertEqual([12], valovi([5, 3, 4]))

    def test_02_sledilnik(self):
        dnevi = [
            (["gledališča", "smučišča"], []),
            (["šole", "frizer", "muzeji"], ["smučišča"]),
            (["knjižnice"], ["muzeji", "smučišča"]),
            (["smučišča", "knjižnice", "gledališča"], ["šole"]),
            (["šole"], ["frizer", "smučišča"]),
            (["smučišča"], []),
            ([], []),
            ([], ["smučišča"])
        ]
        self.assertEqual(4, sledilnik(dnevi))

    def test_03_okuzeni(self):
        druzenja = {
            "Ana": [("Berta", 7), ("Cilka", 10), ("Dani", 4), ("Fanči", 3)],
            "Berta": [("Ana", 7), ("Cilka", 3)],
            "Cilka": [("Ana", 10), ("Berta", 3), ("Dani", 5)],
            "Dani": [("Ana", 4), ("Cilka", 5), ("Ema", 1), ("Fanči", 2)],
            "Ema": [("Dani", 1), ("Fanči", 8), ("Greta", 3)],
            "Fanči": [("Ana", 3), ("Dani", 2), ("Ema", 8), ("Greta", 2)],
            "Greta": [("Ema", 3), ("Fanči", 2)]
        }
        # Najprej samo test testa; ignoriraj
        for oseba1, d in druzenja.items():
            for oseba2, kdaj in d:
                self.assertIn((oseba1, kdaj), druzenja[oseba2])

        self.assertEqual({"Ana"}, okuzeni("Ana", 10, druzenja))
        self.assertEqual({"Ana", "Berta", "Cilka"}, okuzeni("Ana", 5, druzenja))
        self.assertEqual({"Ana", "Berta", "Cilka", "Dani"}, okuzeni("Ana", 3, druzenja))
        self.assertEqual({"Ana", "Berta", "Cilka", "Dani", "Ema", "Fanči"}, okuzeni("Ana", 2, druzenja))
        self.assertEqual({"Ana", "Berta", "Cilka", "Dani"}, okuzeni("Cilka", 1, druzenja))
        self.assertEqual({"Ana", "Cilka", "Dani"}, okuzeni("Cilka", 3, druzenja))
        self.assertEqual({"Ana", "Berta", "Cilka", "Dani", "Ema", "Fanči"}, okuzeni("Dani", 1, druzenja))
        self.assertEqual({"Ana", "Berta", "Cilka", "Dani", "Ema", "Fanči", "Greta"}, okuzeni("Ema", 0, druzenja))

    def test_04_identifikator(self):
        self.assertEqual(
            "GGU",
            identifikator(['GGGUGCCCCA', 'CCCAUAGGGU', 'CAGCUCGGUU'],
                          ['ACCUCAGGAG', 'UCGACCGAAG', 'GUCACUCGCA', 'CGCUUCCCGC', 'GGACCCCGCU'],
                          ["AUC", "GGU", "CAG", "CCC", "GGG", "UCA", "UGC"]))
        self.assertEqual(
            "GGU",
            identifikator(['GGGUGCCCCA', 'CCCAUAGGGU', 'CAGCUCGGUU'],
                          ['ACCUCAGGAG', 'UCGACCGAAG', 'GUCACUCGCA', 'CGCUUCCCGC'],
                          ["AUC", "GGU", "CAG", "CCC", "GGG", "UCA", "UGC"]))
        self.assertIn(
            identifikator(['GGGUGCCCCA', 'CCCAUAGGGU', 'CAGCUCGGUU'],
                          ['ACCUCAGGAG', 'UCGACCGAAG', 'GUCACUCGCA', 'CGCUUCCCGC'],
                          ["AUC", "CAG", "CCC", "UCA", "UGC"]),
            ("CCC", "UGC"))
        self.assertEqual(
            "GGG",
            identifikator(['GGGUGCCCCA', 'CCCAUAGGGU', 'CAGCUCGGUU'],
                          ['ACCUCAGGAG', 'UCGACCGAAG', 'GUCACUCGCA', 'CGCUUCCCGC', 'GGACCCCGCU'],
                          ["AUC", "CAG", "CCC", "GGG", "UCA", "UGC"]))
        self.assertEqual(
            "GGGGGG",
            identifikator(["UGGGGGGGA", "GGGGGGGGGGGGGGGG"],
                          ['ACCUCAGGAG', 'UCGACCGAAG', 'GGGGGGGGGGGG'],
                          ["GGGGGG", "AGG", "U"]))

    def test_05_virus(self):
        virus = Virus("ACCUTCCUUGUACUUTAA")
        self.assertFalse(virus.mrtev())
        self.assertIsNone(virus.izbij("CUU"))
        self.assertEqual("ACCUTCGUATAA", virus.ostanek())
        self.assertFalse(virus.mrtev())

        self.assertIsNone(virus.izbij("A"))
        self.assertEqual("CCUTCGUT", virus.ostanek())
        self.assertFalse(virus.mrtev())

        self.assertIsNone(virus.izbij("UT"))
        self.assertEqual("CCCG", virus.ostanek())
        self.assertFalse(virus.mrtev())

        self.assertIsNone(virus.izbij("CC"))
        self.assertEqual("CG", virus.ostanek())
        self.assertFalse(virus.mrtev())

        self.assertIsNone(virus.izbij("CG"))
        self.assertEqual("", virus.ostanek())
        self.assertTrue(virus.mrtev())

        virus = Virus("AAAAAAAAAAA")
        virus.izbij("AA")
        self.assertEqual("A", virus.ostanek())
        self.assertFalse(virus.mrtev())

        virus = Virus("AAAAAAAAAA")
        virus.izbij("AA")
        self.assertEqual("", virus.ostanek())
        self.assertTrue(virus.mrtev())


if __name__ == "__main__":
    unittest.main()
