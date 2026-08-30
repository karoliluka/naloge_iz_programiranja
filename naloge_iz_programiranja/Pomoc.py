#Multiplikativni range
"""
start = 7
faktor = 4
dolzina = 7

seznam = [start]
for i in range(dolzina - 1):
    seznam.append(seznam[i] * faktor)
print(seznam)
"""

#Drugi največji
"""
xs = [5, 1, 4, 2, 3]
print(sorted(xs)[-2])
"""

#Cezar
"""
print(chr(ord("a") + 3))
"""

#Najsirsa ovira
"""
def najsirsa_ovira(vrstica):
    dolzine_ovir = []
    v_oviri = False
    for i, char in enumerate(vrstica, start = 1):
        if char == "#" and v_oviri is False:
            start = i
            v_oviri = True
        elif char == "#" and v_oviri is True:
            continue
        elif char == "." and v_oviri is True:
            end = i
            dolzine_ovir.append(end - start)
            v_oviri = False
    return max(dolzine_ovir)

print(najsirsa_ovira(".##.####...##."))
"""

#Pretvori zemljevid
"""
def pretvori_vrstico(vrstica):
    ovire = []
    v_oviri = False
    if vrstica[-1] == "#":
        vrstica += "."

    for i, char in enumerate(vrstica):
        if char == "#" and v_oviri is False:
            start = i
            v_oviri = True
        elif char == "#" and v_oviri is True:
            continue
        elif char == "." and v_oviri is True:
            end = i
            ovire.append((start + 1, end))
            v_oviri = False
    return ovire
zemljevid = [
    "......",
    "..##..",
    ".##.#.",
    "...###",
    "###.##",
]

def pretvori_zemljevid(vrstice):
    seznam = []
    for y, vrstica in enumerate(vrstice, start=1):
        if len(pretvori_vrstico(vrstica)) >= 1:
            for x1, x2 in pretvori_vrstico(vrstica):
                nova_ovira = (x1, x2, y)
                seznam.append(nova_ovira)
    return seznam



#Prej potem
prej = [
            "..............##...",
            "..###.....###....##",
            "...###...###...#...",
            "...........#.....##",
            "...................",
            "###.....#####...###"
        ]

potem = [
            "...##.........##...",
            "..###.....###....##",
            "#..###...###...#...",
            "...###.....#.....##",
            "................###",
            "###.....#####...###"
        ]

def izboljsave(prej, potem):
    return sorted(list(set(pretvori_zemljevid(potem)) - set(pretvori_zemljevid(prej))), key=lambda ovira: ovira[2])

def huligani(prej, potem):
    seznam_novih = izboljsave(prej, potem)

print("Friderik I.".split()[0][-1])
"""

