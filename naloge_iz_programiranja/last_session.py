from collections import defaultdict
from email.policy import default
from turtledemo.rosette import mn_eck

predniki = {
    "jaz": ["mama", "oce"],
    "mama": ["babica1", "dedek1"],
    "oce": ["babica2", "dedek1"],  # dedek1 je skupen!
    "babica1": [], "dedek1": [], "babica2": [], "dedek2": []
}

def vsi_predniki(oseba, predniki):
    if not predniki[oseba]:
        return set()

    mnozica_prednikov = set(predniki[oseba])
    for prednik in predniki[oseba]:
        mnozica_prednikov |= vsi_predniki(prednik, predniki)

    return mnozica_prednikov

def stevilo_prednikov(oseba, predniki):
    return len(vsi_predniki(oseba, predniki))

print(stevilo_prednikov("jaz", predniki)) # -> 4 (mama, oce, babica1, dedek1, babica2 = pravzaprav 5)

class Zival:
    def __init__(self, ime, starost):
        self.ime = ime
        self.starost = starost

    def opis(self):
        return f"{self.ime}, star {self.starost} let"

class Pes(Zival):
    def __init__(self, ime, starost, pasma):
        super().__init__(ime, starost)
        self.pasma = pasma

    def opis(self):
        return super().opis() + f", pasma {self.pasma}"

"""
z = Zival("Muri", 3)
print(z.opis())  # "Muri, star 3 let"

p = Pes("Rex", 2, "Labrador")
print(p.opis())  # "Rex, star 2 let, pasma Labrador"
"""

nakupi = ["mleko 1.2", "kruh 2.5", "mleko 1.1", "jajca 3.0", "kruh 2.6", "mleko 1.3"]
def najdrazji_izdelek(nakupi):
    slovar = defaultdict(float)
    for nakup in nakupi:
        izdelek, cena = nakup.split(" ")
        slovar[izdelek] += float(cena)
    return max(slovar, key=slovar.get)

print(najdrazji_izdelek(nakupi))