import unittest

def dolzina_ovir(vrstica):
    return vrstica.count("#")

def stevilo_ovir(vrstica):
    ovir = 1 if vrstica[0] == "#" else 0
    for prej, zdaj in zip(vrstica, vrstica[1:]):
        if prej == "." and zdaj == "#":
            ovir += 1
    return ovir

def najsirsa_ovira(vrstica):
    dolzine_ovir = []
    v_oviri = False
    if vrstica[-1] == "#":
        vrstica += "."

    for i, char in enumerate(vrstica):
        if char == "#" and v_oviri is False:
            start = i
            v_oviri = True
        elif char == "#" and v_oviri is True:
            continue
        elif char == "." and v_oviri is True:
            end = i
            dolzine_ovir.append(end - start)
            v_oviri = False
    return max(dolzine_ovir)

def pretvori_vrstico(vrstica):
    ovire = []
    v_oviri = False
    if vrstica[-1] == "#":
        vrstica += "."

    for i, char in enumerate(vrstica):
        if char == "#" and v_oviri is False:
            start = i
            v_oviri = True
        elif char == "#" and v_oviri is True:
            continue
        elif char == "." and v_oviri is True:
            end = i
            ovire.append((start + 1, end))
            v_oviri = False
    return ovire

def pretvori_zemljevid(vrstice):
    seznam = []
    for y, vrstica in enumerate(vrstice, start=1):
        if len(pretvori_vrstico(vrstica)) >= 1:
            for x1, x2 in pretvori_vrstico(vrstica):
                nova_ovira = (x1, x2, y)
                seznam.append(nova_ovira)
    return seznam

def izboljsave(prej, potem):
    return sorted(list(set(pretvori_zemljevid(potem)) - set(pretvori_zemljevid(prej))), key=lambda ovira: ovira[2]) #ovira(x1, x2, y) -> ovira[2] == y!

def huligani(prej, potem):
    ovire_prej = set(pretvori_zemljevid(prej))
    ovire_potem = set(pretvori_zemljevid(potem))

    dodane = sorted(ovire_potem - ovire_prej, key=lambda ovira: ovira[2])
    odstranjene = sorted(ovire_prej - ovire_potem, key=lambda ovira: ovira[2])

    return dodane, odstranjene









class Test(unittest.TestCase):
    def test_dolzina_ovir(self):
        self.assertEqual(3, dolzina_ovir("...###..."))
        self.assertEqual(1, dolzina_ovir("...#..."))
        self.assertEqual(2, dolzina_ovir("...#..#."))
        self.assertEqual(7, dolzina_ovir("#...#####..#."))
        self.assertEqual(8, dolzina_ovir("...#####.##...#"))
        self.assertEqual(9, dolzina_ovir("#...#####.##...#"))
        self.assertEqual(6, dolzina_ovir("##...#.#...##"))
        self.assertEqual(0, dolzina_ovir("..."))
        self.assertEqual(0, dolzina_ovir("."))

    def test_stevilo_ovir(self):
        self.assertEqual(1, stevilo_ovir("...###..."))
        self.assertEqual(1, stevilo_ovir("...#..."))
        self.assertEqual(2, stevilo_ovir("...#..#."))
        self.assertEqual(3, stevilo_ovir("#...#####..#."))
        self.assertEqual(3, stevilo_ovir("...#####.##...#"))
        self.assertEqual(4, stevilo_ovir("#...#####.##...#"))
        self.assertEqual(4, stevilo_ovir("##...#.#...##"))
        self.assertEqual(0, stevilo_ovir("..."))
        self.assertEqual(0, stevilo_ovir("."))

    def test_najsirsa_ovira(self):
        self.assertEqual(3, najsirsa_ovira("...###..."))
        self.assertEqual(1, najsirsa_ovira("...#..."))
        self.assertEqual(1, najsirsa_ovira("...#..#."))
        self.assertEqual(5, najsirsa_ovira("#...#####..#."))
        self.assertEqual(5, najsirsa_ovira("...#####.##...#"))
        self.assertEqual(5, najsirsa_ovira("#...#####.##...#"))
        self.assertEqual(6, najsirsa_ovira("######...#####.##...#"))
        self.assertEqual(6, najsirsa_ovira("...#####.##...######"))

    def test_pretvori_vrstico(self):
        self.assertEqual([(3, 5)], pretvori_vrstico("..###."))
        self.assertEqual([(3, 5), (7, 7)], pretvori_vrstico("..###.#."))
        self.assertEqual([(1, 2), (5, 7), (9, 9)], pretvori_vrstico("##..###.#."))
        self.assertEqual([(1, 1), (4, 6), (8, 8)], pretvori_vrstico("#..###.#."))
        self.assertEqual([(1, 1), (4, 6), (8, 8)], pretvori_vrstico("#..###.#"))
        self.assertEqual([], pretvori_vrstico("..."))
        self.assertEqual([], pretvori_vrstico(".."))
        self.assertEqual([], pretvori_vrstico("."))

    def test_pretvori_zemljevid(self):
        zemljevid = [
            "......",
            "..##..",
            ".##.#.",
            "...###",
            "###.##",
        ]
        self.assertEqual([(3, 4, 2), (2, 3, 3), (5, 5, 3), (4, 6, 4), (1, 3, 5), (5, 6, 5)], pretvori_zemljevid(zemljevid))

        zemljevid = [
            "..............##...",
            "..###.....###....##",
            "...###...###...#...",
            "...........#.....##",
            "...................",
            "###.....#####...###"
        ]
        self.assertEqual([(15, 16, 1),
                          (3, 5, 2), (11, 13, 2), (18, 19, 2),
                          (4, 6, 3), (10, 12, 3), (16, 16, 3),
                          (12, 12, 4), (18, 19, 4),
                          (1, 3, 6), (9, 13, 6), (17, 19, 6)], pretvori_zemljevid(zemljevid))

    def test_izboljsave(self):
        prej = [
            "..............##...",
            "..###.....###....##",
            "...###...###...#...",
            "...........#.....##",
            "...................",
            "###.....#####...###"
        ]

        potem = [
            "...##.........##...",
            "..###.....###....##",
            "#..###...###...#...",
            "...###.....#.....##",
            "................###",
            "###.....#####...###"
        ]

        self.assertEqual([(4, 5, 1), (1, 1, 3), (4, 6, 4), (17, 19, 5)], izboljsave(prej, potem))

        self.assertEqual([], izboljsave(prej, prej))

    def test_huligani(self):
        prej = [
            "..............##...",
            "..###.....###....##",
            "...###...###...#...",
            "...........#.....##",
            "...................",
            "###.....#####...###"
        ]

        potem = [
            "...##..............",
            "..........###....##",
            "#..###...###...#...",
            "...###.....#.....##",
            "................###",
            "###.....##.##...###"
        ]

        dodane, odstranjene = huligani(prej, potem)
        self.assertEqual([(4, 5, 1), (1, 1, 3), (4, 6, 4), (17, 19, 5), (9, 10, 6), (12, 13, 6)], dodane, "Napaka v seznamu dodanih")
        self.assertEqual([(15, 16, 1), (3, 5, 2), (9, 13, 6)], odstranjene, "Napaka v seznamu odstranjenih")

        dodane, odstranjene = huligani(potem, prej)  # Pazi, obrnjeno!
        self.assertEqual([(15, 16, 1), (3, 5, 2), (9, 13, 6)], dodane, "Napaka v seznamu dodanih")
        self.assertEqual([(4, 5, 1), (1, 1, 3), (4, 6, 4), (17, 19, 5), (9, 10, 6), (12, 13, 6)], odstranjene, "Napaka v seznamu odstranjenih")

        self.assertEqual(([], []), huligani(prej, prej))


if __name__ == "__main__":
    unittest.main()
