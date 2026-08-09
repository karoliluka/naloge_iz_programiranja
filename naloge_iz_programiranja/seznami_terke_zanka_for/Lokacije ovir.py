#Ogrevalna naloga
"""
ovire = "##..#...#"
if ovire[-1] == "#":
    ovire += "."
seznam_parov = []
v_oviri = False
for i, char in enumerate(ovire, start=1):
    if char == "#" and v_oviri is False:
        start = i
        v_oviri = True
    elif char == "#" and v_oviri is True:
        continue
    elif char == "." and v_oviri is True:
        end = i
        seznam_parov.append((start, end - 1))
        v_oviri = False
print(seznam_parov)
"""

#Obvezna naloga
"""
zemljevid = [
    "......",
    "..##..",
    ".##.#.",
    "...###",
    "###.##",
]

seznam_ovir = []
for j, vrstica in enumerate(zemljevid, start=1):
    if vrstica[-1] == "#":
        vrstica += "."
    v_oviri = False

    for i, char in enumerate(vrstica, start=1):
        if char == "#" and v_oviri is False:
            start = i
            v_oviri = True
        elif char == "#" and v_oviri is True:
            continue
        elif char == "." and v_oviri is True:
            end = i
            seznam_ovir.append((start, end - 1, j))
            v_oviri = False
print(seznam_ovir)
"""

#Dodatna naloga
"""
ovire = [(3, 4, 2), (2, 3, 3), (5, 5, 3), (4, 6, 4), (1, 3, 5), (5, 6, 5)]
vrstice = max(y for _, _, y in ovire)
stolpci = max(x2 for _, x2, _ in ovire)

tab = []
for i in range(vrstice):
    tab.append("." * stolpci)

for x1, x2, y in ovire:
    vrstica = tab[y - 1]
    nova_vrstica = vrstica[:x1 - 1] + "#" * (x2 - x1 + 1) + vrstica[x2:]
    tab[y - 1] = nova_vrstica

for vrstica in tab:
    print(vrstica)
"""













