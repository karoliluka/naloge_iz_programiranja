import unittest
from collections import defaultdict


def koordinate(s):
    x1 = ""
    for char in s:
        if char.isnumeric():
            x1 += char
    return int(x1), int(x1) + s.count("-") - 1

def vrstica(s):
    seznam = []
    s = s.split()
    y = ""
    for char in s[0]:
        if char.isnumeric():
            y += char

    for ovira in s[1:]:
        x1, x2 = koordinate(ovira)
        seznam.append((x1, x2, int(y)))

    return seznam

def preberi(s):
    seznam = []
    s = s.splitlines()
    for vrsta in s:
        seznam.extend(vrstica(vrsta))
    return seznam

def intervali(xs):
    seznam = []
    for x1, x2 in xs:
        niz = str(x1)
        niz += ("-" * (x2 - x1 + 1))
        seznam.append(niz)
    return seznam

def zapisi_vrstico(y, xs):
    niz = "(" + str(y) + ")"
    for x, y in xs:
        niz += vrstica(xs)
    print(niz)

def zapisi_vrstico(y, xs):
    niz = "(" + str(y) + ") "
    seznam = intervali(xs)
    nove_ovire = []
    for i, ovira in enumerate(seznam):
        if i == len(seznam) - 1:
            break
        else:
            nove_ovire.append(ovira + " ")

    for ovira in nove_ovire:
        niz += ovira
    niz += seznam[-1]
    return niz

def zapisi(ovire):
    slovar = defaultdict(list) #kljuc bo vrstica, vrednosti pa pari na vrstici
    for x0, x1, y in ovire:
        par = (x0, x1)
        slovar[y] += par

    niz = ""
    for vrsta, pari in sorted(slovar.items()):
        pairs = []
        for x0, x1 in zip(pari[::2], pari[1::2]):
            pairs.append((x0, x1))
        niz += zapisi_vrstico(vrsta, sorted(pairs))
        niz += "\n"
    return niz






class Obvezna(unittest.TestCase):
    def test_koordinate(self):
        self.assertEqual((3, 4), koordinate("3--"))
        self.assertEqual((5, 10), koordinate("5------"))
        self.assertEqual((123, 123), koordinate("123-"))
        self.assertEqual((123, 125), koordinate("123---"))

    def test_vrstica(self):
        self.assertEqual([(1, 3, 4), (5, 11, 4), (15, 15, 4)], vrstica("  (4) 1---  5------- 15-"))
        self.assertEqual([(989, 991, 1234)], vrstica("(1234) 989---"))

    def test_preberi(self):
        self.assertEqual([(5, 6, 4),
                          (90, 100, 13), (5, 8, 13), (19, 21, 13),
                          (9, 11, 5), (19, 20, 5), (30, 34, 5),
                          (9, 11, 4),
                          (22, 25, 13), (17, 19, 13)], preberi(
""" (4) 5--
(13) 90-----------   5---- 19---
 (5) 9---           19--   30-----
(4)           9---
(13)         22---- 17---
"""))

    def test_intervali(self):
        self.assertEqual(["6-----", "12-", "20---", "98-----"], intervali([(6, 10), (12, 12), (20, 22), (98, 102)]))

    def test_zapisi_vrstico(self):
        self.assertEqual("(5) 6----- 12-", zapisi_vrstico(5, [(6, 10), (12, 12)]).rstrip("\n"))
        self.assertEqual("(8) 6----- 12- 20--- 98-----", zapisi_vrstico(8, [(6, 10), (12, 12), (20, 22), (98, 102)]).rstrip("\n"))
        self.assertEqual("(8) 6----- 12- 20--- 98-----", zapisi_vrstico(8, [(6, 10), (12, 12), (20, 22), (98, 102)]).rstrip("\n"))


class Dodatna(unittest.TestCase):
    def test_zapisi(self):
        ovire = [(5, 6, 4),
          (90, 100, 13), (5, 8, 13), (9, 11, 13),
          (9, 11, 5), (19, 20, 5), (30, 34, 5),
          (9, 11, 4),
          (22, 25, 13), (17, 19, 13)]
        kopija_ovir = ovire.copy()
        self.assertEqual("""(4) 5-- 9---
(5) 9--- 19-- 30-----
(13) 5---- 9--- 17--- 22---- 90-----------""", zapisi(ovire).rstrip("\n"))
        self.assertEqual(ovire, kopija_ovir, "Pusti seznam `ovire` pri miru")


if __name__ == "__main__":
    unittest.main()