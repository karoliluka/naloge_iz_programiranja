#Ogrevalni del
"""
ovire = [(3, 9), (7, 1), (5, 9), (9, 2), (7, 3),
         (10, 5), (4, 7), (9, 8), (6, 5), (8, 6),
         (1, 5), (8, 4), (2, 3), (3, 6)]
x = 3

tabela_ovir = []
for x_ovira, y_ovira in ovire:
    if x_ovira == x:
        tabela_ovir.append((x_ovira, y_ovira))

if tabela_ovir:
    najm_x = x
    najm_y = tabela_ovir[0][1]
    for x_ovira, y_ovira in tabela_ovir:
        if y_ovira < najm_y:
            najm_y = y_ovira
            najm_x = x_ovira
    print(najm_y)
else:
    print("Tabela ovir je prazna.")
"""

#Obvezna naloga
"""
ovire = [(1, 3, 6), (2, 4, 3), (4, 6, 7),
         (3, 4, 9), (6, 9, 5), (9, 10, 2), (9, 10, 8)]
x = 6

y_tab = []
for x1, x2, y in ovire:
    if x1 <= x <= x2:
        y_tab.append(y)
print(min(y_tab))
"""






