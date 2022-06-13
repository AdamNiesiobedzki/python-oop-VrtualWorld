import random

from Animal import Animal


class Antilope(Animal):
    __ANTILOPE_INITIATIVE = 4
    __ANTILOPE_STRENGTH = 4

    def __init__(self, posX, posY, strength, world):
        if strength is None:
            super().__init__(world, self.__ANTILOPE_STRENGTH, self.__ANTILOPE_INITIATIVE, posX, posY, "antilope",
                         "antilope.png")
        else:
            super().__init__(world, strength, self.__ANTILOPE_INITIATIVE, posX, posY, 'antilope', 'antilope.png')
        world.addOrganism(self)

    def printSign(self):
        print("A", end='', sep='')

    def isTheSameSpecies(self, organism):
        if isinstance(organism, Antilope):
            return True
        else:
            return False

    def createChild(self, posX, posY, world):
        Antilope(posX, posY, None, world)

    def hasDefended(self, attacker):
        run = random.randint(0, 1)
        success = 0
        if run == 1:
            if self._y > 0 and self._world.getField(self._x, self._y - 1) is None:
                self._y += -1
                self._nextY = self._y
                success = 1
            elif self._x > 0 and self._world.getField(self._x - 1, self._y) is None:
                self._x += -1
                self._nextX = self._x
                success = 1
            elif self._x + 1 < self._world.getWidth() and self._world.getField(self._x + 1, self._y) is None:
                self._x += 1
                self._nextX = self._x
                success = 1
            elif self._y + 1 < self._world.getHeight() and self._world.getField(self._x, self._y + 1) is None:
                self._y += 1
                self._nextY = self._y
                success = 1
        if success == 1:
            return True
        else:
            return False

    def action(self):
        self._hasMoved = True
        direction = random.randint(0, 3)

        if direction == self._UP:
            if self.getY() > 1:
                self._nextY += -2

        elif direction == self._DOWN:
            if self.getY() < self._world.getHeight() - 2:
                self._nextY += 2

        elif direction == self._LEFT:
            if self.getX() > 1:
                self._nextX += -2

        elif direction == self._RIGHT:
            if self.getX() < self._world.getHeight() - 2:
                self._nextX += 2
