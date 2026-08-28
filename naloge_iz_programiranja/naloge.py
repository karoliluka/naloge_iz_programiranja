import math
import os
import random
from collections import defaultdict, Counter
from datetime import date
from enum import unique
from itertools import pairwise, combinations

#--------------
#Čisti začetek
#--------------

#1.  Pretvarjanje iz Fahrenheitov v Celzije
"""
temp_F = float(input("Vpisi temp v F: "))
temp_C = 5/9 * (temp_F  - 32)
print(temp_F, "je", temp_C)
"""

#2. Pitagorov izrek
"""
a = float(input("Vpisi a:"))
b = float(input("Vpisi b:"))
print("Hipotenuza je: ", math.sqrt(pow(a, 2)+pow(b, 2)))
"""


#3. Topologija
"""
hitrost = float(input("Vnesite hitrost izstrelka: "))
kot = float(input("Vnesite kot izstrelka: "))
dolzina = pow(hitrost, 2) * (math.sin(2 * math.radians(kot)) / 10)
print("Izstrelek leti:", dolzina)
"""

#4. Ploščina trikotnika
"""
a = float(input("Vpisi a:"))
b = float(input("Vpisi b:"))
c = float(input("Vpisi c:"))
if a > b + c or b > a + c or c > a + b:
    print("Nepravilen trikotnik.")
else:
    s = (a + b + c) / 2
    p = math.sqrt(s * (s - a) * (s - b) * (s - c))
    print(p)
"""

#-------------
#Pogoji in zanke
#-------------

#5. vaja iz poštevanke
"""
a = random.randint(2, 10)
b = random.randint(2, 10)
print(a, "krat", b)
uporabnikov_odgovor = int(input("Odgovor? "))
if uporabnikov_odgovor == a * b:
    print("Pravilno.")
else:
    print("Napačno")
"""

#6. Vsi po pet
"""
vsota = 0
for i in range(5):
    cena_izdelka = float(input("Cena izdelka: "))
    vsota += cena_izdelka
print("Vsota:", vsota)
"""

#7. Konkurenca
"""
vsota = 0
n = int(input("Število izdelkov: "))
for i in range(n):
    cena_izdelka = float(input("Cena izdelka: "))
    vsota += cena_izdelka
print("Vsota:", vsota)
"""

#8. Top-shop
"""
vsota = 0
while True:
    cena_izdelka = float(input("Cena izdelka: "))
    vsota += cena_izdelka
    if cena_izdelka == 0:
        break

print("Vsota", vsota)
"""

#9. Državna agencija za varstvo potrošnikov
"""
vsota = 0
n = int(input("Število izdelkov: "))
for i in range(n):
    cena_izdelka = float(input("Cena izdelka: "))
    vsota += cena_izdelka
print("Vsota:", vsota)
print("Povprečna cena:", vsota / n)
"""

#10. Collatzova domneva
"""
n = random.randint(1, 100)
if n == 1:
    print(n)

while n != 1:
    if n % 2 == 0:
        n = n // 2
        print(n)
    elif n % 2 == 1:
        n = n * 3 + 1
        print(n)
"""

#11. Benjaminovi kovanci
"""
def vrzi():
    return random.choice("GC")

kovanci = 5

while kovanci != 10 and kovanci != 0:
    met = vrzi()
    if met == "G":
        kovanci -= 1
        print(met, kovanci)
    elif met == "C":
        kovanci += 1
        print(met, kovanci)
"""

#12. Tekmovanje iz postevanke
"""
tocke1 = 0
tocke2 = 0

while abs(tocke1 - tocke2) < 2:
    faktor1_1 = int(input("Tekmovalec 1, prvi faktor?"))
    faktor2_1 = int(input("Tekmovalec 1, drugi faktor?"))
    produkt_2 = int(input("Tekmovalec 2, produkt?"))

    if produkt_2 == faktor1_1 * faktor2_1:
        tocke2 += 1

    faktor1_2 = int(input("Tekmovalec 2, prvi faktor?"))
    faktor2_2 = int(input("Tekmovalec 2, drugi faktor?"))
    produkt_1 = int(input("Tekmovalec 1, produkt?"))

    if produkt_1 == faktor2_2 * faktor1_2:
        tocke1 += 1

    print("Trenutni rezultat:", tocke1, ":", tocke2)

if tocke2 > tocke1:
    print("Bravo drugi, prvi cvek!")

elif tocke1 > tocke2:
    print("Bravo prvi, drugi cvek!")
"""

#13. Števke
"""
n = int(input("Vpisi stevilko: "))

while n > 0:
    print(n % 10)
    n //= 10
"""

#14. Obrnjena stevila
"""
n = int(input("Vpisi stevilko: "))
m = 0
while n > 0:
    zadnja_stevka = n % 10
    m = m * 10 + zadnja_stevka
    n //= 10
print(m)
"""

#15. Kalkulator (funkcije)

#-------------
#Zanke prek seznamov in nizov
#-------------

#16. Vsota elementov seznama
"""
s = [5, 8, 3, 6, 0, 1]
print(sum(s))
"""

#17. Ajavost nizov
"""
niz = str(input("Vpisi niz: "))
print(niz.count("a"))
"""

#18. Najvecji element
"""
s = [5, 8, 3, 6, 0, 1]
print("Najvecji element: ", max(s))
"""

#19. Najvecji absolutist
"""
s = [5, 8, -45, 6, 0, 1]
nov_s = []
najvecji = 0
for n in s:
    if n < 0:
        nov_s.append(abs(n))
    else:
        nov_s.append(n)
print(max(nov_s))
"""

#20. Najmanjsi pozitivist
"""
s = [5, 8, -45, 6, 0, 1]
pozitivni = []
for n in s:
    if n > 0:
        pozitivni.append(n)
print(min(pozitivni))
"""

#21. Najdaljsa beseda
"""
niz = str(input("Vpisi niz: "))
besede = []
for beseda in niz.split(" "):
    besede.append(beseda)
print("Najdaljsa beseda v nizu je", max(besede))
"""

#22. Poprecje
"""
teze = [44.3, 22.5, 66.3, 90.5, 105.3, 75.2]
if len(teze) > 1:
    print(sum(teze) / len(teze))
else:
    print(0)
"""

#23. Poprecje brez skrajnezev
"""
teze = [44.3, 22.5, 66.3, 90.5, 105.3, 75.2]
if len(teze) > 1:
    teze.remove(max(teze))
    teze.remove(min(teze))
    print(sum(teze) / len(teze))
else:
    print(0)
"""

#24. Bomboni
"""
tabela = [5, 8, 6, 4]
vsota = 0
najvecje_stevilo = max(tabela)
for bonbon in tabela:
    vsota += najvecje_stevilo - bonbon
print(vsota)
"""

#25. Vsaj eno liho
"""
def vsaj_eno_liho(s):
    for n in s:
        if n % 2 == 1:
            return True
    return False

print(vsaj_eno_liho([2, 2, 2, 3]))
"""

#26. Sama liha
"""
def sama_liha(s):
    st = 0
    if not s:
        return True
    else:
        for n in s:
            if n % 2 == 1:
                st += 1

    if st == len(s):
        return True
    return False

print(sama_liha([2, 3, 3]))
"""

#27. Blagajna
"""
def blagajna(s):
    naj_vrsta = vrsta = 0
    for c in s:
        if c == "+":
            vrsta += 1
        if vrsta > naj_vrsta:
            naj_vrsta = vrsta
        else:
            vrsta -= 1
    return naj_vrsta


print(blagajna("+++++-----"))
"""

#28. Preobremenjeni colni
"""
def ni_preobremenjenih(tovori, nosilnost):
    skupna_vsota = 0
    for coln in tovori:
        if sum(coln) > nosilnost:
            return False
    return True

print(ni_preobremenjenih([[4, 5, 4], [10], [1, 1, 1]], 11))
"""
#-------------
# Zanke prek številskih intervalov
#-------------

#29. Delitelji
"""
n = int(input("Vpisi stevilo: "))
for i in range(1, n + 1):
    if n % i == 0:
        print(i)
"""

#30. Prastevilo
"""
def prastevilo(n):
    for i in range(2, n):
        if n % i == 0:
            return False
    return True
"""

#31. Vsota deliteljev
"""
def vsota_deliteljev(n):
    vsota = 0
    for i in range(1, n):
        if n % i == 0:
            vsota += i
    return vsota

print(vsota_deliteljev(12))
"""

#32. Popolno stevilo
"""
def popolno(n):
    vsota = 0
    for i in range(1, n):
        if n % i == 0:
            vsota += i

    if vsota == n:
        return True
    return False

#33. Vsa popolna stevila
for i in range(1, 1000):
    if popolno(i):
        print(i)
"""

#14.5.2026

#34. Prijateljska stevila
"""
def prijatelj(n):
    potencialni_prijatelj = 0
    for i in range(1, n):
        if n % i == 0:
            potencialni_prijatelj += i
    vsota_pot = 0

    for i in range(1, potencialni_prijatelj):
        if potencialni_prijatelj % i == 0:
            vsota_pot += i

    if vsota_pot == n:
        return potencialni_prijatelj
    else:
        return None
"""

#35. Vsebuje 7
"""
def vsebuje_7(n):
    if "7" in str(n):
        return True
    return False

#36. Postevanka stevila 7

def postevanka_7(n):
    for i in range(1, n + 1):
        if vsebuje_7(str(i)) or i % 7 == 0:
            print("BUM")
        else:
            print(i)

print(postevanka_7(29))
"""

#37. Fibonaccijevo zaporedje
"""
a = 1
b = 1
for i in range(20):
    print(a)
    a, b = b, a + b
"""

#38. Evklidov algoritem
"""
def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a

print(gcd(48, 18))
"""

#-------------
# Zanke prek več reči hkrati
#-------------

#39. Indeks telesne teže
"""
podatki = [
    ["Ana", 55, 165],
    ["Berta", 60, 153],
]

for ime, teza, visina in podatki:
    print(ime, teza / math.pow(visina/100, 2))
"""

#40. Seštete trojke
"""
def sestete_trojke(s):
    for el1, el2, pot_vsota in s:
        if el1 + el2 != pot_vsota:
            return False
    return True

print(sestete_trojke([(3, 5, 8), (2, 6, 8), (1, 1, 2), (10, 5, 15)]))
"""

#41. Skalarni produkt
"""
def skalarni(v, w):
    vsota = 0
    for i in range(len(v)):
        vsota += v[i] * w[i]
    return vsota

print(skalarni((1, 2, 3), (5, 4, 6)))
"""

#42. Ujemanja crk
"""
def st_ujemanj(b1, b2):
    n = 0
    for i in range(min(len(b1), len(b2))):
        if b1[i] == b2[i]:
            n += 1
    return n

print(st_ujemanj("PAV", "KRVAVICA"))

def st_ujemanj(b1, b2):
    n = 0
    for c1, c2 in zip(b1, b2):
        if c1 == c2:
            n += 1
    return n
"""

#43. Vzorec besede
"""
def se_ujema(beseda, vzorec):
    if len(beseda) != len(vzorec):
        return False

    for i in range(len(beseda)):
        if vzorec[i] != "." and vzorec[i] != beseda[i]:
            return False
    return True

print(se_ujema("MLEKO", "ML..O"))

#44 Prva beseda
def prva_beseda(besede, vzorec):
    for beseda in besede:
        if se_ujema(beseda, vzorec):
            return beseda
    return None


print(prva_beseda(["pes", "maca", "krava"], "p.s"))
"""

#45. Paralelni skoki
"""
def paralelni_skoki(skoki1, skoki2):
    tocke_1, tocke_2 = 0, 0
    for skok1, skok2 in zip(skoki1, skoki2):
        if skok1 > skok2:
            tocke_1 += 1
        elif skok1 < skok2:
            tocke_2 += 1
        else:
            tocke_1 += 0.5
            tocke_2 += 0.5
    if tocke_1 > tocke_2:
        return 1
    elif tocke_1 < tocke_2:
        return 2
    else:
        return None

print(paralelni_skoki([153, 141, 152, 160, 135], [148, 148, 148, 148, 148]))
"""

#46. Mesto največjega elementa
"""
def arg_max(s):
    if not s:
        return None
    
    najvec = 0
    naj_indeks = 0
    for indeks, num in enumerate(s):
        if num > najvec:
            najvec = num
            naj_indeks = indeks
    return naj_indeks

print(arg_max([5, 1, 4, 8, 2, 3, 8, 8, 8]))
"""

#47. Olimpijske medalje
"""
def napredek(s):
    napredovale = 0
    nazadovale = 0
    for indeks, number in enumerate(s, start=1):
        if indeks != number:
            if number > indeks:
                napredovale += 1
            elif number < indeks:
                nazadovale += 1
            else:
                continue
    return napredovale, nazadovale

print(napredek([1, 3, 2, 4, 6, 10, 7, 5, 9, 8]))
print(napredek([1, 2, 3, 4, 5]))
print(napredek([2, 1, 3]))
print(napredek([]))
print(napredek([5, 4, 3, 2, 1]))
"""

#48. Vstavi teže
"""
def vstavi_teze(osebe, teze):
    teze = teze.copy()  # da ne spremenimo izvirnega seznama tez
    i = 0
    j = 0
    while i < len(osebe):
        if not osebe[i].endswith("a"):
            osebe[i] = teze[j]
            j += 1
        i += 1

print(vstavi_teze(["Adam", "Eva", "Kajn", "Abel"], [87, 86, 75]))
"""
#49. Primerjanje seznamov
"""
def primerjaj(s, t):
    if s == t:
        return 0

    if len(s) == len(t):
        for el_s, el_t in zip(s, t):
            if el_s > el_t:
                return 1

    if len(s) == len(t):
        for el_s, el_t in zip(s, t):
            if el_s < el_t:
                return -1
    return 0

print(primerjaj([1, 2, 3, 4], [2, 3, 4, 5]))
print(primerjaj([2, 3, 4, 5], [1, 2, 0, 0]))
print(primerjaj([1, 2, 3], [4, 5, 6, 7]))
print(primerjaj([1, 0], [0, 1]))
"""

#INDEKSIRANJE, SEZNAMI, NIZI

#50. Spol in EMŠO
"""
def je_zenska(emso):
    return int(emso[9:12]) >= 500
"""

#51. Pravilnost EMŠO
"""
def preveri_emso(emso):
    print(emso)
    j = 7
    vsota = 0
    for i in range(len(emso) - 1):
        print(emso[i], j)
        vsota += int(emso[i]) * j
        if j == 2:
            j = 7
            continue
        j -= 1

    return (vsota + int(emso[-1])) % 11 == 0
    
    print(preveri_emso("0109005500399"))
"""

#52. Starost iz EMŠO
"""
def starost(emso):
    dan = int(emso[0:2])
    mesec = int(emso[2:4])
    lll = int(emso[4:7])

    if lll >= 500:
        leto = 1000 + lll
    else:
        leto = 2000 + lll

    danasnji_dan = 26
    danasnji_mesec = 1
    danasnje_leto = 2010

    starost = danasnje_leto - leto

    if mesec > danasnji_mesec:
        starost -= 1
    elif mesec == danasnji_mesec and dan > danasnji_dan:
        starost -= 1

    return starost
"""

#53. Domine
"""
def domine(s):
    for domina1, domina2 in pairwise(s):
        if domina1[1] != domina2[0]:
            return False
    return True

print(domine([(3, 6), (6, 6), (6, 1), (1,0)]))
print(domine([(3, 6), (6, 6), (2, 3)]))
"""

#54. Dan v letu
"""
def dan_v_letu(dan, mesec):
    dni_v_mesecu = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    return sum(dni_v_mesecu[:mesec - 1]) + dan

print(dan_v_letu(10, 2))
"""

#55. Nepadajoči seznam
"""
def nepadajoc(s):
    for pred, po in pairwise(s):
        if po < pred:
            return False
    return True

print(nepadajoc([1, 2, 1, 4, 5, 6]))
"""

#56. Mesta črke
"""
def mesta_crke(beseda, crka):
    mesta_crk = []
    for i, letter in enumerate(beseda):
        if letter == crka:
            mesta_crk.append(i)
    return mesta_crk


print(mesta_crke("PONUDNIK","N"))
"""

#57. Multiplikativni range
"""
def mrange(n, k, m):
    i = 1
    seznam = [n]
    while i <= m - 1:
        n *= k
        seznam.append(n)
        i += 1
    print(seznam)

print(mrange(7, 4, 5))
"""

#58. Sumljive besede
"""
def sumljive(niz):
    seznam_sumljivih = []
    for beseda in niz.split(" "):
        if "u" in beseda and "a" in beseda:
            seznam_sumljivih.append(beseda)
    return seznam_sumljivih


print(sumljive('Muha pa je rekla: "Tale juha se je pa res prilegla, najlepsa huala," in odletela.'))
"""

#59. Kockarji
"""
def kockarji(s, n):
    slovar_sest = defaultdict(int)
    n_deli = [(s[i:i+n]) for i in range(0, len(s), n)]
    for delcek in n_deli:
        for i, num in enumerate(delcek, start=1):
            if num == 6:
                slovar_sest[i] += 1
    if slovar_sest:
        return max(slovar_sest, key=slovar_sest.get)
    else:
        return None

print(kockarji([1, 2, 6, 1, 2, 6, 1, 6, 6, 1, 2, 1], 3))
print((kockarji([1, 6, 1, 6, 2, 2], 2)))
"""

#60. Križanka
"""
def prva_druga(beseda, vzorec):
    if len(beseda) != len(vzorec):
        return False

    for b, v in zip(beseda, vzorec):
        if b != v and v != ".":
            return False
    return True

def krizanka(vzorec, besede):
    seznam_ujemajocih = []
    for beseda in besede:
        if prva_druga(beseda, vzorec):
            seznam_ujemajocih.append(beseda)
    return seznam_ujemajocih

print(krizanka("r.k.", ["reka", "rokav", "robot", "roka"]))
"""

#15.5.2026
"""
def funkcija(n):
    stevec_lihih = 0
    for i in range(1, n + 1):
        if i % 2 == 0:
            print(i)
            continue
        stevec_lihih += 1
    print(stevec_lihih)

print(funkcija(10))
"""

#4. 8. 2026

#107 Izplačilo
"""
bankovci = {100: 8, 20: 7, 10: 4}

def izplacilo(bankovci, znesek):
    for bankovec in sorted(bankovci, reverse=True):
        while znesek >= bankovec and bankovci[bankovec] > 0:
            znesek -= bankovec
            bankovci[bankovec] -= 1
        if bankovci[bankovec] == 0:
            del bankovci[bankovec]

print(izplacilo(bankovci, 800))
print(bankovci)
"""

#108 Dopisovalci
"""
relacije = defaultdict(set)

def dopis(kdo, komu, relacije):
    relacije[kdo].add(komu)

dopis("Ana", "Berta", relacije)
dopis("Ana", "Cilka", relacije)
dopis("Ana", "Dani", relacije)
dopis("Berta", "Ana", relacije)
dopis("Berta", "Cilka", relacije)
dopis("Cilka", "Dani", relacije)

print(dict(relacije))

def najzgovornejsi(relacije):
    naj = -1
    ime = ""
    for name, dopisniki in relacije.items():
        st = len(dopisniki)
        if st > naj:
            naj = st
            ime = name
    return ime

print(najzgovornejsi(relacije))

def vse_osebe(relacije):
    mnozica_vseh = set()
    for ime, dopisniki in relacije.items():
            mnozica_vseh.add(ime) #ni potrebno preverjati ce so duplikati, ker ne morajo bit v mnozici
            mnozica_vseh.update(dopisniki) #pogosto dodajanje vecih elementov v npr. vrednostih pri kljucih lahko naredimo z union (namesto da vsakega posebej)
    return mnozica_vseh

def vse_osebe(relacije):
    return set(relacije) | set().union(*relacije.values())
    #set(relacije) doda vse kljuce
    #set().union(*relacije.values()) da unijo vseh vrednosti
    #| zdruzi oboje

def neznanci(ime, relacije):
    return vse_osebe(relacije) - relacije.get(ime, set()) #.get se uporablja takrat ko nismo sigurni ali kljuc obstaja, z njim dolocimo tudi kar lahko vrne!


print(vse_osebe(relacije))
print(neznanci("Dani", relacije))

"""

#109. Zaporniki
"""
zapor = [["ABC", "B", "BC", "E", "A"],
         ["C", "D", "AE", "DB", "DC"],
         ["BC", "AE", "E", "BC", "AED"]]

def sogovorniki(zapor):
    stevilo = 0
    for vrstica in zapor:
        for leva, desna in zip(vrstica, vrstica[1:]):
            if set(leva) & set(desna):
                stevilo += 1


    for zgornja, spodnja in zip(zapor, zapor[1:]):
        for gor, dol in zip(zgornja, spodnja):
            if set(gor) & set(dol):
                stevilo += 1

    return stevilo
"""

#110 Ograje
"""
s = ["AAABC", "ABCDC", "ACCDA"]

def ograje(s):
    n = len(s)
    m = len(s[0])
    maksimalna_dolzina = m * (n+1) + n * (m+1)

    for vrstica in s:
        for levo, desno in zip(vrstica, vrstica[1:]):
            if levo == desno:
                maksimalna_dolzina -= 1

    for vrstica1, vrstica2 in zip(s, s[1:]):
        for gor, dol in zip(vrstica1, vrstica2):
            if gor == dol:
                maksimalna_dolzina -= 1

    return maksimalna_dolzina

print(ograje(s))

"""
#111 Trgovanje
"""
ponudbe = [({"deska", "steklenica"}, {"pašteta"}),
({"knjiga", "vilice"}, {"sveča", "deska", "papir"}),
({"riba", "pašteta"}, {"tipkovnica", "zaslon"})]

def obstaja(dam, dobim, ponudbe):
    for ponudba in ponudbe:
        dati, dobiti = ponudba[0], ponudba[1]
        if dam in dati and dobim in dobiti:
            return True
    return False

def obstaja(dam, dobim, ponudbe):
    for dati, dobiti in ponudbe:
        if dam in dati and dobim in dobiti:
            return True
    return False

def menjave(zaporedje_stvari, ponudbe):
    for stvar1, stvar2 in zip(zaporedje_stvari, zaporedje_stvari[1:]):
        print(stvar1, stvar2)
        if not obstaja(stvar1, stvar2, ponudbe):
            return False
    return True

print(obstaja("sveča", "knjiga", ponudbe))
print(menjave(["deska", "pašteta", "zaslon"], ponudbe))
print(menjave(["vilice", "papir", "pašteta", "tipkovnica"], ponudbe))
"""

#112 Ne na lihih
"""
def ne_na_lihih(s):
    mnozica_sodih = set()
    mnozica_lihih = set()
    for i, x in enumerate(s):
        if i % 2 == 0:
            mnozica_sodih.add(x)
        else:
            mnozica_lihih.add(x)
    return mnozica_sodih - mnozica_lihih

print(ne_na_lihih([12, 17, 17, 5, 3]))
"""

#113 Sopomenke
"""
sopomenke = [{"fant", "deček", "pob"}, {"cesta", "pot", "kolovoz", "makadam"}, {"kis", "jesih"}]

def predelaj(stavek, sopomenke):
    rezultat = []
    s = stavek.split(" ")
    for beseda in s:
        dodaj = beseda  # privzeto: dodaj original
        for besede in sopomenke:
            if beseda in besede:
                dodaj = random.choice(list(besede))
                break  # našel — ne rabim več iskati
        rezultat.append(dodaj)

    return " ".join(rezultat)


print(predelaj("fant in dekle sta vzela pot pod noge", sopomenke))
"""

#114 Stavka z istim pomenom
"""
sopomenke = [{"fant", "deček", "pob"}, {"cesta", "pot", "kolovoz", "makadam"}, {"kis", "jesih"}, {"dekle", "punca"}, {"noge", "tace"}]

def sta_sopomenki(b1, b2, sopomenke):
    if b1 == b2:
        return True
    for besede in sopomenke:
            if b1 in besede and b2 in besede:
                return True
    return False

def sopomena(stavek1, stavek2, sopomenke):
    for beseda1, beseda2 in zip(stavek1.split(" "), stavek2.split(" ")):
        if not sta_sopomenki(beseda1, beseda2, sopomenke):
            return False
    return True

print(sta_sopomenki("fant", "cesta", sopomenke))
print(sopomena("fant in dekle sta vzela pot pod noge","pob in punca sta vzela kolovoz pod tace", sopomenke))
"""

#115 Združi - razmeči
"""
def zdruzi(s):
    slovar = dict()
    for i, x in enumerate(s):
        if x not in slovar:
            slovar[x] = set()
        slovar[x].add(i)
    print(slovar)

def zdruzi(s):
    slovar = defaultdict(set)
    for i, x in enumerate(s):
        slovar[x].add(i)
    return dict(slovar)

def razmeci(s):
    velikost = len(set().union(*s.values()))
    seznam = [None] * velikost

    for vrednost, indeksi in s.items():
        for indeks in indeksi:
            seznam[indeks] = vrednost
    print(seznam)

print(zdruzi([3, 1, 12, 3, 7, 12]))
print(razmeci({3: {0, 3}, 1: {1}, 12: {2, 5}, 7: {4}}))
"""

#116 Podarjanje daril
"""
def dolzina_poti(s, o):
    slovar = dict(s)
    stevec = 0
    trenutna = o
    while trenutna in slovar:
        trenutna = slovar[trenutna]
        stevec += 1
    return stevec
    
print(dolzina_poti([(8, 2), (1, 8), (5, 1), (4, 42)], 5))
"""

#117 Požrešneži
"""
def ne_daje_naprej(s):
    slovar = dict(s)
    return set(slovar.values()) - set(slovar)

print(ne_daje_naprej([(3, 1), (8, 2), (1, 8), (4, 5)]))
"""

#118 Ne maram
"""
vrsta = ["Ana", "Berta", "Cilka", "Dani", "Ema"]
prepovedani = [("Ana", "Cilka"), ("Berta", "Ana"), ("Berta", "Dani")]

def preveri_vrsto(vrsta, prepovedani):
    vsi_pari = zip(vrsta, vrsta[1:])
    for par in vsi_pari:
        if par in prepovedani or par[::-1] in prepovedani:
            return False
    return True

print(preveri_vrsto(vrsta, prepovedani))

def preveri_vrsto(vrsta, prepovedani):
    prepovedani_set = {frozenset(par) for par in prepovedani}
    for par in zip(vrsta, vrsta[1:]):
        if frozenset(par) in prepovedani_set:
            return False
    return True
"""

#119 Najmnajši unikat
"""
def najmanjsi_unikat(s):
    ostevilceno = Counter(s)
    samo_enkrat = set()
    for kljuc, st in ostevilceno.items():
        if st == 1:
            samo_enkrat.add(kljuc)
    return min(samo_enkrat, default=None)

print(najmanjsi_unikat([3, 1, 4, 1, 5, 9, 2, 6, 5, 3]))   # → 2)
"""
#5. 8. 2026

#120 Bingo
"""
def bingo(listki, vrstni_red):
    najboljsi_listek = None
    najmanjsi_korak = len(vrstni_red)
    for listek in listki:
        korak = max(vrstni_red.index(cifra) for cifra in listek) #dobimo najvecji indeks cifre na listku
        if korak < najmanjsi_korak:
            najmanjsi_korak = korak
            najboljsi_listek = listek
    return najboljsi_listek


print(bingo([[4, 1, 2, 3, 5], [6, 1, 2, 3, 4], [7, 6, 4, 3, 2]],[4, 2, 8, 3, 1, 6, 5, 7]))
"""

#121 Trki besed
"""
def skrij(beseda):
    return beseda

def trk(besede):
    slovar = dict() #kljuc je pretvorjena, vrednost je original
    for original in besede:
        pretvorjena = skrij(original)
        if pretvorjena in slovar:
            return (slovar[pretvorjena], original)
        slovar[pretvorjena] = original
"""

#Rekurzija

rodovnik = {'Ulrik I.': ['Viljem'], 'Margareta': [],
'Herman I.': ['Herman II.', 'Hans'], 'Elizabeta II.': [],
'Viljem': ['Ana Poljska'], 'Elizabeta I.': [], 'Ana Poljska': [],
'Herman III.': ['Margareta'], 'Ana Ortenburška': [],
'Barbara': [], 'Herman IV.': [], 'Katarina': [], 'Friderik III.': [],
'Herman II.': ['Ludvik', 'Friderik II.', 'Herman III.',
'Elizabeta I.', 'Barbara'],
'Ulrik II.': ['Herman IV.', 'Jurij', 'Elizabeta II.'],
'Hans': [], 'Ludvik': [], 'Jurij': [],
'Friderik I.': ['Ulrik I.', 'Katarina', 'Herman I.',
'Ana Ortenburška'],
'Friderik II.': ['Friderik III.', 'Ulrik II.'] }

#122 Preštej vnuke
"""
def prestej_vnuke(oseba):
    st = 0
    for otrok in rodovnik[oseba]: #otroci od osebe npr. otroci od Ulrika I. je le Viljem
        st += len(rodovnik[otrok]) #stevcu pristejemo se dolzino otrok od otroka, torej stevilo otrok Viljema (1 - Ana Poljska)
    return st

print(prestej_vnuke("Friderik I."))
"""

#123 Poišči rojaka
"""
def poisci_rojaka(oseba, ime):
    if oseba == ime:
        return True
    for otrok in rodovnik[oseba]:
        if poisci_rojaka(otrok, ime):
            return True
    return False

print(poisci_rojaka("Friderik I.", "Barbara"))
"""

#124 Poišči potomca
"""
def poisci_potomca(oseba, ime):
    otroci = rodovnik[oseba]
    if ime in otroci:
        return True
    for otrok in otroci:
        if poisci_potomca(otrok, ime):
            return True
    return False
"""

#125 Preštej rodbino
"""
def prestej_rodbino(oseba):
    stevilo = 1
    for otrok in rodovnik[oseba]:
        stevilo += prestej_rodbino(otrok)
    return stevilo

print(prestej_rodbino("Ulrik I."))
"""

#126 Preštej potomce
"""
def prestej_potomce(oseba):
    otroci = rodovnik[oseba]
    potomcev = len(otroci)
    for otrok in otroci:
        potomcev += prestej_potomce(otrok)
    return potomcev

print(prestej_potomce("Ulrik I."))
"""

#127 Najdaljše ime v rodbini
"""
def najdaljse_ime(oseba):
    najdaljse = oseba
    otroci = rodovnik[oseba]
    for otrok in otroci:
        kandidat = najdaljse_ime(oseba)
        if len(kandidat) > len(najdaljse):
            najdaljse = kandidat
    return najdaljse
"""

#18. 8. 2026

#128. Globina rodbine
"""
def globina(oseba):
    if rodovnik[oseba] == []:
        return 1

    globine = []
    for otrok in rodovnik[oseba]:
        globine.append(globina(otrok))

    return max(globine) + 1

print(globina("Hans"))
print(globina('Ulrik II.'))
print(globina('Friderik I.'))
"""

#129. Kolikokrat ime
"""
def kolikokrat_ime(oseba, ime):
    stevec = 0
    if oseba.split()[0] == ime:
        stevec += 1

    for otrok in rodovnik[oseba]:
        stevec += kolikokrat_ime(otrok, ime)

    return stevec

print(kolikokrat_ime('Friderik I.', 'Friderik'))
"""

#130. Koliko žensk
"""
def zensk_v_rodbini(oseba):
    stevec = 0
    if oseba.split()[0][-1] == "a":
        stevec += 1

    for otrok in rodovnik[oseba]:
        stevec += zensk_v_rodbini(otrok)

    return stevec

print(zensk_v_rodbini('Friderik I.'))
"""


#131. Naštej rodbino
"""
def vsa_rodbina(oseba):
    if rodovnik[oseba] == []:
        return set([oseba])

    rodbina = set([oseba])
    for otrok in rodovnik[oseba]:
        rodbina |= vsa_rodbina(otrok)

    return rodbina

print(vsa_rodbina('Ulrik II.'))
"""

#132. Naštej potomce
"""
def vse_potomstvo(oseba):
    if rodovnik[oseba] == []:
        return set()

    potomci = set(rodovnik[oseba])
    for otrok in rodovnik[oseba]:
        potomci |= vse_potomstvo(otrok)

    return potomci

print(vse_potomstvo("Ulrik II."))

def vse_potomstvo(oseba):
    return vsa_rodbina(oseba) - {oseba}
"""

#133. Največ otrok
"""
def najvec_otrok(oseba):
    if rodovnik[oseba] == []:
        return 0

    najvec = len(rodovnik[oseba])
    for otrok in rodovnik[oseba]:
        if najvec_otrok(otrok) > najvec:
            najvec = najvec_otrok(otrok)

    return najvec

print(najvec_otrok('Friderik I.'))
print(najvec_otrok('Ulrik II.'))
"""

#134. Največ vnukov
"""
def vnukov(oseba):
    otroci = rodovnik[oseba]
    st_vnukov = 0
    for otrok in otroci:
        st_vnukov += len(rodovnik[otrok])
    return st_vnukov

def najvec_vnukov(oseba):
    if vnukov(oseba) == 0:
        return 0

    najvec = vnukov(oseba)
    for otrok in rodovnik[oseba]:
        naj_vnukov = najvec_vnukov(otrok)
        if naj_vnukov > najvec:
            najvec = naj_vnukov

    return najvec

print(najvec_vnukov("Friderik I."))
"""

#135. Največ sester
"""
def sester_pod(ime, rodovnik):
    otroci = rodovnik[ime]
    hcere = [otrok for otrok in otroci if otrok.split(" ")[0].endswith("a")]
    st_hcera = len(hcere)

    if st_hcera == 0:
        return 0
    elif st_hcera == len(otroci):
        return st_hcera - 1
    else:
        return st_hcera

def najvec_sester(oseba):
    najvec = sester_pod(oseba, rodovnik)
    for otrok in rodovnik[oseba]:
        otrokovih = najvec_sester(otrok)
        if otrokovih > najvec:
            najvec = otrokovih
    return najvec
"""

#136. Najplodovitejši
"""
def najvec_otrok_kdo(oseba):
    if rodovnik[oseba] == []:
        return 0, oseba

    najvec = len(rodovnik[oseba]), oseba
    for otrok in rodovnik[oseba]:
        rezultat_otroka = najvec_otrok_kdo(otrok)
        if rezultat_otroka[0] > najvec[0]:
            najvec = rezultat_otroka

    return najvec

print(najvec_otrok_kdo('Friderik I.'))
print(najvec_otrok_kdo('Ulrik II.'))
"""

#167. Stopnice
"""
def kako_visoko(stopnice):
    if stopnice[0] > 20:
        return 0
    for prejsna, naslednja in zip(stopnice, stopnice[1:]):
        if naslednja - prejsna > 20:
            return prejsna
    return stopnice[-1]

print(kako_visoko([10, 20, 30, 40, 45]))
"""

#168 Drugi najvecji element
"""
def drugi_najvecji(s):
    brez_duplikatov = []
    for x in s:
        if x not in brez_duplikatov:
            brez_duplikatov.append(x)
    return sorted(brez_duplikatov)[-2]

print(drugi_najvecji([5, 1, 4, 8, 2, 3, 8]))
"""

#169. Collatz 2
"""
def collatz(n):
    dolzina = 1
    while n != 1:
        if n % 2 == 0:
            n //= 2
        else:
            n = 3*n + 1
        dolzina += 1
    return dolzina

def arg_max_collatz():
    najvec = 1
    naj_stevilo = 1
    for i in range(1, 100000):
        dolzina = collatz(i)
        if dolzina > najvec:
            najvec = dolzina
            naj_stevilo = i
    return naj_stevilo, najvec


print(arg_max_collatz())
"""

#170. Delnice
"""
delnica = [1, -2, -4, 1, 2, -1, 3, 4, -2, 1, -5, -5]
def posrednik(s):
    naj_dobicek = -1
    for od in range(12):
        for do in range(od, 12):
            dobicek = sum(delnica[od:do])
            if dobicek > naj_dobicek:
                naj_dobicek = dobicek
                naj_od, naj_do = od, do
    return naj_od, naj_do
"""

#171. Spremembe smeri
"""
def spremebe_smeri(s):
    seznam = []
    for prej, potem in zip(s, s[1:]):
        if potem > prej:
            seznam.append(True)
        elif prej > potem:
            seznam.append(False)

    stevilo_sprememb = 0
    for x in zip(seznam, seznam[1:]):
        if x[0] != x[1]:
            stevilo_sprememb += 1

print(spremebe_smeri([1, 2, 3, 0, -1]))
"""

#172. Sekajoči se krogi
"""
#krog -> (x, y, r) -> (1, 2, 5)
def sekajo(krogi):
    for i, (x1, y1, r1) in enumerate(krogi):
        for j, (x2, y2, r2) in enumerate(krogi):
            if i != j and math.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2) <= r1 + r2:
                return True
    return False
"""

#173. Največ n-krat
"""
def najvec_n(s, n): #z novim seznamom
    seznam = []
    for x in s:
        if seznam.count(x) < n:
            seznam.append(x)
    print(seznam)

def najvec_n(s, n):
    kopija = s.copy()          # ali list(s)
    for x in kopija:
        if s.count(x) > n:
            s.remove(x)
    return s
    
print(najvec_n([1, 2, 3, 1, 1, 2, 1, 2, 3, 3, 2, 4, 5, 3, 1], 3))
"""

#6. 8. 2026

#174. Brez n-tih
"""
cc = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
def brez_ntih(s, n):
    for i in range(len(s) - 1, -1, -1):
        if (i + 1) % n == 0:      # 1-indeksirano: 3, 6, 9, ...
            del s[i]
brez_ntih(cc, 3)
print(cc)
"""

#175. Vse črkež
"""
def vse_crke(beseda, crke):
    return set(beseda) <= crke

print(vse_crke("AMFITEATER", set(["A", "M"])))
print(vse_crke("AMFITEATER", set(["A", "M", "F", "I", "T", "E"])))
print(vse_crke("AMFITEATER", set(["A", "M", "F", "I", "T", "E", "R"])))
print(vse_crke("AMFITEATER", set(["A", "M", "F", "I", "T", "E", "R", "X", "O", "B", "L"])))
"""
#176. Skritopis
"""
def skritopis(s):
    v_besedi = False
    rezultat = []
    for char in s:
        if char.isalpha() and v_besedi is False:
            rezultat.append(char)
            v_besedi = True
        elif char.isalpha() and v_besedi is True:
            continue
        elif not char.isalpha():
            rezultat.append(char)
            v_besedi = False
    return "".join(rezultat)
    
print(skritopis("Napiši funkcijo skritopis(s), ki (kar predobro) skrije besedilo tako, da vsako besedo zamenja z njeno prvo črko."))
"""

#177. Igra z besedami
"""
def skrij(beseda):
    po_abecedi = sorted(beseda)
    nova_beseda = "".join(po_abecedi)
    slovar = Counter(nova_beseda)
    rezultat = ""
    for crka, stevilo in slovar.items():
        vzorec = crka + str(stevilo)
        rezultat += vzorec
    return rezultat

print(skrij("HANA"))
"""

#178. Srečanje čebel
"""
def srecanje(vrt):
    skupen_cas = 0
    for cvet in vrt:
        skupen_cas += (cvet + 1)
    polovica = skupen_cas / 2
    preostalo = polovica

    for i, cvet in enumerate(vrt):
        cas_cveta = cvet + 1
        if preostalo < cas_cveta:
            return i
        preostalo -= cas_cveta

print(srecanje([1, 4, 1, 2, 8, 3]))
"""

#179. Odvečni presledki
"""
def prepresledki(s):
    skupine_skupaj = 0
    podaljsane = 0
    dolzina_trenutne_skupine = 0

    for char in s:
        if char == " ":
            dolzina_trenutne_skupine += 1
        else:
            if dolzina_trenutne_skupine >= 1:
                skupine_skupaj += 1
                if dolzina_trenutne_skupine >= 2:
                    podaljsane += 1
                dolzina_trenutne_skupine = 0

    if dolzina_trenutne_skupine >= 1:
        skupine_skupaj += 1
        if dolzina_trenutne_skupine >= 2:
            podaljsane += 1

    if skupine_skupaj == 0:
        return 0.0
    return podaljsane / skupine_skupaj

print(prepresledki("Tule je    samo en preveč."))
"""

#180. Kričiš
"""
def kricis(s):
    for prvi, drugi in zip(s, s[1:]):
        if prvi.isupper() and drugi.isupper():
            return True
    return False

print(kricis("mojlam"))
"""

#181. Napadalne kraljice
#to-do

#182. Obljudeni stolpci
#to-do

#183. Banka
"""
def klienti(transakcije):
    seznam_imen = []
    for ime, denar in transakcije:
        if ime not in seznam_imen:
            seznam_imen.append(ime)
    return seznam_imen

print(klienti([("Ana", 2), ("Berta", 8), ("Ana", 4), ("Berta", -3)]))
"""

"""
def bilanca(transakcije, ime):
    skupno = 0
    for oseba, denar in transakcije:
        if ime == oseba:
            skupno += denar
    return skupno

print(bilanca([("Ana", 2), ("Berta", 8), ("Ana", 4), ("Berta", -3)], "Berta"))
"""

"""
def najbogatejsi(transakcije):
    imena = klienti(transakcije)
    najbogatejsa_oseba = imena[0]
    najvec = bilanca(transakcije, najbogatejsa_oseba)
    for ime in imena[1:]:
        stanje = bilanca(transakcije, ime)
        if stanje > najvec:
            najvec = stanje
            najbogatejsa_oseba = ime
    return najbogatejsa_oseba

print(najbogatejsi([("Ana", 2), ("Berta", 8), ("Ana", 4), ("Berta", -3)]))
"""

"""
def racunovodja(transakcije):
    rezultat = []
    for ime in klienti(transakcije):
        rezultat.append([ime, bilanca(transakcije, ime)])
    return rezultat
print(racunovodja([("Ana", 2), ("Berta", 8), ("Ana", 4), ("Berta", -3)]))
"""

#184. Srečni gostje
"""
def je_zenska(emso):
    stevilka = str(emso[9]) + str(emso[10]) + str(emso[11])
    return 500 <= int(stevilka) <= 999
"""
"""

def stevilo_srecnezev(razpored):
    n = len(razpored)
    srecni = 0
    for i in range(n):
        levi = (i - 1) % n
        desni = (i + 1) % n
        spol_gosta = je_zenska(razpored[i])
        levi_sosed = je_zenska(razpored[levi])
        desni_sosed = je_zenska(razpored[desni])
        if levi_sosed != spol_gosta and desni_sosed != spol_gosta:
            srecni += 1
    return srecni
"""

#7. 8. 2026
#185. Gostoljubni gostitelji
"""
def razporedi(gosti):
    moska_kolona = []
    zenska_kolona = []
    najsrecnejsi = []
    for gost in gosti:
        if je_zenska(gost):
            zenska_kolona.append(gost)
        else:
            moska_kolona.append(gost)

    for moski, zenska in zip(moska_kolona, zenska_kolona):
        najsrecnejsi.append(moski)
        najsrecnejsi.append(zenska)

    najsrecnejsi.extend(moska_kolona[len(zenska_kolona):])
    najsrecnejsi.extend(zenska_kolona[len(moska_kolona):])

    return najsrecnejsi

print(razporedi(['0505913509174', '2202973506004', '0304943506069', '2702943501809',
'2407980508463', '0209965503761', '2109913502875', '1802924506701',
'0207970500808', '1501917509568']))
"""

#186. Po starosti
"""
def datum_rojstva(emso):

    dan = int(emso[0:2])
    mesec = int(emso[2:4])
    leto_kratko = int(emso[4:7])
    if leto_kratko >= 800:
        leto = 1000 + leto_kratko
    else:
        leto = 2000 + leto_kratko
        
    return date(leto, mesec, dan)

def po_starosti(s):
    pari = []
    rezultat = []
    for ime, emso in s:
        pari.append((datum_rojstva(emso), ime))
    pari.sort()

    for datum, ime in pari:
        rezultat.append(ime)
        
    return rezultat
    
print(po_starosti([("Ana", "2401983505012"), ("Berta", "1509980505132"), ("Cilka", "0203001505333"), ("Dani", "1005983505333")]))
"""

#187. Ujeme
"""
def ujeme(b1, b2):
    niz = ""
    if len(b1) > len(b2):
        daljsa = b1
        krajsa = b2
    elif len(b2) > len(b1):
        daljsa = b2
        krajsa = b1
    else:
        daljsa = b1
        krajsa = b2

    i = 0
    while i < len(krajsa):
        if krajsa[i] == daljsa[i]:
            niz += krajsa[i]
        else:
            niz += "."
        i += 1

    print(niz)

print(ujeme("CELINKE", "POLOVINKE"))
"""

#188. Najboljše prilagajanje podniza
"""
def st_ujemanj(a, b):
    stevilo = 0
    for x, y in zip(a, b):
        if x == y:
            stevilo += 1
    return stevilo


def naj_prileg(s, sub):
    najboljsi_indeks = 0
    najboljsi_stevilo = -1
    najboljsi_podniz = ""

    for i in range(len(s) - len(sub) + 1):
        podniz = s[i:i + len(sub)]
        ujemanj = st_ujemanj(podniz, sub)
        if ujemanj > najboljsi_stevilo:
            najboljsi_stevilo = ujemanj
            najboljsi_indeks = i
            najboljsi_podniz = podniz

    return (najboljsi_indeks, najboljsi_stevilo, najboljsi_podniz)

print(naj_prileg("Poet tvoj nov Slovencem venec vije", "vine"))
"""

#189. Deljenje nizov
"""
def deli_niz(s, k):
    if len(s) % k != 0:
        return None
    dolzina_vzorca = len(s) // k
    vzorec = s[:dolzina_vzorca]
    if vzorec * k == s:
        return vzorec
    return None

print(deli_niz('toktoktoktok', 4))
print(deli_niz('tktktktk', 2))
print(deli_niz('XXX', 3))
print(deli_niz('toktoktoktok', 3))
print(deli_niz('tiktoktak', 3))
"""

#190. Bralca bratca
"""
def razdeli_knjige(debeline):
    skupno = sum(debeline)
    najboljsa_razlika = skupno  # največja možna
    najboljsi_i = 0
    peter_debelina = 0

    for i in range(len(debeline) + 1):
        pavel_debelina = skupno - peter_debelina
        razlika = abs(peter_debelina - pavel_debelina)
        if razlika < najboljsa_razlika:
            najboljsa_razlika = razlika
            najboljsi_i = i
        if i < len(debeline):
            peter_debelina += debeline[i]

    return najboljsi_i, len(debeline) - najboljsi_i

#print(razdeli_knjige([500, 100, 100, 100, 900]))
#print(razdeli_knjige([500, 100, 100, 100, 900, 100]))
#print(razdeli_knjige([50, 86, 250, 13, 205, 85]))
print(razdeli_knjige([50, 86, 150, 13, 205, 85]))
"""

#191. Turnir Evenzero
"""
def turnir(s):
    while len(s) > 1:
        novi = []
        for par in zip(s[::2], s[1::2]):
            if (len(par[0]) + len(par[1])) % 2 == 0:
                novi.append(par[0])
            else:
                novi.append(par[1])
        s = novi
    return s[0]

print(turnir(['Alice', 'Bob', 'Tom', 'Judy']))
"""

"""
#192. Najdaljše nepadajoče zaporedje
def najdaljse_nepadajoce(s):
    if not s:
        return 0
    
    najdaljsa = 1
    trenutna = 1
    for prej, naslednji in zip(s, s[1:]):
        if naslednji >= prej:
            trenutna += 1
        else:
            if trenutna > najdaljsa:
                najdaljsa = trenutna
            trenutna = 1
            
    if trenutna > najdaljsa:
        najdaljsa = trenutna
    return najdaljsa
"""

#193. Seznam vsot seznamov
"""
def vsota_seznamov(s):
    nov_seznam = []
    for seznam in s:
        nov_seznam.append(sum(seznam))
    return nov_seznam

print(vsota_seznamov([[2, 4, 1], [3, 1], [], [8, 2], [1, 1, 1, 1]]))

def najvecja_vsota(s):
    seznam_vsot = vsota_seznamov(s)
    naj = 0
    naj_indeks = 0
    for i, vsota in enumerate(seznam_vsot):
        if vsota > naj:
            naj = vsota
            naj_indeks = i
    return s[naj_indeks]

print(najvecja_vsota([[2, 4, 1], [3, 1], [], [8, 2], [1, 1, 1, 1]]))
"""

#194. Veliko, a ne več kot
"""
def naj_pod(s, n):
    najvec = 0
    naj_zacetek = 0
    naj_konec = 0
    for zacetek in range(len(s)):
        for konec in range(zacetek + 1, len(s) + 1):
            podseznam = s[zacetek:konec]
            vsota = sum(podseznam)
            if n >= vsota > najvec:
                najvec = vsota
                naj_zacetek = zacetek
                naj_konec = konec
    return s[naj_zacetek:naj_konec]

print(naj_pod([2, 1, 5, 6, 11, 2, 3, 6], 16))
"""

#195. Nepadajoči podseznami
"""
def nepadajoci(s):
    if not s:
        return []
    
    rezultat = []
    trenutni = [s[0]]           
    for prej, potem in zip(s, s[1:]):
        if potem >= prej:
            trenutni.append(potem)   
        else:
            rezultat.append(trenutni)
            trenutni = [potem]        
    rezultat.append(trenutni)         
    return rezultat

print(nepadajoci([2, 5, 7, 8, 4, 6, 9, 14, 7, 8, 3, 2, 5, 6]))
"""

#196. Sodi vs. lihi
"""
def sodi_vs_lihi(s):
    sodi = []
    lihi = []
    for x in s:
        if x % 2 == 0:
            sodi.append(x)
        elif x % 2 == 1:
            lihi.append(x)

    if len(sodi) > len(lihi):
        return sodi
    elif len(sodi) == len(lihi):
        return sodi
    return lihi

print(sodi_vs_lihi(([])))
"""

#27-08-2026
#181. Napadalne kraljice
"""

def stolpec_prost(stolpec, razpored):
    for x, y in razpored:
        for s in stolpec:
            if s == x:
                return False
    return True

def prosti_stolpci(razpored):
    vsi_stolpci = {chr(char) for char in range(int(ord("a")), int(ord("i")))}
    razpored_stolpci = {coord[0] for coord in razpored}
    return vsi_stolpci - razpored_stolpci

def prost_stolpec(razpored):
    vsi_stolpci = [chr(char) for char in range(int(ord("a")), int(ord("i")))]
    kraljice_stolpci = [coord[0] for coord in razpored]

    for stolpec in vsi_stolpci:
        if stolpec not in kraljice_stolpci:
            return stolpec
    return None

def napada(polje1, polje2):
    x1 = ord(polje1[0]) - ord("a") + 1
    y1 = int(polje1[1])
    x2 = ord(polje2[0]) - ord("a") + 1
    y2 = int(polje2[1])

    return x1 == x2 or y1 == y2 or abs(x1 - x2) == abs(y1 - y2)

def napadajo(polje, razpored):
    seznam_napadajocih = []
    for kraljica in razpored:
        if napada(polje, kraljica):
            seznam_napadajocih.append(kraljica)
    return seznam_napadajocih

def napadeno(polje, razpored):
    for kraljica in razpored:
        if napada(polje, kraljica):
            return True
    return False

def prosto_v_stolpcu(stolpec, razpored):
    vsa_polja = {"".join((stolpec, str(y))) for y in range(1, 9)}
    napadeni = set()
    for polje in vsa_polja:
        for razp in razpored:
            if napada(polje, razp):
                napadeni.add(polje)
    nenapadeni = list(vsa_polja - napadeni)
    return nenapadeni

def prosto_v_stolpcu(stolpec, razpored):
    vsa_polja = {"".join((stolpec, str(y))) for y in range(1, 9)}
    nenapadeni = []
    for polje in vsa_polja:
        if not napadeno(polje, razpored):
            nenapadeni.append(polje)
    return nenapadeni

def napadajoce_se(razpored):
    napdajoce_mnozica = set()
    pari = combinations(razpored,2 )
    for p1, p2 in pari:
        if napada(p1, p2):
            napdajoce_mnozica.add((p1, p2))
    return napdajoce_mnozica

def legalen(razpored):
    if len(razpored) == 8 and not napadajoce_se(razpored):
        return True
    return False
"""

#204. Legalni konj
"""
def legalni_skoki(koordinate):
    x = ord(koordinate[0]) - ord("a") + 1
    y = int(koordinate[1])

    premiki = [(2, 1), (2, -1), (-2, 1), (-2, -1),
               (1, 2), (1, -2), (-1, 2), (-1, -2)]

    seznam_dosegljivih = []
    for dx, dy in premiki:
        nov_x = x + dx
        nov_y = y + dy
        if 1 <= nov_x <= 8 and 1 <= nov_y <= 8:
            novo_polje = chr(nov_x - 1 + ord("a")) + str(nov_y)
            seznam_dosegljivih.append(novo_polje)

    return seznam_dosegljivih
"""

#219. Slovar anagramov
"""
def slovar_anagramov(besede):
    slovar = defaultdict(set)
    for beseda in besede:
        slovar["".join(sorted(beseda))].add(beseda)
    return slovar

def anagrami(beseda, s):
    mnozica_anagramov = set()
    for crke, besede in s.items():
        if sorted(crke) == sorted(beseda):
            mnozica_anagramov |= besede
    return mnozica_anagramov
"""

#240. Vse datoeke s končnico .py
"""
pot = "C:\\Users\\Luka\\PycharmProjects\\PythonProject\\naloge_iz_programiranja"
for item in os.listdir(pot):
    if item.endswith(".py"):
        print(item)

def vse_py(pot):
    seznam = []
    for item in os.listdir(pot):
        polna_pot = os.path.join(pot, item)
        if os.path.isdir(polna_pot):
            seznam.extend(vse_py(polna_pot))
        elif os.path.isfile(polna_pot) and polna_pot.endswith(".py"):
            seznam.append(polna_pot)
    return seznam

pot = "C:\\Users\\Luka\\PycharmProjects\\PythonProject\\naloge_iz_programiranja"
print(vse_py(pot))
"""

#205. Skoki
"""
def skoki(s):
    st_skokov = 0
    trenutno = 0
    while st_skokov <= len(s):
        trenutno = s[trenutno]
        st_skokov += 1

        if trenutno == 0:
            return st_skokov
    return -2

s = [3, 4, 0, 4, 2, 3]
print(skoki(s))
"""

