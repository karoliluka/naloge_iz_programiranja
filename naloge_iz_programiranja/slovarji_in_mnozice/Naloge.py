from email.policy import default
import random

def zaloga(inventar, artikel):
    return inventar[artikel]

def prodaj(inventar, artikel, kolicina):
    inventar[artikel] -= kolicina

def primanjkljaj(inventar, narocilo):
    slovar = collections.defaultdict(int)
    for aritkel_n, kolicina_n in narocilo.items():
        if aritkel_n in inventar:
            if kolicina_n > inventar[aritkel_n]:
                slovar[aritkel_n] += kolicina_n - inventar[aritkel_n]
        else:
            slovar[aritkel_n] = kolicina_n
    return slovar

def freq(s):
    return collections.Counter(s)

def max_freq(f):
    return max(f, key=f.get)

def najpogostejse(s):
    znaki = freq(s)
    najvec_znak = max_freq(znaki)

    besede = s.split()
    stevilo_besed = freq(besede)
    najvec_besed = max_freq(stevilo_besed)

    return najvec_besed, najvec_znak

def najpogostejse_urejene(s):
    crke = freq(s)
    urejene_crke = sorted(crke, key=lambda c: (-crke[c], c))

    besede = s.split()
    words = freq(besede)
    urejene_besede = sorted(words, key=lambda b: (-words[b], b))

    return urejene_besede, urejene_crke

def nasledniki(txt):
    seznam = dict()
    po_besedah = txt.split()
    for b1, b2 in zip(po_besedah, po_besedah[1:]):
        if b1 not in seznam:
            seznam[b1] = [b2]
        else:
            seznam[b1] += [b2]
    return seznam

def tekst(nasl, num_besed):
    besede = []
    vse_besede = list(nasl.keys())
    beseda = random.choice(vse_besede)
    for i in range(num_besed):
        besede.append(beseda)
        beseda = random.choice(nasl.get(beseda, vse_besede))
    return " ".join(besede)

def family_tree(family):
    slovar = collections.defaultdict(list)
    for stars, otrok in family:
        slovar[stars].append(otrok)
    return slovar

def children(tree, name):
    return tree.get(name, [])

def grandchildren(tree, name):
    vnuki = []
    for otrok in children(tree, name):
        for vnuk in children(tree, otrok):
            vnuki.append(vnuk)
    return vnuki

def successors(tree, name):
    imena = []
    for child in children(tree, name): #za vsakega otroka dodamo otroka v imena, potem pa podaljsamo seznam z otroci tega otroka
        imena.append(child)
        imena.extend(successors(tree, child))
    return imena

def sifriraj(niz, kljuc):
    return ''.join(chr(ord(c) ^ (kljuc // 256**(i % 2) % 256)) for i, c in enumerate(niz))

def sifra(niz):
    words = set()
    with open('Usr.Dict.Words') as f:
        for word in f:
            words.add(word.strip())

    for i in range(65536):
        desifrirano = sifriraj(niz, i)
        desifrirano_besedilo = desifrirano.split()
        if all(beseda in words for beseda in desifrirano_besedilo):
            return " ".join(desifrirano_besedilo)
    return None


### ^^^ Naloge rešujte nad tem komentarjem. ^^^ ###

import unittest
import collections

class TestSlovarji(unittest.TestCase):
    def setUp(self):
        self.tree = {
            'alice': ['mary', 'tom', 'judy'],
            'bob': ['mary', 'tom', 'judy'],
            'ken': ['suzan'],
            'renee': ['rob', 'bob'],
            'rob': ['jim'],
            'sid': ['rob', 'bob'],
            'tom': ['ken']}

    def assertDictCounterEqual(self, first, second, msg=None):
        def dict_counter(d):
            d_copy = dict(d)
            for k, v in d_copy.items():
                d_copy[k] = collections.Counter(v)
            return d_copy
        self.assertDictEqual(dict_counter(first), dict_counter(second), msg)

    def test_zaloga(self):
        inv = {"kruh": 5, "kajzerica": 4, "makovka": 3}
        self.assertEqual(zaloga(inv, "kruh"), 5)
        self.assertEqual(zaloga(inv, "kajzerica"), 4)
        self.assertEqual(zaloga(inv, "makovka"), 3)

    def test_prodaj(self):
        inv = {"kruh": 5, "kajzerica": 4, "makovka": 3}
        self.assertIsNone(prodaj(inv, "kajzerica", 2), "Funkcija naj ne vrača ničesar!")
        self.assertEqual(zaloga(inv, "kruh"), 5)
        self.assertEqual(zaloga(inv, "kajzerica"), 2)
        self.assertEqual(zaloga(inv, "makovka"), 3)

        prodaj(inv, "kruh", 5)
        self.assertTrue("kruh" not in inv or (zaloga(inv, "kruh"), 0))
        self.assertEqual(zaloga(inv, "kajzerica"), 2)
        self.assertEqual(zaloga(inv, "makovka"), 3)

    def test_primanjkljaj(self):
        inventar = {
            'sir': 8, 'kruh': 15, 'makovka': 10, 'pasja radost': 2,
            'pašteta': 10, 'mortadela': 4, 'klobasa': 7
        }
        self.assertDictEqual(
            primanjkljaj(inventar, {"kruh": 2, "makovka": 10}),
            {})
        self.assertDictEqual(
            primanjkljaj(inventar, {"kruh": 2, "makovka": 12}),
            {"makovka": 2})
        self.assertDictEqual(
            primanjkljaj(inventar, {"kruh": 2, "makovka": 12, "pivo": 3}),
            {"makovka": 2, "pivo": 3})
        self.assertDictEqual(primanjkljaj(inventar, {}), {})
        self.assertDictEqual(primanjkljaj(inventar, inventar), {})

    def test_family_tree(self):
        family = [
            ('bob', 'mary'),
            ('bob', 'tom'),
            ('bob', 'judy'),
            ('alice', 'mary'),
            ('alice', 'tom'),
            ('alice', 'judy'),
            ('renee', 'rob'),
            ('renee', 'bob'),
            ('sid', 'rob'),
            ('sid', 'bob'),
            ('tom', 'ken'),
            ('ken', 'suzan'),
            ('rob', 'jim')]
        self.assertDictCounterEqual(family_tree(family), self.tree)

    def test_children(self):
        self.assertCountEqual(children(self.tree, 'alice'), ['mary', 'tom', 'judy'])
        self.assertCountEqual(children(self.tree, 'mary'), [])
        self.assertCountEqual(children(self.tree, 'renee'), ['bob', 'rob'])
        self.assertCountEqual(children(self.tree, 'rob'), ['jim'])
        self.assertCountEqual(children(self.tree, 'suzan'), [])

    def test_grandchildren(self):
        self.assertCountEqual(grandchildren(self.tree, 'alice'), ['ken'])
        self.assertCountEqual(grandchildren(self.tree, 'bob'), ['ken'])
        self.assertCountEqual(grandchildren(self.tree, 'ken'), [])
        self.assertCountEqual(grandchildren(self.tree, 'mary'), [])
        self.assertCountEqual(grandchildren(self.tree, 'renee'), ['jim', 'mary', 'tom', 'judy'])
        self.assertCountEqual(grandchildren(self.tree, 'sid'), ['jim', 'mary', 'tom', 'judy'])
        self.assertCountEqual(grandchildren(self.tree, 'tom'), ['suzan'])

    def test_successors(self):
        self.assertCountEqual(successors(self.tree, 'tom'), ['ken', 'suzan'])
        self.assertCountEqual(successors(self.tree, 'sid'),
            ['rob', 'bob', 'jim', 'mary', 'tom', 'judy', 'ken', 'suzan'])
        self.assertCountEqual(successors(self.tree, 'suzan'), [])
        self.assertCountEqual(successors(self.tree, 'ken'), ['suzan'])
        self.assertCountEqual(successors(self.tree, 'rob'), ['jim'])

    def test_najpogostejse(self):
        self.assertEqual(najpogostejse('a'), ('a', 'a'))
        self.assertEqual(najpogostejse('aa bb aa'), ('aa', 'a'))
        self.assertEqual(najpogostejse('in to in ono in to smo mi'), ('in', ' '))
        self.assertEqual(najpogostejse('abc abc abc abacbca'), ('abc', 'a'))
        self.assertEqual(najpogostejse('abc abc abc abacbcb'), ('abc', 'b'))
        self.assertEqual(najpogostejse('abc abc abc abacbcc'), ('abc', 'c'))

    def test_najpogostejse_urejene(self):
        self.assertEqual(najpogostejse_urejene('a'), (['a'], ['a']))
        self.assertEqual(najpogostejse_urejene('aa bb aa'), (['aa', 'bb'], ['a', ' ', 'b']))
        self.assertEqual(najpogostejse_urejene('in to in ono in to smo mi'),
            (['in', 'to', 'mi', 'ono', 'smo'], [' ', 'o', 'i', 'n', 'm', 't', 's']))
        self.assertEqual(najpogostejse_urejene('abc abc abc abacbca'),
            (['abc', 'abacbca'], ['a', 'b', 'c', ' ']))
        self.assertEqual(najpogostejse_urejene('abc abc abc abacbcb'),
            (['abc', 'abacbcb'], ['b', 'a', 'c', ' ']))
        self.assertEqual(najpogostejse_urejene('abc abc abc abacbcc'),
            (['abc', 'abacbcc'], ['c', 'a', 'b', ' ']))

    def test_sifra(self):
        self.assertEqual(sifra('\x19\x14\x1c]\x19\x0f\x14\t\x13\x18\t]\x12\x0e[\n\x1a\t\x18\x15\x12\x13\x1c'),
            'big brother is watching')
        self.assertEqual(sifra('\xe1d\xe0q\xe5r\xf7b\xe0i'), 'strawberry')

    def test_nasledniki(self):
        self.assertDictCounterEqual(nasledniki('in in in in'), {'in': ['in', 'in', 'in']})
        self.assertDictCounterEqual(nasledniki('in to in ono in to smo mi'),
            {'smo': ['mi'], 'to': ['in', 'smo'], 'ono': ['in'], 'in': ['to', 'ono', 'to']})
        self.assertDictCounterEqual(nasledniki('danes je lep dan danes sije sonce'),
            {'lep': ['dan'], 'je': ['lep'], 'dan': ['danes'], 'danes': ['je', 'sije'], 'sije': ['sonce']})

    def test_tekst(self):
        self.assertEqual(tekst({'in': ['in', 'in']}, 3), 'in in in')

if __name__ == '__main__':
    unittest.main(verbosity=2)
