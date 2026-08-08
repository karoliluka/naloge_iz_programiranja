import math
import random
from math import *
from time import *

#Pretvarjanje temperatur
"""
temp_F = float(input("Temperature [F]? "))
temp_C = (temp_F - 32) * 5/9
temp_K = temp_C + 273.15
print(temp_F, "F je enako",temp_K, "K ali",  temp_C, "C")
"""

#Krog
"""
r = float(input("Polmer kroga?"))
print("Obseg kroga:", 2 * math.pi * r)
print("Površina kroga:", math.pi * pow(r, 2))
"""

#Pitagorov izrek
"""
k1 = float(input("Kateta?"))
k2 = float(input("Kateta?"))
print("Hipotenuza:", math.sqrt(pow(k1, 2) + pow(k2, 2)))
"""

#Vodnjak
"""
cas = int(input("Čas [s]?"))
print("Globina vodnjaka:", 0.5 * 9.81 * pow(cas, 2), "m")
"""

#Indeks telesne teže
"""
visina = float(input("Višina [cm]?"))
masa = float(input("Masa [kg]?"))
print("Indeks telesne mase:", masa / pow((visina / 100), 2))
"""

#Povprečna ocena
"""
ana = float(input("Ocena [Ana]?"))
berta = float(input("Ocena [Berta]?"))
cilka = float(input("Ocena [Cilka]?"))
print("Povprečje", (ana + berta + cilka) / 3)
print("Srednja vrednost:", ana + berta + cilka - min(ana, berta, cilka) - max(ana, berta, cilka))
"""

#Površina trikotnika
"""
a = float(input("Dolžina stranice a?"))
b = float(input("Dolžina stranice b?"))
c = float(input("Dolžina stranice c?"))
s = (a + b + c) / 2
ploscina = sqrt(s * (s - a) * (s - b) * (s - c))
r_vcrtan = ploscina / s
r_ocrtan = (a * b * c) / (4 *  ploscina)
print("Površina trikotnika", ploscina)
print("Površina včrtanega kroga", math.pi * pow(r_vcrtan, 2))
print("Površina očrtanega kroga", math.pi * pow(r_ocrtan, 2))
"""

#Hitri prsti
"""
cas_pred = time()
odg = int(input("Koliko je 6 krat 7?"))
cas_po = time()
print("Za razmisljanje si porabil", cas_po - cas_pred, "s.")
"""

#Misleči stroj - razlicica 1
"""
x = float(input("Prvo število?"))
y = float(input("Drugo število?"))
sleep(3)
print(x * y)
"""

#Misleči stroj - razlicica 2
"""
x = float(input("Prvo število?"))
y = float(input("Drugo število?"))
sleep(random.randint(1,5))
print(x * y)
"""

#Misleči stroj - razlicica 3
"""
x = float(input("Prvo število?"))
y = float(input("Drugo število?"))
sleep(x * y / 10)
print(x * y)
"""






