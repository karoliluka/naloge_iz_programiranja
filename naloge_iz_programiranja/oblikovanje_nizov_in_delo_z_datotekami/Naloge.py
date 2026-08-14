def preberi_vrstice(ime_datoteke):
    seznam = []
    for vrstica in open(ime_datoteke):
        seznam.append(vrstica.strip())
    return seznam

def preberi_csv(ime_datoteke):
    seznam_terk = []
    for vrstica in open(ime_datoteke):
        kraj, vreme, temp = vrstica.strip().split(";")
        seznam_terk.append((kraj, vreme, float(temp)))
    return seznam_terk

def oblikuj(podatki):
    seznam_nizov = []
    for kraj, vreme, temp in podatki:
        seznam_nizov.append(f"Kraj: {kraj}, Vreme: {vreme}, Temperatura: {temp}°C")
    return seznam_nizov

def oblikuj_tabelo(podatki):
    seznam_nizov = ['Kraj            Vreme           Temperatura (°C)', '------------------------------------------------']
    for kraj, vreme, temp in podatki:
        seznam_nizov.append(f"{kraj:16}{vreme:<28}{temp:>4}")
    return seznam_nizov

def oblikuj_tabelo_f(podatki):
    seznam_nizov = ['Kraj            Vreme           Temperatura (°F)', '------------------------------------------------']
    for kraj, vreme, temp in podatki:
        seznam_nizov.append(f"{kraj:16}{vreme:<28}{(temp * 9/5) + 32:>4.1f}")
    return seznam_nizov

def oblikuj_pike(podatki):
    seznam_nizov = ['Kraj            Vreme           Temperatura (°F)', '------------------------------------------------']
    for kraj, vreme, temp in podatki:
        seznam_nizov.append(f"{kraj:.<16}{vreme:.<28}{(temp * 9 / 5) + 32:.>4.1f}")
    return seznam_nizov

def oblikuj_fc(podatki):
    seznam = []
    seznam.append(f"Kraj            Vreme        Temperatura °F (°C)")
    seznam.append(f"------------------------------------------------")
    for mesto, vreme, temp in podatki:
        stopinje_str = f"{(temp * 9 / 5) + 32:.1f} ({temp:.1f})"
        seznam.append(f"{mesto:.<16}{vreme:.<16}{stopinje_str:.>16}")
    return seznam

def shrani(vrstice, ime_datoteke):
    file = open(ime_datoteke, "w")
    for vrsta in vrstice:
        file.write(vrsta + "\n")

def najdaljse_besede(s):
    naj = 0
    for beseda in s.split():
        if len(beseda) > naj:
            naj = len(beseda)

    najdaljse = []
    for beseda in s.split():
        if len(beseda) == naj:
            najdaljse.append(beseda)
    return ", ".join(najdaljse)





### ^^^ Naloge rešujte nad tem komentarjem. ^^^ ###

import unittest

class Testi(unittest.TestCase):

    def setUp(self):
        f = open("podatki.txt","w",encoding='utf-8')
        f.write("Ljubljana;oblačno;12.1\n")
        f.write("Maribor;sončno;9\n")
        f.write("Koper;sončno;14.7\n")
        f.close()

        self.podatki = [('Ljubljana', 'oblačno', 12.1), ('Maribor', 'sončno', 9.0), ('Koper', 'sončno', 14.7)]

    def test_preberi_vrstice(self):
        self.assertEqual(preberi_vrstice("podatki.txt"), ["Ljubljana;oblačno;12.1", "Maribor;sončno;9", "Koper;sončno;14.7"])

    def test_preberi_csv(self):
        self.assertEqual(preberi_csv("podatki.txt"), [('Ljubljana', 'oblačno', 12.1), ('Maribor', 'sončno', 9.0), ('Koper', 'sončno', 14.7)])

    def test_oblikuj(self):
        self.assertEqual(oblikuj(self.podatki),
                         ['Kraj: Ljubljana, Vreme: oblačno, Temperatura: 12.1°C',
                          'Kraj: Maribor, Vreme: sončno, Temperatura: 9.0°C',
                          'Kraj: Koper, Vreme: sončno, Temperatura: 14.7°C'])

    def test_oblikuj_tabelo(self):
        self.assertEqual(oblikuj_tabelo(self.podatki),
                         ['Kraj            Vreme           Temperatura (°C)',
                          '------------------------------------------------',
                          'Ljubljana       oblačno                     12.1',
                          'Maribor         sončno                       9.0',
                          'Koper           sončno                      14.7'])

    def test_oblikuj_tabelo_f(self):
        self.assertEqual(oblikuj_tabelo_f(self.podatki),
                         ['Kraj            Vreme           Temperatura (°F)',
                          '------------------------------------------------',
                          'Ljubljana       oblačno                     53.8',
                          'Maribor         sončno                      48.2',
                          'Koper           sončno                      58.5'])

    def test_oblikuj_pike(self):
        self.assertEqual(oblikuj_pike(self.podatki),
                         ['Kraj            Vreme           Temperatura (°F)',
                          '------------------------------------------------',
                          'Ljubljana.......oblačno.....................53.8',
                          'Maribor.........sončno......................48.2',
                          'Koper...........sončno......................58.5'])

    def test_oblikuj_fc(self):
        self.assertEqual(oblikuj_fc(self.podatki),
                         ['Kraj            Vreme        Temperatura °F (°C)',
                          '------------------------------------------------',
                          'Ljubljana.......oblačno..............53.8 (12.1)',
                          'Maribor.........sončno................48.2 (9.0)',
                          'Koper...........sončno...............58.5 (14.7)'])

    def test_shrani(self):
        lines = ['prva vrstica', 'druga vrstica', 'tretja vrstica']
        shrani(lines, 'datoteka.txt')
        f = open("datoteka.txt", "r")
        lines_f = f.read().splitlines()
        f.close()
        self.assertEqual(lines_f, lines)

    def test_najdaljse_besede(self):
        self.assertEqual(najdaljse_besede('ob znaku bo ura deset in pet minut'), 'znaku, deset, minut')

if __name__ == '__main__':
    unittest.main(verbosity=2)
