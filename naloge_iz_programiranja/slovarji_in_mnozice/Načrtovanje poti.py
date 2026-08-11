
A, B, C, D, E, F, G, H, I, J, K, L, M, N, O, P, R, S, T, U, V = "ABCDEFGHIJKLMNOPRSTUV"

zemljevid = {
    ('A', 'B'): {'trava', 'gravel'},
    ('A', 'V'): {'lonci', 'pešci'},
    ('B', 'A'): {'trava', 'gravel'},
    ('B', 'C'): {'lonci', 'bolt'},
    ('B', 'V'): set(),
    ('C', 'B'): {'lonci', 'bolt'},
    ('C', 'R'): {'lonci', 'pešci', 'stopnice'},
    ('D', 'F'): {'pešci', 'stopnice'},
    ('D', 'R'): {'pešci'},
    ('E', 'I'): {'trava', 'lonci'},
    ('F', 'D'): {'pešci', 'stopnice'},
    ('F', 'G'): {'trava', 'črepinje'},
    ('G', 'F'): {'trava', 'črepinje'},
    ('G', 'H'): {'črepinje', 'pešci'},
    ('G', 'I'): {'avtocesta'},
    ('H', 'G'): {'črepinje', 'pešci'},
    ('H', 'J'): {'bolt', 'robnik'},
    ('I', 'E'): {'trava', 'lonci'},
    ('I', 'G'): {'avtocesta'},
    ('I', 'M'): {'avtocesta'},
    ('I', 'P'): {'gravel'},
    ('I', 'R'): {'stopnice', 'robnik'},
    ('J', 'H'): {'bolt', 'robnik'},
    ('J', 'K'): set(),
    ('J', 'L'): {'bolt', 'gravel'},
    ('K', 'J'): set(),
    ('K', 'M'): {'bolt', 'stopnice'},
    ('L', 'J'): {'bolt', 'gravel'},
    ('L', 'M'): {'pešci', 'robnik'},
    ('M', 'I'): {'avtocesta'},
    ('M', 'K'): {'bolt', 'stopnice'},
    ('M', 'L'): {'pešci', 'robnik'},
    ('M', 'N'): {'rodeo'},
    ('N', 'M'): {'rodeo'},
    ('N', 'P'): {'gravel'},
    ('O', 'P'): {'gravel'},
    ('P', 'I'): {'gravel'},
    ('P', 'N'): {'gravel'},
    ('P', 'O'): {'gravel'},
    ('P', 'S'): set(),
    ('R', 'C'): {'lonci', 'pešci', 'stopnice'},
    ('R', 'D'): {'pešci'},
    ('R', 'I'): {'stopnice', 'robnik'},
    ('R', 'U'): {'trava', 'pešci'},
    ('R', 'V'): {'lonci', 'pešci'},
    ('S', 'P'): set(),
    ('S', 'T'): {'trava', 'robnik'},
    ('T', 'S'): {'trava', 'robnik'},
    ('T', 'U'): {'trava', 'gravel'},
    ('U', 'R'): {'trava', 'pešci'},
    ('U', 'T'): {'trava', 'gravel'},
    ('U', 'V'): {'lonci', 'trava', 'robnik'},
    ('V', 'A'): {'lonci', 'pešci'},
    ('V', 'B'): set(),
    ('V', 'R'): {'lonci', 'pešci'},
    ('V', 'U'): {'lonci', 'trava', 'robnik'}}

mali_zemljevid = {
    (A, B): {"robnik", "bolt"},
    (B, A): {"robnik", "bolt"},
    (A, C): {"bolt", "rodeo", "pešci"},
    (C, A): {"bolt", "rodeo", "pešci"},
    (C, D): set(),
    (D, C): set()}

def mozna_pot(pot, zemljevid):
    pari = []
    for k1, k2 in zip(pot, pot[1:]):
        pari.append((k1, k2))

    for par in pari:
        if par not in zemljevid:
            return False
    return True


def potrebne_vescine(pot, zemljevid):
    pari = []
    for k1, k2 in zip(pot, pot[1:]):
        pari.append((k1, k2))

    potrebne = set()
    for par in pari:
        for vescina in zemljevid[par]:
            potrebne.add(vescina)

    return potrebne

def nepotrebne_vescine(pot, zemljevid, vescine):
    potrebne = potrebne_vescine(pot, zemljevid)
    return set(vescine) - potrebne

def kam(zemljevid, tocka, vescine):
    potencialne = []
    for start, cilj in zemljevid:
        if start == tocka:
            potencialne.append((tocka, cilj))

    mozne_tocke = set()
    for par in potencialne:
        if vescine >= set(zemljevid[par]):
            mozne_tocke.add(par[1])
    return mozne_tocke


def dolgcas(zemljevid):
    mnozica_frozensetov = set()
    for par in zemljevid:
        if not zemljevid[par]:
            mnozica_frozensetov.add(frozenset(par))

    mnozica = set()
    for par in mnozica_frozensetov:
        mnozica.add(tuple(par))

    return mnozica

def koncna_tocka(pot, zemljevid, vescine):
    for par in zip(pot, pot[1:]):
        trenutna_tocka = par[0]
        if vescine >= zemljevid[par]:
            continue
        else:
            return trenutna_tocka, zemljevid[par] - vescine
    return None

import unittest
import ast


class TestObvezna(unittest.TestCase):
    def test_1_mozna_pot(self):
        self.assertTrue(mozna_pot("ACD", mali_zemljevid))
        self.assertTrue(mozna_pot("ABACD", mali_zemljevid))
        self.assertTrue(mozna_pot("AB", mali_zemljevid))
        self.assertFalse(mozna_pot("ABD", mali_zemljevid))

        self.assertTrue(mozna_pot("ABCRVRIEIPNM", zemljevid))
        self.assertTrue(mozna_pot("HJKMLJH", zemljevid))
        self.assertFalse(mozna_pot("AC", zemljevid))
        self.assertFalse(mozna_pot("ABCRVRIEPNM", zemljevid))
        self.assertTrue(mozna_pot("A", zemljevid))

    def test_2_potrebne_vescine(self):
        self.assertEqual({'pešci', 'bolt', 'rodeo'},
                         potrebne_vescine("AC", mali_zemljevid))

        self.assertEqual({'pešci', 'bolt', 'rodeo'},
                         potrebne_vescine("ACD", mali_zemljevid))

        self.assertEqual({'pešci', 'robnik', 'bolt', 'rodeo'},
                         potrebne_vescine("ABACD", mali_zemljevid))

        self.assertEqual({'robnik', 'stopnice', 'gravel', 'trava'},
                          potrebne_vescine("RIPSTUT", zemljevid))

        self.assertEqual({'pešci', 'trava', 'lonci', 'bolt', 'stopnice', 'gravel'},
                         potrebne_vescine("ABCRVR", zemljevid))

        self.assertEqual({'pešci', 'trava', 'robnik', 'lonci', 'bolt', 'stopnice', 'rodeo', 'gravel'},
                         potrebne_vescine("ABCRVRIEIPNM", zemljevid))

        self.assertEqual({'pešci', 'robnik', 'bolt', 'stopnice', 'gravel'},
                         potrebne_vescine("HJKMLJH", zemljevid))

        self.assertEqual(set(), potrebne_vescine("BVBVBVB", zemljevid))

    def test_3_nepotrebne_vescine(self):
        vescine = {'pešci', 'robnik', 'stopnice', 'gravel', 'bolt', 'rodeo'}
        kopija = vescine.copy()
        self.assertEqual({'stopnice', 'gravel'},
                         nepotrebne_vescine("ABACD", mali_zemljevid, vescine))
        self.assertEqual(vescine, kopija, "Se mi prav zdi, da je funkcija nepotrebne_vescine spremenila "
                                          "vrednost svojega argumenta `vescine`? Fail, fail!")

        vescine = {'stopnice', 'gravel', 'bolt', 'rodeo'}
        self.assertEqual({'stopnice', 'bolt'},
                         nepotrebne_vescine("IPNMNPO", zemljevid, vescine))

        vescine = {'gravel', 'rodeo'}
        self.assertEqual(set(), nepotrebne_vescine("IPNMNPO", zemljevid, vescine))

    def test_4_kam(self):
        self.assertEqual({U, I, D}, kam(zemljevid, R, {"stopnice", "trava", "pešci", "robnik", "avtocesta"}))
        self.assertEqual({U, I, D, V, C}, kam(zemljevid, R, {"stopnice", "trava", "pešci", "robnik", "lonci", "avtocesta"}))
        self.assertEqual({D, V, C}, kam(zemljevid, R, {"stopnice", "pešci", "lonci", "avtocesta"}))

        self.assertEqual({S}, kam(zemljevid, P, {"stopnice", "pešci", "lonci", "avtocesta"}))
        self.assertEqual({S}, kam(zemljevid, P, set()))
        self.assertEqual({S, O, I, N}, kam(zemljevid, P, {"gravel", "stopnice", "pešci", "lonci", "avtocesta"}))
        self.assertEqual({S, O, I, N}, kam(zemljevid, P, {"gravel"}))

        self.assertEqual({P}, kam(zemljevid, I, {"gravel"}))
        self.assertEqual({P}, kam(zemljevid, I, {"gravel", "lonci"}))
        self.assertEqual({P, G, M}, kam(zemljevid, I, {"gravel", "lonci", "avtocesta"}))

        self.assertEqual({P, G, M}, kam(zemljevid, I, {"gravel", "lonci", "avtocesta"}))
        self.assertEqual(set(), kam(zemljevid, I, set()))

    def test_5_dolgcas(self):
        dolgocasne = dolgcas(zemljevid)
        self.assertEqual(3, len(dolgocasne))
        for od, do in {(B, V), (S, P), (J, K)}:
            self.assertTrue(
                ((od, do) in dolgocasne) != ((do, od) in dolgocasne),
                f"manjka povezava med {od} in {do}")

        dolgocasne = dolgcas(mali_zemljevid)
        self.assertIn(dolgocasne, ({(C, D)}, {(D, C)}))

class TestDodatna(unittest.TestCase):
    def test_1_koncna_tocka(self):
        vescine = {'pešci', 'robnik', 'bolt', 'stopnice', 'gravel'}
        self.assertEqual(("H", {'črepinje'}), koncna_tocka("HJKMLJHGFD", zemljevid, vescine))
        self.assertEqual(("M", {'rodeo'}), koncna_tocka("HJKMNPIG", zemljevid, vescine))
        self.assertEqual(("B", {'lonci', 'bolt'}), koncna_tocka("ABCRVB", zemljevid, {"gravel", "trava"}))


if "__main__" == __name__:
    unittest.main()
