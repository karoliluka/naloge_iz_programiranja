from itertools import count
#A-javnost nizov
"""
niz = str(input("Vpišite niz: "))
print(niz.count("a"))
"""

#Najmanjši pozitivec
"""
l = [5, 4, -7, 2, 12, -3, -4, 11, 7]
samo_pozitivni = []
for x in l:
    if x > 0:
        samo_pozitivni.append(x)
print(min(samo_pozitivni))

print(min([x for x in l if x > 0]))
"""

#Najtežji ven
"""
teze = [66, 72, 84, 68, 96, 73, 80]
del teze[teze.index(max(teze))]
print(teze)
"""

#Povprečje brez najtežjega
"""
teze = [66, 72, 84, 68, 96, 73, 80]
del teze[teze.index(max(teze))]
print(sum(teze) / len(teze))
"""

#Padajoča povprečja
"""
teze = [66, 72, 84, 68, 96, 73, 80]
while teze:
    naj = 0
    naj_i = 0
    for i, teza in enumerate(teze):
        if teza > naj:
            naj = teza
            naj_i = i
    del teze[naj_i]
    if len(teze) >= 1:
        print("Povprečje: ", sum(teze) / len(teze))
    else:
        print("Ni več elementov.")
"""

#Indeks telesne teže
"""
podatki = [
    ["Ana", 55, 165],
    ["Berta", 60, 153],
]

for ime, teza, visina in podatki:
    print(ime, teza / (visina / 100)**2)
"""

#Fršlusanje zmagovalcev
"""
finska = [153, 141, 152, 160, 135]
danska = [148, 148, 148, 148, 148]
tocke_f = 0
tocke_d = 0
for finec, danec in zip(finska, danska):
    if finec > danec:
        tocke_f += 1
    else:
        tocke_d += 1

if tocke_f > tocke_d:
    print("Zmagala je Finska z", tocke_f, "proti Danski z", tocke_d, ".")
else:
    print("Zmagala je Danska z", tocke_d, "proti Finski z", tocke_f, ".")
"""

#Dobički
"""
l = [4, 5, 8, 0, 4, 1, 2, 0, 0, 0, 4, 6, 10, 0, 5, 0, 12, 1, 0]
vsota = 0
for x in l:
    if x != 0:
        vsota += x

    if vsota == 0:
        continue
    elif vsota > 0 and x == 0:
        print(vsota)
        vsota = 0
"""

#Seznam dobičkov
"""
l = [4, 5, 8, 0, 4, 1, 2, 0, 0, 0, 4, 6, 10, 0, 5, 0, 12, 1, 0]
vsota = 0
seznam = []
for x in l:
    if x != 0:
        vsota += x

    if vsota == 0:
        continue
    elif vsota > 0 and x == 0:
        seznam.append(vsota)
        vsota = 0
print(seznam)
"""

#Oklepaji
"""
niz = "(((((((((("
stevec = 0
ni_negativen = True

for char in niz:
    if char == "(":
        stevec += 1
    else:
        stevec -= 1

    if stevec < 0:
        ni_negativen = False
        break

if ni_negativen and stevec == 0:
    print("Je regularen izraz.")
else:
    print("Ni regularen izraz.")
"""

#Malo bolj kompleksni oklepaji
"""
niz = "AaBbACBbDdcDda"
sklad = []
regularen = True

for znak in niz:
    if znak.isupper():
        sklad.append(znak)
    else:
        if not sklad:
            regularen = False
            break
        if sklad[-1] != znak.upper():
            regularen = False
            break
        elif sklad[-1] == znak.upper():
            sklad.pop()
        else:
            regularen = False
            break
if regularen and not sklad:
    print("Je regularen izraz.")
else:
    print("Ni regularen izraz.")
"""


