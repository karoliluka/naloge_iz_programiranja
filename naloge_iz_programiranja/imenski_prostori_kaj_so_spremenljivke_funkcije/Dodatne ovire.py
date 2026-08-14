def sovpad(ovira1, ovira2):
    return ovira2[0] <= ovira1[0] <= ovira2[1] or ovira1[0] <= ovira2[0] <= ovira1[1]

def odstrani_odvecne(obstojece, dodatne):
    ostanejo = []
    for ovira_o in obstojece:
        prekriva_se = False
        for ovira_d in dodatne:
            if sovpad(ovira_o, ovira_d):
                prekriva_se = True
        if not prekriva_se:
            ostanejo.append(ovira_o)
    obstojece[:] = ostanejo

def pretvori_vrstico(vrstica):
    if vrstica and vrstica[-1] == "#":
        vrstica += "."
    seznam_parov = []
    v_oviri = False
    for i, char in enumerate(vrstica, start=1):
        if char == "#" and v_oviri is False:
            start = i
            v_oviri = True
        elif char == "." and v_oviri is True:
            konec = i
            seznam_parov.append((start, konec - 1))
            v_oviri = False
    return seznam_parov

def zlite_ovire(obstojece, dodatne):
    kopija = obstojece[:]
    odstrani_odvecne(kopija, dodatne)
    dolzina = max([ovira[1] for ovira in kopija + dodatne])
    niz = "." * dolzina
    for x0, x1 in kopija + dodatne:
        niz = niz[:x0 - 1] + "#" * (x1 - x0 + 1) + niz[x1:]
    return pretvori_vrstico(niz)

def zlij_ovire(obstojece, dodatne):
    ostanejo = []
    for o in obstojece:
        prekriva = False
        for d in dodatne:
            if sovpad(o, d):
                prekriva = True
                break
        if not prekriva:
            ostanejo.append(o)

    i, j = 0, 0
    vse = []
    while i < len(ostanejo) and j < len(dodatne):
        if ostanejo[i][0] <= dodatne[j][0]:
            vse.append(ostanejo[i])
            i += 1
        else:
            vse.append(dodatne[j])
            j += 1
    vse.extend(ostanejo[i:])
    vse.extend(dodatne[j:])

    zdruzeno = []
    for x0, x1 in vse:
        if zdruzeno and x0 <= zdruzeno[-1][1] + 1:
            prej_x0, prej_x1 = zdruzeno[-1]
            zdruzeno[-1] = (prej_x0, max(prej_x1, x1))
        else:
            zdruzeno.append((x0, x1))

    obstojece[:] = zdruzeno





import unittest

class Test01Obvezna(unittest.TestCase):
    def test_01_odstrani_odvecne(self):
        obst = [(2, 5), (10, 15)]
        o = obst.copy()
        self.assertIsNone(odstrani_odvecne(o, []), "Funkcija ne sme vračati ničesar!")
        self.assertEqual(o, obst)

        odstrani_odvecne(o, [(0, 1), (6, 9), (16, 20)])
        self.assertEqual(o, obst)

        odstrani_odvecne(o, [(0, 2)])
        self.assertEqual([(10, 15)], o)

        o = obst.copy()
        odstrani_odvecne(o, [(3, 4)])
        self.assertEqual([(10, 15)], o)

        o = obst.copy()
        odstrani_odvecne(o, [(3, 7)])
        self.assertEqual([(10, 15)], o)

        o = obst.copy()
        odstrani_odvecne(o, [(3, 12)])
        self.assertEqual([], o)

        o = obst.copy()
        odstrani_odvecne(o, [(12, 18)])
        self.assertEqual([(2, 5)], o)

        obst = []
        odstrani_odvecne(obst, [(2, 5)])
        self.assertEqual([], obst)

        odstrani_odvecne(obst, [])
        self.assertEqual([], obst)

        obstojece = [(3, 5), (9, 10), (13, 15), (19, 24), (26, 27), (33, 35), (37, 38), (45, 47), (49, 50), (53, 55),
                     (60, 60), (62, 62), (64, 66), (69, 69), (71, 71), (73, 73), (76, 77)]
        nove = [(7, 9), (15, 16), (20, 20), (24, 25), (30, 33), (36, 36), (41, 42), (48, 48), (59, 65), (69, 72),
                (79, 81)]
        odstrani_odvecne(obstojece, nove)
        self.assertEqual([(3, 5), (26, 27), (37, 38), (45, 47), (49, 50), (53, 55), (73, 73), (76, 77)],
                         obstojece)

    def test_02_zlite_ovire(self):
        def ns():
            self.assertEqual(obstojece, o, "Je bila funkcija poredna? Je spreminjala seznam `obstojece`?")
            self.assertEqual(nove, n, "Je bila funkcija poredna? Je spreminjala seznam `nove`?")

        obstojece = [(2, 5), (10, 15)]
        o = obstojece.copy()
        nove = [(7, 8)]
        n = nove.copy()
        self.assertEqual([(2, 5), (7, 8), (10, 15)], zlite_ovire(obstojece, nove))
        ns()

        nove = [(6, 8)]
        n = nove.copy()
        self.assertEqual([(2, 8), (10, 15)], zlite_ovire(obstojece, nove))
        ns()

        nove = [(5, 8)]
        n = nove.copy()
        self.assertEqual([(5, 8), (10, 15)], zlite_ovire(obstojece, nove))
        ns()

        nove = [(5, 11)]
        n = nove.copy()
        self.assertEqual([(5, 11)], zlite_ovire(obstojece, nove))
        ns()

        nove = [(6, 9)]
        n = nove.copy()
        self.assertEqual([(2, 15)], zlite_ovire(obstojece, nove))
        ns()

        self.assertEqual(obstojece, zlite_ovire(obstojece, []))

        self.assertEqual([(1, 2), (5, 8), (10, 12)], zlite_ovire([(5, 8)], [(1, 2), (10, 12)]))

        self.assertEqual([(2, 15)], zlite_ovire([(2, 5), (7, 8), (10, 15)], [(6, 9)]))

        obstojece = [(3, 5), (9, 10), (13, 15), (19, 24), (26, 27), (33, 35), (37, 38), (45, 47), (49, 50), (53, 55),
                     (60, 60), (62, 62), (64, 66), (69, 69), (71, 71), (73, 73), (76, 77)]
        nove = [(7, 9), (15, 16), (20, 20), (24, 25), (30, 33), (36, 36), (41, 42), (48, 48), (59, 65), (69, 72),
                (79, 81)]
        self.assertEqual(
            [(3, 5), (7, 9), (15, 16), (20, 20), (24, 27), (30, 33), (36, 38), (41, 42), (45, 50), (53, 55), (59, 65),
             (69, 73), (76, 77), (79, 81)], zlite_ovire(obstojece, nove)
        )

class Test02Dodatna(unittest.TestCase):
    def test_02_zlite_ovire(self):
        f = 10000000000000000000000

        def preveri(obstojece, nove, rezultat):
            o = obstojece.copy()
            n = nove.copy()

            zlij_ovire(o, n)
            self.assertEqual(rezultat, o)
            self.assertEqual(nove, n, "Je bila funkcija poredna? Je spreminjala seznam `nove`?")

            def krat(s):
                return [(x0 * f, x1 * f + f - 1) for x0, x1 in s]

            o, n, rezultat = map(krat, (obstojece, nove, rezultat))
            zlij_ovire(o, n)
            self.assertEqual(rezultat, o)

        obstojece = [(2, 5), (10, 15)]
        preveri(obstojece, [(7, 8)], [(2, 5), (7, 8), (10, 15)])
        preveri(obstojece, [(6, 8)], [(2, 8), (10, 15)])
        preveri(obstojece, [(5, 8)], [(5, 8), (10, 15)])
        preveri(obstojece, [(5, 11)], [(5, 11)])
        preveri(obstojece, [(6, 9)], [(2, 15)])
        preveri(obstojece, [], [(2, 5), (10, 15)])
        preveri([(5, 8)], [(1, 2), (10, 12)], [(1, 2), (5, 8), (10, 12)])
        preveri([(2, 5), (7, 8), (10, 15)], [(6, 9)], [(2, 15)])
        preveri(
            [(3, 5), (9, 10), (13, 15), (19, 24), (26, 27), (33, 35), (37, 38), (45, 47), (49, 50), (53, 55),
             (60, 60), (62, 62), (64, 66), (69, 69), (71, 71), (73, 73), (76, 77)],
            [(7, 9), (15, 16), (20, 20), (24, 25), (30, 33), (36, 36), (41, 42), (48, 48), (59, 65), (69, 72), (79, 81)],
            [(3, 5), (7, 9), (15, 16), (20, 20), (24, 27), (30, 33), (36, 38), (41, 42), (45, 50), (53, 55), (59, 65),
             (69, 73), (76, 77), (79, 81)])


if __name__ == "__main__":
    unittest.main()
