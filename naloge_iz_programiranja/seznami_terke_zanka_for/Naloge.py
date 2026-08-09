#Vsebuje
"""
xs = [5, 4, -7, 12, -3, -4, 11, 2]
videl_sem_42 = False
if 42 in xs:
    videl_sem_42 = True

print(videl_sem_42)
if videl_sem_42:
    print("Res sem videl 42.")
"""

#Vsebuje niz
"""
xs = ['foo', 'bar', 'baz', 'foobar']
videl_sem_waldo = False
if "Waldo" in xs:
    videl_sem_waldo = True
print(videl_sem_waldo)
if videl_sem_waldo:
    print("Res sem videl Waldo.")
"""

#Štej
"""
xs = [5, 4, -7, 42, 12, -3, -4, 11, 42, 2]
i = 0
for x in xs:
    if x == 42:
        i += 1
print(f"Število 42 se v seznamu pojavi {i} krat.")
"""

#Vsebuje večkratnik
"""
xs = [5, 4, -7, 42, 12, -3, -4, 11, 42, 2]
je_veckratnik = False
for x in xs:
    if 42 % x == 0:
        je_veckratnik = True
print(je_veckratnik)
"""

#Le večkratniki
"""
xs = [5, 4, -7, 42, 12, -3, -4, 11, 42, 2]
samo_veckratniki = True
for x in xs:
    if 42 % x != 0:
        samo_veckratniki = False
        break
print(samo_veckratniki)
"""

#Delitelji
"""
n = int(input("Vpiši število: "))
for i in range(1, n):
    if n % i == 0:
        print(i)     
"""

#Vsota deliteljev
"""
n = int(input("Vpiši število: "))
vsota = 0
for i in range(1, n):
    if n % i == 0:
        vsota += i
print("Vsota deliteljev", vsota)
"""

#Popolna števila
"""
n = int(input("Vpiši število: "))
vsota = 0
for i in range(1, n):
    if n % i == 0:
        vsota += i

if vsota == n:
    print(n, "je popolno število.")
else:
    print(n, "ni popolno število.")
"""

#Prijateljska števila
"""
n = int(input("Vnesi število: "))
vsota_deliteljev_n = 0
for i in range(1, n):
    if n % i == 0:
        vsota_deliteljev_n += i
print(vsota_deliteljev_n)

potencialni_prijatelj = vsota_deliteljev_n
vsota_potencialnega_prijatelja = 0
for i in range(1, potencialni_prijatelj):
    if potencialni_prijatelj % i == 0:
        vsota_potencialnega_prijatelja += i

if vsota_potencialnega_prijatelja == n:
    print(f"{n} ima prijatelja {vsota_deliteljev_n}.")
else:
    print(f"{n} nima prijateljev.")
"""

#Praštevilo
"""
n = int(input("Vnesi število: "))
for i in range(2, n):
    if n % i == 0:
        print(n, "ni praštevilo.")
        break
else:
    print(n, "je praštevilo")
"""

#Praštevila
"""
for i in range(2, 100):
    for j in range(2, i):
        if i % j == 0:
            break
    else:
        print(i)
"""

#Kino
"""
filmi = [
    ('Poletje v skoljki 2', 6.1),
    ('Ne cakaj na maj', 7.3),
    ('Pod njenim oknom', 7.1),
    ('Kekec', 8.1),
    ('Poletje v skoljki', 7.2),
    ('To so gadi', 7.7),
]

for film, rating in filmi:
    if rating > 7.0:
        print(film)

naj_ocena = 0
naj_film = ""
for film, rating in filmi:
    if rating > naj_ocena:
        naj_ocena = rating
        naj_film = film
print(naj_film)

for film, rating in filmi:
    if rating > 7.0:
        print(film)
        break

vsota = 0
for _, rating in filmi:
    vsota += rating
print(vsota / len(filmi))

for film1, _ in filmi:
    nadaljevanje = film1 + " 2"
    for film2, _ in filmi:
        if nadaljevanje == film2:
            print(film1)
"""

#Kino 2
"""
filmi = ['Poletje v skoljki 2', 'Ne cakaj na maj', 'Pod njenim oknom', 'Kekec', 'Poletje v skoljki', 'To so gadi']
ocene = [6.1, 7.3, 7.1, 8.1, 7.2, 7.7]

for film, rating in zip(filmi, ocene):
    st_presledkov = 0
    for char in film:
        if char == " ":
            st_presledkov += 1
    if st_presledkov == 2:
        print(f"{film} ({rating})")
"""







