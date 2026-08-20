# Svojo rešitev pišite sem.
# Najboljše je, da pustite teste v datoteki z rašitvijo, da ne bi ponesreči pobrisali preveč.
from naloge_iz_programiranja.slovarji_in_mnozice.Pomoč import zemljevid


def unzip(s, sirina):
    smeri = ["<", ">", "v", "^"]
    nov_niz = ""
    zadnja_smer = ""

    for znak in s:
        if znak in smeri:
            nov_niz += znak
            zadnja_smer = znak
        elif znak.isnumeric():
            nov_niz += zadnja_smer * int(znak)

    vrstice = []
    for zacetek in range(0, len(nov_niz), sirina):
        vrstice.append(nov_niz[zacetek : zacetek + sirina])

    return vrstice

def pot_do_ponovitve(zemljevid, x, y):
    obiskana = []
    trenutna = (x, y)

    while trenutna not in obiskana:
        obiskana.append(trenutna)
        nx, ny = trenutna
        znak = zemljevid[ny][nx]

        if znak == ">":
            trenutna = (nx + 1, ny)
        elif znak == "<":
            trenutna = (nx - 1, ny)
        elif znak == "v":
            trenutna = (nx, ny + 1)
        elif znak == "^":
            trenutna = (nx, ny - 1)

    obiskana.append(trenutna)
    return obiskana

def pred_ciklom(zemljevid, x, y):
    pot = pot_do_ponovitve(zemljevid, x, y)
    ponovljeno_polje = pot[-1]
    return pot.index(ponovljeno_polje)

def naslednje_polje(zemljevid, x, y):
    znak = zemljevid[y][x]
    if znak == ">":
        return (x + 1, y)
    elif znak == "<":
        return (x - 1, y)
    elif znak == "v":
        return (x, y + 1)
    elif znak == "^":
        return (x, y - 1)

def polja_do(zemljevid, x, y):
    visina = len(zemljevid)
    sirina = len(zemljevid[0])

    obratni_graf = {}
    for vy in range(visina):
        for vx in range(sirina):
            nasl = naslednje_polje(zemljevid, vx, vy)
            obratni_graf.setdefault(nasl, []).append((vx, vy))

    # sirjenje nazaj po obratnem grafu, zacensi pri (x, y)
    obiskana = {(x, y)}
    vrsta = [(x, y)]
    while vrsta:
        trenutno = vrsta.pop()
        for prejsnje in obratni_graf.get(trenutno, []):
            if prejsnje not in obiskana:
                obiskana.add(prejsnje)
                vrsta.append(prejsnje)

    return obiskana

def polja_do_rek(zemljevid, x, y, prepovedana):
    if (x, y) in prepovedana:
        return set()

    rezultat = set()
    rezultat.add((x, y))
    for vy in range(len(zemljevid)):
        for vx in range(len(zemljevid[0])):
            if naslednje_polje(zemljevid, vx, vy) == (x, y):
                rezultat |= polja_do_rek(zemljevid, vx, vy, prepovedana | {(x, y)})
    return rezultat



class Plug:
    def __init__(self, zemljevid, x, y):
        self.zemljevid = zemljevid
        self.x = x
        self.y = y
        self.ociscenih_polj = 0
        self.servis = 0

    def lokacija(self):
        return (self.x, self.y)

    def ociscenih(self):
        return self.ociscenih_polj

    def premik(self, smer):
        if self.servis:
            self.servis -= 1
            return

        nx, ny = {"<": (self.x - 1, self.y), ">": (self.x + 1, self.y),
                  "^": (self.x, self.y - 1), "v": (self.x, self.y + 1)}[smer]
        if 0 <= nx < len(self.zemljevid[0]) and 0 <= ny < len(self.zemljevid):
            s = self.zemljevid[self.y]
            if s[self.x] != ".":
                self.zemljevid[self.y] = s[:self.x] + "." + s[self.x + 1:]
                self.ociscenih_polj += 1
            self.x, self.y = nx, ny
        else:
            self.servis = 3





import unittest

sneg = """
>>v>>v
vvv^<<
>>>>v^
^^<>>v
>^<<<<""".strip().splitlines()

print(sneg)

class Test(unittest.TestCase):
    def test_01_unzip(self):
        self.assertEqual(["<^<<vvvv"], unzip("<^<<vvvv", 8))
        self.assertEqual(["<^<<", "vvvv"], unzip("<^<<vvvv", 4))
        self.assertEqual(["<^<<", "vvvv"], unzip("<^<<v3", 4))
        self.assertEqual(sneg, unzip(">1v>1v3^<1>3v^2<>>v>^<3", 6))

        self.assertEqual([">" * 4] * 3, unzip(">56", 4))

    def test_02_pred_ciklom(self):
        self.assertEqual(4, pred_ciklom(sneg, 0, 0))
        self.assertEqual(3, pred_ciklom(sneg, 1, 0))
        self.assertEqual(2, pred_ciklom(sneg, 2, 0))
        self.assertEqual(1, pred_ciklom(sneg, 2, 1))
        self.assertEqual(0, pred_ciklom(sneg, 2, 2))

        self.assertEqual(1, pred_ciklom(sneg, 1, 1))
        self.assertEqual(0, pred_ciklom(sneg, 1, 2))
        self.assertEqual(0, pred_ciklom(sneg, 2, 2))
        self.assertEqual(0, pred_ciklom(sneg, 3, 2))

        self.assertEqual(1, pred_ciklom(sneg, 0, 2))
        self.assertEqual(2, pred_ciklom(sneg, 0, 3))

        self.assertEqual(1, pred_ciklom(sneg, 0, 4))

        self.assertEqual(0, pred_ciklom(sneg, 3, 0))
        self.assertEqual(1, pred_ciklom(sneg, 5, 2))

        self.assertEqual(4, pred_ciklom([">>>>><"], 0, 0))

    def test_03_polja_do(self):
        self.assertEqual({(0, 0)},
                         polja_do(sneg, 0, 0))
        self.assertEqual({(0, 1), (0, 2), (0, 3)},
                         polja_do(sneg, 0, 2))
        self.assertEqual({(0, 1), (2, 4), (1, 2), (0, 4), (3, 4), (2, 1), (4, 3), (5, 4), (0, 2), (2, 2), (1, 0), (3, 2), (1, 3), (4, 4), (0, 0), (1, 1), (0, 3), (2, 0), (1, 4), (4, 2), (2, 3), (3, 3), (5, 3)},
                         polja_do(sneg, 1, 2))
        self.assertEqual({(0, 1), (2, 4), (1, 2), (0, 4), (3, 4), (2, 1), (4, 3), (5, 4), (0, 2), (2, 2), (1, 0), (3, 2), (1, 3), (4, 4), (0, 0), (1, 1), (0, 3), (2, 0), (1, 4), (4, 2), (2, 3), (3, 3), (5, 3)},
                         polja_do(sneg, 1, 3))

    def test_04_polja_do_rek(self):
        self.assertEqual({(0, 0)},
                         polja_do_rek(sneg, 0, 0, set()))
        self.assertEqual({(0, 1), (0, 2), (0, 3)},
                         polja_do_rek(sneg, 0, 2, set()))
        self.assertEqual({(0, 1), (0, 2)},
                         polja_do_rek(sneg, 0, 2, {(0, 3)}))
        self.assertEqual({(0, 1), (2, 4), (1, 2), (0, 4), (3, 4), (2, 1), (4, 3), (5, 4), (0, 2), (2, 2), (1, 0), (3, 2), (1, 3), (4, 4), (0, 0), (1, 1), (0, 3), (2, 0), (1, 4), (4, 2), (2, 3), (3, 3), (5, 3)},
                         polja_do_rek(sneg, 1, 2, set()))
        self.assertEqual({(0, 1), (2, 4), (1, 2), (0, 4), (3, 4), (2, 1), (4, 3), (5, 4), (0, 2), (2, 2), (1, 0), (3, 2), (1, 3), (4, 4), (0, 0), (1, 1), (0, 3), (2, 0), (1, 4), (4, 2), (2, 3), (3, 3), (5, 3)},
                         polja_do_rek(sneg, 1, 3, set()))

    def test_05_plug(self):
        zemljevid = sneg.copy()
        plug1 = Plug(zemljevid, 0, 0)
        plug2 = Plug(zemljevid, 2, 0)
        plug3 = Plug(zemljevid, 1, 4)

        self.assertEqual((1, 4), plug3.lokacija())
        self.assertEqual(0, plug3.ociscenih())

        plug2.premik("<")
        self.assertEqual((1, 0), plug2.lokacija())
        self.assertEqual(1, plug2.ociscenih())

        plug2.premik("v")
        self.assertEqual((1, 1), plug2.lokacija())
        self.assertEqual(2, plug2.ociscenih()) # očistil je polje (1, 1)

        plug2.premik("v")
        self.assertEqual((1, 2), plug2.lokacija())
        self.assertEqual(3, plug2.ociscenih())

        plug1.premik("v")
        self.assertEqual((0, 1), plug1.lokacija())
        self.assertEqual(1, plug1.ociscenih())

        plug1.premik(">")
        self.assertEqual((1, 1), plug1.lokacija())
        self.assertEqual(2, plug1.ociscenih())  # očistil je polje (0, 1)

        plug1.premik(">")
        self.assertEqual((2, 1), plug1.lokacija())
        self.assertEqual(2, plug1.ociscenih())  # ni očistil polja (1, 1), ker ga je pred njim že plug2

        plug1.premik(">")
        self.assertEqual((3, 1), plug1.lokacija())
        self.assertEqual(3, plug1.ociscenih())  # očistil je polje (2, 1)

        plug3.premik("<")
        self.assertEqual((0, 4), plug3.lokacija())
        self.assertEqual(1, plug3.ociscenih())  # očistil je polje (1, 4)

        plug3.premik(">")
        self.assertEqual((1, 4), plug3.lokacija())
        self.assertEqual(2, plug3.ociscenih())  # očistil je polje (0, 4)

        plug3.premik("<")
        self.assertEqual((0, 4), plug3.lokacija())
        self.assertEqual(2, plug3.ociscenih())  # (1, 4) je bilo že čisto

        plug3.premik(">")
        self.assertEqual((1, 4), plug3.lokacija())
        self.assertEqual(2, plug3.ociscenih())  # (0, 4) tudi

        plug3.premik("v")  # zapelje ven: ignoriramo naslednje tri ukaze
        self.assertEqual((1, 4), plug3.lokacija())
        self.assertEqual(2, plug3.ociscenih())  # (0, 4) tudi

        plug3.premik("^")  # ignoriramo
        self.assertEqual((1, 4), plug3.lokacija())
        self.assertEqual(2, plug3.ociscenih())

        plug3.premik("^")  # ignoriramo
        self.assertEqual((1, 4), plug3.lokacija())
        self.assertEqual(2, plug3.ociscenih())

        plug2.premik("v")
        self.assertEqual((1, 3), plug2.lokacija())  # plug 2 očisti (1, 2)
        self.assertEqual(4, plug2.ociscenih())

        plug2.premik("v")
        self.assertEqual((1, 4), plug2.lokacija())  # plug 2 očisti (1, 3)
        self.assertEqual(5, plug2.ociscenih())

        plug2.premik(">")
        self.assertEqual((2, 4), plug2.lokacija())  # ne očisti (1, 4), ker ga je že plug 3
        self.assertEqual(5, plug2.ociscenih())

        plug3.premik("^")  # ignoriramo
        self.assertEqual((1, 4), plug3.lokacija())
        self.assertEqual(2, plug3.ociscenih())

        plug3.premik("^")  # ne ignoriramo ...
        self.assertEqual((1, 3), plug3.lokacija())  # vendar ne očisti (1, 4), ker ga je že prej
        self.assertEqual(2, plug3.ociscenih())

        plug3.premik("<")  # ne ignoriramo ...
        self.assertEqual((0, 3), plug3.lokacija())  # vendar ne očisti (1, 3), ker ga je že plug 2
        self.assertEqual(2, plug3.ociscenih())

        plug3.premik(">")
        self.assertEqual((1, 3), plug3.lokacija())
        self.assertEqual(3, plug3.ociscenih())  # očisti (0, 3)


if __name__ == "__main__":
    unittest.main()
