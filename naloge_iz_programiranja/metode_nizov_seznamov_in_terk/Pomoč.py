#Izloči besedo
"""
def izloci_besedo(beseda):
    while beseda and not beseda[0].isalnum():
        beseda = beseda[1:]
    while beseda and not beseda[-1].isalnum():
        beseda = beseda[:-1]
    return beseda

print(izloci_besedo("!!!janeu!"))
"""
from collections import defaultdict
from doctest import set_unittest_reportflags
from email.policy import default
from itertools import count

#Se začne z
"""
tviti = [
        "sandra: Spet ta dež. #dougcajt",
        "berta: @sandra Delaj domačo za #programiranje1",
        "sandra: @berta Ne maram #programiranje1 #krneki",
        "ana: kdo so te @berta, @cilka, @dani? #krneki",
        "cilka: jst sm pa #luft",
        "benjamin: pogrešam ano #zalosten",
        "ema: @benjamin @ana #split? po dvopičju, za začetek?",
    ]

def se_zacne_z(tvit, c):
    seznam = []
    for beseda in tvit.split(" "):
        if beseda[0] == c:
            niz = ""
            for char in beseda:
                if char.isalnum():
                    niz += char
            seznam.append(niz)
    return seznam

def zberi_se_zacne_z(tviti, c):
    seznam = []
    for tvit in tviti:
        if se_zacne_z(tvit, c):
            for beseda in se_zacne_z(tvit, c):
                if beseda not in seznam:
                    seznam.append(beseda)
    print(seznam)

print(zberi_se_zacne_z(tviti, "@"))
"""

#Angelčin zapis
def koordinate(s):
    x1 = ""
    for char in s:
        if char.isnumeric():
            x1 += char
    return int(x1), int(x1) + s.count("-") - 1

def vrstica(s):
    seznam = []
    s = s.split()
    y = ""
    for char in s[0]:
        if char.isnumeric():
            y += char

    for ovira in s[1:]:
        x1, x2 = koordinate(ovira)
        seznam.append((x1, x2, int(y)))
    print(seznam)

def preberi(s):
    seznam = []
    s = s.splitlines()
    for vrsta in s:
        seznam.append(vrstica(vrsta))
    return seznam

def intervali(xs):
    seznam = []
    for x1, x2 in xs:
        niz = str(x1)
        niz += ("-" * (x2 - x1 + 1))
        seznam.append(niz)
    return seznam

def zapisi_vrstico(y, xs):
    niz = "(" + str(y) + ") "
    seznam = intervali(xs)
    nove_ovire = []
    for i, ovira in enumerate(seznam):
        if i == len(seznam) - 1:
            break
        else:
            nove_ovire.append(ovira + " ")

    for ovira in nove_ovire:
        niz += ovira
    niz += seznam[-1]
    return niz

def zapisi(ovire):
    slovar = defaultdict(list) #kljuc bo vrstica, vrednosti pa pari na vrstici
    for x0, x1, y in ovire:
        par = (x0, x1)
        slovar[y] += par

    niz = ""
    for vrsta, pari in sorted(slovar.items()):
        pairs = []
        for x0, x1 in zip(pari[::2], pari[1::2]):
            pairs.append((x0, x1))
        niz += zapisi_vrstico(vrsta, sorted(pairs))
        niz += "\n"
    return niz

print(zapisi([(5, 6, 4),
        (90, 100, 13), (5, 8, 13), (9, 11, 13),
        (9, 11, 5), (19, 20, 5), (30, 34, 5),
        (9, 11, 4),
        (22, 25, 13), (17, 19, 13)]))