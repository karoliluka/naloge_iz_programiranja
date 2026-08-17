from math import *
from random import random, randint

import risar
from risar import stoj

from PyQt5.QtCore import *
from PyQt5.QtGui import *

class Turtle:
    def __init__(self):
        self.x = risar.maxX/2
        self.y = risar.maxY/2
        self.angle = 0
        self.pen_active = True
        self.pause = 0
        self.body = risar.krog(0, 0, 5, risar.zelena, 3)
        self.head = risar.krog(0, 0, 2, risar.zelena, 3)
        self.update()

    def update(self):
        self.body.setPos(self.x, self.y)
        phi = radians(90 - self.angle)
        self.head.setPos(self.x + 5 * cos(phi), self.y - 5 * sin(phi))
        risar.obnovi()
        if self.pause:
            self.wait(self.pause)

    def forward(self, a):
        phi = radians(90 - self.angle)
        nx = self.x + a * cos(phi)
        ny = self.y - a * sin(phi)
        if self.pen_active:
            risar.crta(self.x, self.y, nx, ny)
        self.x = nx
        self.y = ny
        self.update()

    def turn(self, phi):
        self.angle += phi
        self.update()

    def backward(self, a):
        self.forward(-a)

    def left(self):
        self.turn(-90)

    def right(self):
        self.turn(90)

    def fly(self, x, y, angle):
        self.x = x
        self.y = y
        self.angle = angle
        self.update()

    def pen_up(self):
        self.pen_active = False

    def pen_down(self):
        self.pen_active = True

    def wait(self, s):
        risar.cakaj(s)

    def hide(self):
        self.body.hide()
        self.head.hide()

    def show(self):
        self.body.show()
        self.head.show()

    def set_pause(self, s):
        self.pause = s

    def no_pause(self):
        self.set_pause(0)

    def __mul__(self, other):
        razdalja = sqrt((self.x - other.x) ** 2 + (self.y - other.y) ** 2)
        if razdalja < 10:
            return Turtle()
        raise ValueError("Želvi nista dovolj blizu, da bi se lahko zmnožili.")


class ZelvaZImenom(Turtle):
    def __init__(self, ime):
        super().__init__()
        self.ime = ime

    def pozdrav(self):
        print(f"Jaz sem želva {self.ime}")

#Želva z imenom
"""
i = ZelvaZImenom('Jožica') # Ustvari želvo z imenom Jožica
i.forward(100)
i.pozdrav() # izpiše 'Jaz sem želva Jožica'
"""

class Cveka(ZelvaZImenom):
    def forward(self, a):
        print(f"{self.ime} gre {a} korakov naprej.")
        super().forward(a)

    def turn(self, phi):
        print(f"{self.ime} se obrača za {phi} stopinj")
        super().turn(phi)

#Čveka
"""
c = Cveka('Jožica') # Ustvari želvo čveko z imenom Jožica
c.forward(20) # izpiše 'Jožica gre 20 korakov naprej'
c.turn(60) # izpiše 'Jožica se obrača za 60 stopinj'
c.forward(20) # izpiše 'Jožica gre 20 korakov naprej'
c.pozdrav() # izpiše 'Jaz sem želva Jožica'
"""

class Rdecevratka(Turtle):
    def __init__(self):
        super().__init__()
        self.head.setPen(QPen(QBrush(risar.rdeca), 3))

    def forward(self, a):
        super().forward(a / 2)

    def hide(self):
        self.head.hide()

#Rdečevratka
"""
# Zelva Rdecevratka je počasna zelva
r = Rdecevratka()
r.forward(40)
r.turn(90)
r.forward(50)
t = Turtle()
t.forward(40)
t.turn(90)
t.forward(50)
risar.stoj()
"""

class VojskaZelv:
    def __init__(self, n):
        self.zelve = []
        for i in range(n):
            zelva = Turtle()
            x = 30 * i
            y = risar.maxY / 2
            angle = 0
            zelva.fly(x, y, angle)
            self.zelve.append(zelva)

    def forward(self, a):
        for zelva in self.zelve:
            zelva.forward(a)

    def turn(self, phi):
        for zelva in self.zelve:
            zelva.turn(phi)

#Vojska zelv
"""
vojska = VojskaZelv(5)
vojska.forward(50)
vojska.turn(30)
vojska.forward(50)
risar.stoj()
"""

class Pijanka(Turtle):
    def __init__(self):
        super().__init__()
        self.stevilo_popitih = 0

    def drink(self):
        self.stevilo_popitih += 1

    def popila_sem(self):
        print(self.stevilo_popitih)

    def forward(self, a):
        if self.stevilo_popitih < 5:
            super().forward(a)
            self.angle += randint(self.stevilo_popitih * (-5), self.stevilo_popitih * 5)


#Pijanka
"""
p = Pijanka()
p.drink()
p.drink()
p.drink()
p.drink()
for i in range(20):
    p.forward(10)
risar.stoj()
"""
#

class Pravokotnica(Turtle):
    def forward(self, a):
        phi = radians(90 - self.angle)
        dx = a * cos(phi)
        dy = -a * sin(phi)

        prvotni_kot = self.angle

        self.angle = 0
        super().forward(-dy)

        self.angle = 90
        super().forward(dx)

        self.angle = prvotni_kot
        self.update()

#Pravokotnica
"""
p = Pravokotnica()
p.turn(30)
p.forward(20)
p.forward(20)
p.forward(20)
p.forward(20)
p.turn(100)
p.forward(100)
risar.stoj()
"""

#Množeje - koda v originalnem Turtle klasu
oce = Turtle()
mati = Turtle()
otrok = oce * mati       # obe na začetni poziciji, razdalja = 0 -> deluje

oce.forward(20)
mati.forward(100)
otrok2 = oce * mati       # zdaj sta narazen -> vrže ValueError

risar.stoj()