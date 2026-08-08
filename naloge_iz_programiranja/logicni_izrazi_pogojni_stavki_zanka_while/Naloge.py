#Blagajna "vse po pet"
"""
i = 0
vsota = 0
while i < 5:
    cena = int(input("Cena artikla: "))
    vsota += cena
    i += 1
print("Vsota: ", vsota)
"""

#Blagajna "konkurenca"
"""
st_izdelkov = int(input("Število izdelkov: "))
i = 0
vsota = 0
while i < st_izdelkov:
    cena = int(input("Cena artikla: "))
    vsota += cena
    i += 1
print("Vsota: ", vsota)
"""

#Blagajna "top shop"
"""
cena = 1
vsota = 0
while cena != 0:
    cena = int(input("Cena artikla: "))
    vsota += cena
print("Vsota: ", vsota)
"""

#Državna agencija za varstvo potrošnikov
"""
cena = 1
vsota = 0
st_izdelkov = -1
while cena != 0:
    cena = int(input("Cena artikla: "))
    vsota += cena
    st_izdelkov += 1
print("Vsota: ", vsota)
print("Povprečna cena: ", vsota / st_izdelkov)
"""

#Tekoči račun
"""
tekoci_racun = 0
while tekoci_racun > -100:
    sprememba = int(input("Sprememba "))
    tekoci_racun += sprememba
    print("Stanje ",tekoci_racun)
print("Bankrot")
"""

#Klub anonimnih potrošnikov
"""
cena = 1
st_artiklov = 0
vsota = 0
while cena != 0 and vsota < 100 and st_artiklov < 10:
    cena = int(input("Cena: "))
    vsota += cena
    st_artiklov += 1

if cena == 0:
    st_artiklov -= 1

print("Porabili boste", vsota, "evrov za", st_artiklov, "stvari.")
"""





