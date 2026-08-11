def kam(zemljevid, tocka, vescine):
    return {kam
            for (odkod, kam), potrebne in zemljevid.items()
            if odkod == tocka and potrebne <= vescine}

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


def dosegljive(zemljevid, tocka, vescine):
    obiskane = {tocka}
    za_obdelat = [tocka]
    while za_obdelat:
        trenutna = za_obdelat.pop()
        sosedi = kam(zemljevid, trenutna, vescine)
        for sosed in sosedi:
            if sosed not in obiskane:
                obiskane.add(sosed)
                za_obdelat.append(sosed)
    return obiskane

import unittest
import ast


class TestDosegljive(unittest.TestCase):
    def test(self):
        self.assertEqual(
            {'A', 'B', 'V'},
            dosegljive(zemljevid, 'A', {'trava', 'gravel'})
        )

        self.assertEqual(
            {'C', 'B', 'R', 'D', 'I', 'A', 'F', 'V'},
            dosegljive(zemljevid, 'C', {'lonci', 'pešci', 'stopnice', 'bolt', 'robnik'})
        )

        self.assertSetEqual(
            {'A', 'B', 'V', 'R', 'D', 'U', 'T', 'S', 'P', 'I', 'E', 'N', 'O'},
            dosegljive(zemljevid, 'A', {'trava', 'lonci', 'pešci', 'gravel', 'robnik'}),
        )

if "__main__" == __name__:
    unittest.main()
