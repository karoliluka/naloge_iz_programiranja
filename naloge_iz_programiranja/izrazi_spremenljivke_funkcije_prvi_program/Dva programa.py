#Prvi program
"""
a = imput("prva kateta")
b = imput("druga kateta")
c = sqrt(a^2 + b^2)
print(Dolzina hipotenuze je, c)
"""

#Prvi program - popravljen
"""
from math import *
a = float(input("prva kateta"))
b = float(input("druga kateta"))
c = sqrt((a**2) + (b**2))
print("Dolzina hipotenuze je", c)
"""

#Drugi program
"""
ime = input("Kako ti je ime?")
print("Pozdravljen, ', ime, 'bi vadil poštevanko?")
int(input("Pa dajva. Vpiši prvi faktor."))
int(input("Pa še drugi faktor."))
rezultat = a*b
c = input("Koliko, misliš, znaša produkt?")
print("Napisal si, da je ", a, "krat", b, "enako", c)
print("Pravilen odgovor pa je", rezultat)
"""

#Drugi program - popravljen
ime = str(input("Kako ti je ime?"))
print("Pozdravljen, ", ime, "bi vadil poštevanko?")
a = float(input("Pa dajva. Vpiši prvi faktor."))
b = float(input("Pa še drugi faktor."))
rezultat = a*b
c = float(input("Koliko, misliš, znaša produkt?"))
print("Napisal si, da je ", a, "krat", b, "enako", c)
print("Pravilen odgovor pa je", rezultat)


