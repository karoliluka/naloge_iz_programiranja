#Največji
from os import makedirs
def naj(xs):
    return max(xs)

print(naj([5, 1, -6, -7, 2]))

#Največji absolutist
def naj_abs(xs):
    naj = 0
    for x in xs:
        if abs(x) > abs(naj):
            naj = x
    return naj

#Oštevilči
def ostevilci(xs):
    seznam = []
    for i, x in enumerate(xs):
        seznam.append((i, x))
    return seznam

#Indeks telesne teže
osebe = [('Ana', 55, 165), ('Berta', 60, 153)]
def bmi(osebe):
    seznam = []
    for ime, teza, visina in osebe:
        seznam.append((ime, teza / (visina / 100)**2))
    return seznam

#Indeks telesne teže 2
imena = ['Ana', 'Berta']
teze = [55, 60]
visine = [165, 153]
def bmi2(imena, teze, visine):
    seznam = []
    for ime, teza, visina in zip(imena, teze, visine):
        seznam.append((ime, teza / (visina / 100)**2))
    return seznam

#Praštevila
def je_prastevilo(n):
    if n < 2:
        return False

    for i in range(2, n):
        if n % i == 0:
            return False
    return True

def prastevila(n):
    stevec = 0
    for i in range(n):
        if je_prastevilo(i):
            stevec += 1

    return stevec

#Palindrom
def palindrom(s):
    return s == s[::-1]

def palindrom(s):
    return s == "".join(reversed(s))

#Palindromska števila
def palindromska_stevila():
    palindromi = []
    for i in range(100, 1000):
        for j in range(100, 1000):
            if palindrom(str(i * j)):
                palindromi.append(i * j)
    return max(palindromi)

#Inverzije
def inverzije(xs):
    stevec = 0
    for x in xs:
        for y in xs:
            if y == x:
                break
            if y > x:
                stevec += 1
    return stevec

### ^^^ Naloge rešujte nad tem komentarjem. ^^^ ###

import unittest


class TestVaje(unittest.TestCase):
    def test_naj(self):
        self.assertEqual(naj([1]), 1)
        self.assertEqual(naj([-1]), -1)
        self.assertEqual(naj([5, 1, -6, -7, 2]), 5)
        self.assertEqual(naj([1, -6, -7, 2, 5]), 5)
        self.assertEqual(naj([-5, -1, -6, -7, -2]), -1)
        self.assertEqual(naj([1, 2, 5, 6, 10, 2, 3, 4, 9, 9]), 10)
        self.assertEqual(naj([-10 ** 10, -10 ** 9]), -10 ** 9)

    def test_naj_abs(self):
        self.assertEqual(naj_abs([1]), 1)
        self.assertEqual(naj_abs([-1]), -1)
        self.assertEqual(naj_abs([10, 12, 9]), 12)
        self.assertEqual(naj_abs([0, 0, 0, 0, 0]), 0)
        self.assertEqual(naj_abs([5, 1, -6, -7, 2]), -7)
        self.assertEqual(naj_abs([1, -6, 5, 2, -7]), -7)
        self.assertEqual(naj_abs([-5, -1, -6, -7, -2]), -7)
        self.assertEqual(naj_abs([100, 1, 5, 3, -90, 3]), 100)
        self.assertEqual(naj_abs([-100, 1, 5, 3, -90, 3]), -100)
        self.assertEqual(naj_abs([-10 ** 10, -10 ** 9]), -10 ** 10)
        self.assertEqual(naj_abs([1, 2, 5, 6, 10, 2, 3, 4, 9, 9]), 10)
        self.assertEqual(naj_abs([1, 2, 5, 6, -10, 2, 3, 4, 9, 9]), -10)

    def test_ostevilci(self):
        self.assertEqual(ostevilci([]), [])
        self.assertEqual(ostevilci([1]), [(0, 1)])
        self.assertEqual(ostevilci([5, 1, 4, 2, 3]), [(0, 5), (1, 1), (2, 4), (3, 2), (4, 3)])

    def test_bmi(self):
        in_out = [
            ([], []),
            ([('Ana', 55, 165), ('Berta', 60, 153)],
             [('Ana', 20.202020202020204), ('Berta', 25.63116749967961)]),
            ([('Ana', 55, 165), ('Berta', 60, 153), ('Cilka', 70, 183)],
             [('Ana', 20.202020202020204), ('Berta', 25.63116749967961), ('Cilka', 20.902385858042937)]),
        ]
        for i, o in in_out:
            for (nu, bu), (n, b) in zip(bmi(i), o):
                self.assertEqual(nu, n)
                self.assertAlmostEqual(bu, b)

    def test_bmi2(self):
        in_out = [
            (([], [], []), []),
            ((['Ana', 'Berta'], [55, 60], [165, 153]),
             [('Ana', 20.202020202020204), ('Berta', 25.63116749967961)]),
            ((['Ana', 'Berta', 'Cilka'], [55, 60, 70], [165, 153, 183]),
             [('Ana', 20.202020202020204), ('Berta', 25.63116749967961), ('Cilka', 20.902385858042937)]),
        ]
        for i, o in in_out:
            for (nu, bu), (n, b) in zip(bmi2(*i), o):
                self.assertEqual(nu, n)
                self.assertAlmostEqual(bu, b)

    def test_prastevila(self):
        self.assertEqual(prastevila(10), 4)
        self.assertEqual(prastevila(11), 4)
        self.assertEqual(prastevila(12), 5)
        self.assertEqual(prastevila(50), 15)
        self.assertEqual(prastevila(100), 25)
        self.assertEqual(prastevila(1000), 168)

    #    def test_prastevila_hard(self):
    #        self.assertEqual(prastevila(10**6), 78498)
    #        self.assertEqual(prastevila(10**7), 664579)

    def test_palindrom(self):
        self.assertEqual(palindrom(''), True)
        self.assertEqual(palindrom('a'), True)
        self.assertEqual(palindrom('aa'), True)
        self.assertEqual(palindrom('ab'), False)
        self.assertEqual(palindrom('aba'), True)
        self.assertEqual(palindrom('abc'), False)
        self.assertEqual(palindrom('abcdefedcba'), True)
        self.assertEqual(palindrom('abcdefgedcba'), False)
        self.assertEqual(palindrom('pericarezeracirep'), True)
        self.assertEqual(palindrom('perica'), False)

    def test_palindromska_stevila(self):
        self.assertEqual(palindromska_stevila(), 906609)

    def test_inverzije(self):
        self.assertEqual(inverzije([]), 0)
        self.assertEqual(inverzije([1]), 0)
        self.assertEqual(inverzije([1, 2]), 0)
        self.assertEqual(inverzije([2, 1]), 1)
        self.assertEqual(inverzije([3, 2, 1]), 3)
        self.assertEqual(inverzije([4, 3, 2, 1]), 6)
        self.assertEqual(inverzije([5, 4, 3, 2, 1]), 10)
        self.assertEqual(inverzije([1, 4, 3, 5, 2]), 4)
        self.assertEqual(inverzije([10, 3, 9, 2, 22, 42, 0, 88, 66]), 12)


if __name__ == '__main__':
    unittest.main(verbosity=2)
