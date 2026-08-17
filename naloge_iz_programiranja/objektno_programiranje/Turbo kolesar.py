class Kolesar:
    def __init__(self):
        self.x = 0
        self.y = 0
        self.prevozena_razdalja = 0
        self.turbo = False
        self.turbo_stevec = 0

    def premik(self, smer):
        if self.turbo:
            multiplier = 2
        else:
            multiplier = 1

        if smer == "<":
            self.x -= 1 * multiplier
            self.prevozena_razdalja += 1 * multiplier
        elif smer == ">":
            self.x += 1 * multiplier
            self.prevozena_razdalja += 1 * multiplier
        elif smer == "^":
            self.y -= 1 * multiplier
            self.prevozena_razdalja += 1 * multiplier
        else:
            self.y += 1 * multiplier
            self.prevozena_razdalja += 1 * multiplier

        if self.turbo:
            self.turbo_stevec -= 1
            if self.turbo_stevec == 0:
                self.turbo = False

    def lokacija(self):
        return self.x, self.y

    def prevozi(self, pot):
        for char, smer in zip(pot[::2], pot[1::2]):
            for i in range(int(char)):
                self.premik(smer)

    def razdalja(self):
        return self.prevozena_razdalja

    def vkljuci_turbo(self):
        self.turbo = True

    def vkljuci_turbo(self):
        if not self.turbo:
            self.turbo = True
            self.turbo_stevec = 5

    def izkljuci_turbo(self):
        self.turbo = False

import unittest

class TestKolesar(unittest.TestCase):
    def test_1_premik(self):
        ana = Kolesar()
        berta = Kolesar()

        self.assertEqual((0, 0), ana.lokacija())
        ana.premik("^")
        self.assertEqual((0, -1), ana.lokacija())
        ana.premik("^")
        self.assertEqual((0, -2), ana.lokacija())
        ana.premik("<")
        self.assertEqual((-1, -2), ana.lokacija())
        ana.premik("v")
        self.assertEqual((-1, -1), ana.lokacija())
        ana.premik(">")
        self.assertEqual((0, -1), ana.lokacija())

        self.assertEqual((0, 0), berta.lokacija())
        berta.premik("<")
        self.assertEqual((-1, 0), berta.lokacija())

    def test_2_prevozi(self):
        ana = Kolesar()

        ana.prevozi("2>5^2>8v2<")
        self.assertEqual((2, 3), ana.lokacija())
        ana.premik("v")
        self.assertEqual((2, 4), ana.lokacija())
        ana.prevozi("4>")
        self.assertEqual((6, 4), ana.lokacija())

    def test_3_razdalja(self):
        ana = Kolesar()

        self.assertEqual((0, 0), ana.lokacija())
        self.assertEqual(0, ana.razdalja())
        ana.premik("^")
        self.assertEqual((0, -1), ana.lokacija())
        self.assertEqual(1, ana.razdalja())
        ana.premik("v")
        self.assertEqual((0, 0), ana.lokacija())
        self.assertEqual(2, ana.razdalja())
        ana.prevozi("2>5^2>8v2<")
        self.assertEqual((2, 3), ana.lokacija())
        self.assertEqual(21, ana.razdalja())
        ana.premik("v")
        self.assertEqual((2, 4), ana.lokacija())
        self.assertEqual(22, ana.razdalja())
        ana.prevozi("4>")
        self.assertEqual((6, 4), ana.lokacija())
        self.assertEqual(26, ana.razdalja())

    def test_4_turbo(self):
        ana = Kolesar()

        self.assertEqual((0, 0), ana.lokacija())
        self.assertEqual(0, ana.razdalja())
        ana.premik("^")
        self.assertEqual((0, -1), ana.lokacija())
        self.assertEqual(1, ana.razdalja())
        ana.vkljuci_turbo()
        ana.premik("v")
        self.assertEqual((0, 1), ana.lokacija())
        self.assertEqual(3, ana.razdalja())
        ana.premik(">")
        self.assertEqual((2, 1), ana.lokacija())
        self.assertEqual(5, ana.razdalja())
        ana.premik("v")
        self.assertEqual((2, 3), ana.lokacija())
        self.assertEqual(7, ana.razdalja())
        ana.izkljuci_turbo()
        ana.premik("v")
        self.assertEqual((2, 4), ana.lokacija())
        self.assertEqual(8, ana.razdalja())
        ana.vkljuci_turbo()
        ana.prevozi("2>1^")
        self.assertEqual((6, 2), ana.lokacija())
        self.assertEqual(14, ana.razdalja())

    def test_5_varni_turbo(self):
        ana = Kolesar()
        berta = Kolesar()

        ana.vkljuci_turbo()
        ana.premik(">")
        ana.premik(">")
        ana.premik(">")
        ana.premik(">")
        self.assertEqual((8, 0), ana.lokacija())
        self.assertEqual(8, ana.razdalja())
        ana.premik(">")
        self.assertEqual((10, 0), ana.lokacija())
        self.assertEqual(10, ana.razdalja())

        berta.vkljuci_turbo()
        berta.premik(">")
        # Drugi klic turbo nima učinka - še vedno odštevamo
        berta.vkljuci_turbo()
        for _ in range(5):
            berta.premik(">")
        self.assertEqual((11, 0), berta.lokacija())

        # Turbo se sam izključi
        ana.premik(">")
        self.assertEqual((11, 0), ana.lokacija())
        self.assertEqual(11, ana.razdalja())

        # Turbo se bo izključil po petih premikih
        ana.vkljuci_turbo()
        ana.prevozi("3>6v")
        self.assertEqual((17, 8), ana.lokacija())
        self.assertEqual(25, ana.razdalja())
        # In je zdaj izključen
        ana.premik(">")
        self.assertEqual((18, 8), ana.lokacija())
        self.assertEqual(26, ana.razdalja())

if __name__ == "__main__":
    unittest.main()
