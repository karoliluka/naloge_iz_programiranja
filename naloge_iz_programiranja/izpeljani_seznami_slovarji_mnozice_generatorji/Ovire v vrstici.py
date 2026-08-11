def vrstice(ovire):
    return [y for y, x0, x1 in ovire]

def ovirane_vrstice(ovire):
    return sorted(vrstice(ovire))

def ovirane_vrstice_uni(ovire):
    return list(set(ovirane_vrstice(ovire)))

def ovire_v_vrstici(ovire, vrstica):
    return set([(x0, x1) for y, x0, x1 in ovire if y == vrstica])

def stevilo_ovir(ovire, vrstica):
    return len(ovire_v_vrstici(ovire, vrstica))

def dolzina_ovir(ovire):
    return sum(x1 - x0 + 1 for y, x0, x1 in ovire)

def prosta_pot(ovire, stolpec):
    return all([x0 <= stolpec <= x1 for y, x0, x1 in ovire if y == stolpec])

def stevila_ovir(ovire):
    return {y : len(ovire_v_vrstici(ovire, y)) for y, x0, x1 in ovire}

def zacetki(ovire):
    return {y : min([x0 for y_2, x0, x1 in ovire if y == y_2]) for y, x0, x1 in ovire}

def ovire_po_vrsticah(ovire):
    return {y: set((x0, x1) for y_2, x0, x1 in ovire if y_2 == y) for y, x0, x1 in ovire}


import unittest
import ast

ovire1 = [(1, 3, 6), (1, 8, 10),
          (2, 1, 4),
          (3, 5, 8),
          (2, 7, 9),
          (7, 10, 10), (7, 12, 13),
          (5, 8, 10), (5, 1, 3),
          (2, 15, 19)]


class TestOneLineMixin:
    functions = {
        elm.name: elm
        for elm in ast.parse(open(__file__, "r", encoding="utf-8").read()).body
        if isinstance(elm, ast.FunctionDef)}

    def assert_is_one_line(self, func):
        body = self.functions[func.__code__.co_name].body
        self.assertEqual(len(body), 1, "\nFunkcija ni dolga le eno vrstico")
        self.assertIsInstance(body[0], ast.Return, "\nFunkcija naj bi vsebovala le return")

    def test_nedovoljene_funkcije(self):
        dovoljene_funkcije = {
            "vrstice", "ovirane_vrstice", "ovirane_vrstice_uni", "ovire_v_vrstici",
            "stevilo_ovir", "dolzina_ovir", "razpon", "prosta_pot",
            "stevila_ovir", "zacetki", "ovire_po_vrsticah"}
        for func in self.functions:
            self.assertIn(func, dovoljene_funkcije, f"\nFunkcija {func} ni dovoljena.")


class Test01Obvezna(unittest.TestCase, TestOneLineMixin):
    def test_01_vrstice(self):
        self.assertEqual([1, 1, 2, 3, 2, 7, 7, 5, 5, 2], vrstice(ovire1))
        self.assertEqual([], vrstice([]))
        self.assert_is_one_line(vrstice)

    def test_02_ovirane_vrstice(self):
        self.assertEqual([1, 1, 2, 2, 2, 3, 5, 5, 7, 7], ovirane_vrstice(ovire1))
        self.assertEqual([], ovirane_vrstice([]))
        self.assert_is_one_line(ovirane_vrstice)

    def test_03_ovirane_vrstice_uni(self):
        self.assertEqual([1, 2, 3, 5, 7], ovirane_vrstice_uni(ovire1))
        self.assertEqual([], ovirane_vrstice_uni([]))
        self.assert_is_one_line(ovirane_vrstice_uni)

    def test_04_ovire_v_vrstici(self):
        self.assertEqual({(3, 6), (8, 10)}, ovire_v_vrstici(ovire1, 1))
        self.assertEqual({(1, 4), (7, 9), (15, 19)}, ovire_v_vrstici(ovire1, 2))
        self.assertEqual(set(), ovire_v_vrstici(ovire1, 4))
        self.assert_is_one_line(ovire_v_vrstici)

    def test_05_stevilo_ovir(self):
        self.assertEqual(2, stevilo_ovir(ovire1, 1))
        self.assertEqual(3, stevilo_ovir(ovire1, 2))
        self.assertEqual(0, stevilo_ovir(ovire1, 4))
        self.assert_is_one_line(stevilo_ovir)

    def test_06_dolzina_ovir(self):
        self.assertEqual(32, dolzina_ovir(ovire1))
        self.assertEqual(0, dolzina_ovir([]))
        self.assert_is_one_line(dolzina_ovir)

    def test_07_prosta_pot(self):
        self.assertFalse(prosta_pot(ovire1, 1))
        self.assertFalse(prosta_pot(ovire1, 2))
        self.assertTrue(prosta_pot(ovire1, 14))
        self.assertTrue(prosta_pot(ovire1, 20))
        self.assert_is_one_line(prosta_pot)


class Test02Dodatna(unittest.TestCase, TestOneLineMixin):
    def test_01_stevila_ovir(self):
        self.assertEqual({1: 2, 2: 3, 3: 1, 5: 2, 7: 2}, stevila_ovir(ovire1))
        self.assertEqual({}, stevila_ovir([]))
        self.assert_is_one_line(stevila_ovir)

    def test_02_zacetki(self):
        self.assertEqual({1: 3, 2: 1, 3: 5, 5: 1, 7: 10}, zacetki(ovire1))
        self.assertEqual({}, zacetki([]))
        self.assert_is_one_line(zacetki)

    def test_03_ovire_po_vrsticah(self):
        self.assertEqual({
            1: {(3, 6), (8, 10)},
            2: {(1, 4), (7, 9), (15, 19)},
            3: {(5, 8)},
            5: {(1, 3), (8, 10)},
            7: {(10, 10), (12, 13)}}, ovire_po_vrsticah(ovire1))
        self.assertEqual({}, ovire_po_vrsticah([]))
        self.assert_is_one_line(ovire_po_vrsticah)


if __name__ == "__main__":
    unittest.main()
