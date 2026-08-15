zmage = {'Ana': {'Vera', 'Cilka'},
         'Berta': {'Greta', 'Klara', 'Iva', 'Cilka'},
         'Cilka': {'Olga'},
         'Črtomira': set(),
         'Dani': {'Liza', 'Ana', 'Fanči', 'Cilka', 'Micka', 'Greta'},
         'Ema': set(),
         'Fanči': {'Liza', 'Poldka', 'Cilka'},
         'Greta': set(),
         'Helga': set(),
         'Iva': {'Ema', 'Helga'},
         'Jana': {'Liza', 'Dani', 'Berta', 'Micka', 'Tina', 'Greta'},
         'Klara': {'Helga', 'Nina'},
         'Liza': {'Vera', 'Olga', 'Rezka'},
         'Micka': {'Liza', 'Saša', 'Urša'},
         'Nina': {'Olga', 'Poldka'},
         'Olga': {'Poldka'},
         'Poldka': set(),
         'Rezka': {'Saša'},
         'Saša': set(),
         'Špela': {'Žana'},
         'Tina': set(),
         'Urša': {'Vera'},
         'Vera': set(),
         'Zoja': {'Žana', 'Tina'},
         'Žana': set()}

def hitrejsa(prva, druga):
    if druga in zmage[prva]:
        return True
    if not zmage[prva]:
        return False

    for kolesarka in zmage[prva]:
        if hitrejsa(kolesarka, druga):
            return True
    return False

def skalpi(kolesarka):
    if not zmage[kolesarka]:
        return set([kolesarka])

    mnozica = set([kolesarka])
    for ime in zmage[kolesarka]:
        mnozica |= skalpi(ime)
    return mnozica

def dokazov(prva, druga):
    if not zmage[prva]:
        return 0

    st_dokazov = 0
    for ime in zmage[prva]:
        if ime == druga:
            st_dokazov += 1
        else:
            st_dokazov += dokazov(ime, druga)
    return st_dokazov

def zanesljivo_hitrejsa(prva, druga, n):
    if druga in zmage[prva]:
        return True
    if n == 0:
        return False

    for kolesarka in zmage[prva]:
        if zanesljivo_hitrejsa(kolesarka, druga, n - 1):
            return True
    return False

def obisci(oseba, obiskani, rezultat):
    if oseba in obiskani:
        return None

    obiskani.add(oseba)
    for kolesarka in zmage[oseba]:
        obisci(kolesarka, obiskani, rezultat)
    rezultat.append(oseba)

def uredi(zmage):
    obiskani = set()
    rezultat = []
    for kolesarka in zmage:
        obisci(kolesarka, obiskani, rezultat)
    rezultat.reverse()
    return rezultat




import unittest

class Test01Obvezna(unittest.TestCase):
    def test_01_hitrejsa(self):
        self.assertTrue(hitrejsa("Jana", "Berta"))
        self.assertFalse(hitrejsa("Berta", "Jana"))
        self.assertTrue(hitrejsa("Berta", "Poldka"))
        self.assertFalse(hitrejsa("Poldka", "Berta"))
        self.assertFalse(hitrejsa("Saša", "Berta"))
        self.assertFalse(hitrejsa("Berta", "Saša"))
        self.assertFalse(hitrejsa("Špela", "Tina"))
        self.assertFalse(hitrejsa("Jana", "Črtomira"))
        self.assertFalse(hitrejsa("Črtomira", "Jana"))

    def test_02_skalpi(self):
        self.assertEqual(
            {"Berta", "Cilka", "Olga", "Poldka", "Iva", "Klara", "Helga", "Ema", "Nina", "Greta"},
            skalpi("Berta"))
        self.assertEqual(
            {"Cilka", "Olga", "Poldka"},
            skalpi("Cilka"))
        self.assertEqual(
            {"Olga", "Poldka"},
            skalpi("Olga"))
        self.assertEqual(
            {"Greta"},
            skalpi("Greta"))
        self.assertEqual(
            {"Iva", "Helga", "Ema"},
            skalpi("Iva"))


class Test02Dodatna(unittest.TestCase):
    def test_01_dokazov(self):
        self.assertEqual(1, dokazov("Jana", "Berta"))
        self.assertEqual(0, dokazov("Berta", "Jana"))
        self.assertEqual(4, dokazov("Jana", "Cilka"))
        self.assertEqual(1, dokazov("Jana", "Nina"))
        self.assertEqual(5, dokazov("Jana", "Liza"))
        self.assertEqual(10, dokazov("Jana", "Olga"))
        self.assertEqual(12, dokazov("Jana", "Poldka"))
        self.assertEqual(1, dokazov("Špela", "Žana"))

    def test_02_zanesljivo_hitrejsa(self):
        self.assertTrue(zanesljivo_hitrejsa("Jana", "Berta", 0))
        self.assertTrue(zanesljivo_hitrejsa("Jana", "Berta", 3))
        self.assertTrue(zanesljivo_hitrejsa("Jana", "Cilka", 1))
        self.assertFalse(zanesljivo_hitrejsa("Jana", "Cilka", 0))
        self.assertTrue(zanesljivo_hitrejsa("Jana", "Poldka", 3))
        self.assertTrue(zanesljivo_hitrejsa("Jana", "Poldka", 2))
        self.assertFalse(zanesljivo_hitrejsa("Jana", "Poldka", 1))
        self.assertFalse(zanesljivo_hitrejsa("Klara", "Ema", 100))
        self.assertFalse(zanesljivo_hitrejsa("Poldka", "Cilka", 100))
        self.assertTrue(zanesljivo_hitrejsa("Fanči", "Poldka", 0))

        self.assertFalse(zanesljivo_hitrejsa("Berta", "Poldka", 1))
        self.assertTrue(zanesljivo_hitrejsa("Berta", "Poldka", 2))
        self.assertTrue(zanesljivo_hitrejsa("Berta", "Poldka", 3))
        self.assertTrue(zanesljivo_hitrejsa("Berta", "Poldka", 4))


class Test03SeBoljDodatna(unittest.TestCase):
    def test_01_uredi(self):
        urejena = uredi(zmage)
        for i, x in enumerate(urejena):
            for y in urejena[:i]:
                self.assertFalse(hitrejsa(x, y), f"Napaka: {x} je postavljena za {y}, čeprav je hitrejša od nje")

if __name__ == "__main__":
    unittest.main()
