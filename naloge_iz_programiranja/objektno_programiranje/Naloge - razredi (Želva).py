from math import *
import risar

class Turtle:
    def __init__(self):
        self.x = risar.maxX/2
        self.y = risar.maxY/2
        self.angle = 0
        self.pen_active = True
        self.pause = 0
        self.body = risar.krog(0, 0, 5, risar.zelena, 3)
        self.head = risar.krog(0, 0, 2, risar.zelena, 3)
        self.indikator = risar.krog(0, 0, 2, risar.rumena, 2)
        self.width = 1
        self.color = risar.zelena
        self.posodobi_indikator()
        self.seznam_odtisov = []
        self.recording = None
        self.update()

    def update(self):
        self.body.setPos(self.x, self.y)
        phi = radians(90 - self.angle)
        self.head.setPos(self.x + 5 * cos(phi), self.y - 5 * sin(phi))
        self.indikator.setPos(self.x + 5 * cos(phi), self.y - 5 * sin(phi))
        risar.obnovi()
        if self.pause:
            self.wait(self.pause)

    def forward(self, a):
        if self.recording is not None:
            self.recording.append((self.forward, (a,)))
        phi = radians(90 - self.angle)
        nx = self.x + a * cos(phi)
        ny = self.y - a * sin(phi)
        if self.pen_active:
            risar.crta(self.x, self.y, nx, ny, self.color, self.width)
        self.x = nx
        self.y = ny
        self.update()

    def turn(self, phi):
        if self.recording is not None:
            self.recording.append((self.turn, (phi,)))
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
        self.posodobi_indikator()

    def pen_down(self):
        self.pen_active = True
        self.posodobi_indikator()

    def wait(self, s):
        risar.cakaj(s)

    def hide(self):
        self.body.hide()
        self.head.hide()
        self.posodobi_indikator()

    def show(self):
        self.body.show()
        self.head.show()
        self.posodobi_indikator()

    def set_pause(self, s):
        self.pause = s

    def no_pause(self):
        self.set_pause(0)

    def turnAround(self):
        self.turn(180)

    def setWidth(self, w):
        self.width = w

    def setColor(self, c):
        self.color = c

    def posodobi_indikator(self):
        if self.pen_active and self.head.isVisible():
            self.indikator.show()
        else:
            self.indikator.hide()

    def stamp(self):
        odtis = risar.krog(self.x, self.y, 2, risar.zelena, 3)
        self.seznam_odtisov.append(odtis)

    def clearStamps(self):
        for krog in self.seznam_odtisov:
            krog.hide()
        self.seznam_odtisov = []

    def startRecording(self):
        self.recording = []

    def stopRecording(self):
        trace = self.recording
        self.recording = None
        return trace

    def play(self, trace):
        for func, pars in trace:
            func(*pars)

#turnAround
"""
t = Turtle()
t.forward(50)      # gre gor
t.turnAround()      # obrne se za 180 stopinj
t.forward(50)       # gre nazaj čez isto črto (nazaj na start)

risar.stoj()
"""

#selfWidth in selfColor
"""
t = Turtle()
t.forward(20)
t.setWidth(10)
t.forward(20)
t.setColor(risar.rdeca)
t.forward(20)
risar.stoj()
"""

#Indikator peresa
"""
t = Turtle()
t.pen_up()
t.hide()
t.show()
risar.stoj()
# pero mora biti nevidno
"""

#stamp in clearStamps
"""
t = Turtle()
t.forward(10)
t.stamp()
t.left()
t.forward(100)
t.turn(45)
t.forward(20)
t.stamp()
t.right()
t.forward(40)
t.left()
t.forward(40)
t.right()
t.forward(40)
t.stamp()
t.right()
t.forward(40)
t.clearStamps()
"""

# Snemalnik makrov
"""
t = Turtle()
t.startRecording()
for i in range(4):
    t.forward(100)
    t.right()
kvadrat = t.stopRecording()

for i in range(10):
    t.turn(36)
    t.play(kvadrat)
risar.stoj()
"""



