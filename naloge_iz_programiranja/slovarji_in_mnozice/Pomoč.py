import collections
import random
import urllib.request
from collections import defaultdict
from random import choice

inventar = {
            'sir': 8, 'kruh': 15, 'makovka': 10, 'pasja radost': 2,
            'pašteta': 10, 'mortadela': 4, 'klobasa': 7
        }

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
    naj = max(f, key=f.get)
    return naj

def najpogostejse_urejene(s):
    crke = freq(s)
    urejene_crke = sorted(crke, key=crke.get, reverse=True)

    besede = s.split()
    words = freq(besede)
    urejene_besede = sorted(words, key=words.get, reverse=True)

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
    zacetna = random.choice(list(nasl.keys()))
    for i in range(num_besed):
        besede.append(zacetna)
        zacetna = random.choice(nasl.get(zacetna, list(nasl.keys())))
    return " ".join(besede)

family = [('bob', 'mary'), ('bob', 'tom'), ('bob', 'judy'), ('alice', 'mary'),
    ('alice', 'tom'), ('alice', 'judy'), ('renee', 'rob'), ('renee', 'bob'),
    ('sid', 'rob'), ('sid', 'bob'), ('tom', 'ken'), ('ken', 'suzan'), ('rob', 'jim')]

def family_tree(family):
    slovar = dict()
    for stars, otrok in family:
        if stars not in slovar:
            slovar[stars] = [otrok]
        else:
            slovar[stars] += [otrok]
    return slovar


def family_tree(family):
    slovar = collections.defaultdict(list)
    for stars, otrok in family:
        slovar[stars].append(otrok)
    return slovar

tree = family_tree(family)

def children(tree, name):
    return tree.get(name, [])

def grandchildren(tree, name):
    vnuki = []
    for otrok in children(tree, name):
        for vnuk in children(tree, otrok):
            vnuki.append(vnuk)
    print(vnuki)

def successors(tree, name):
    imena = []
    for child in children(tree, name):
        imena.append(child)
        imena.extend(successors(tree, child))
    return imena

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

def potrebne_vescine(pot, zemljevid):
    pari = []
    for k1, k2 in zip(pot, pot[1:]):
        pari.append((k1, k2))

    potrebne = set()
    for par in pari:
        for vescina in zemljevid[par]:
            potrebne.add(vescina)

    return potrebne

def kam(zemljevid, tocka, vescine):
    potencialne = []
    for start, cilj in zemljevid:
        if start == tocka:
            potencialne.append((tocka, cilj))

    mozne_tocke = set()
    for par in potencialne:
        if vescine > set(zemljevid[par]):
            mozne_tocke.add(par[1])
    return mozne_tocke

def dolgcas(zemljevid):
    mnozica_frozensetov = set()
    for par in zemljevid:
        if not zemljevid[par]:
            mnozica_frozensetov.add(frozenset(par))

    mnozica = set()
    for par in mnozica_frozensetov:
        mnozica.add(tuple(par))

    return mnozica

def koncna_tocka(pot, zemljevid, vescine):
    for par in zip(pot, pot[1:]):
        trenutna_tocka = par[0]
        if vescine >= zemljevid[par]:
            continue
        else:
            return trenutna_tocka, zemljevid[par] - vescine
    return None


print(koncna_tocka("ABCRVB", zemljevid, {"gravel", "trava"}))