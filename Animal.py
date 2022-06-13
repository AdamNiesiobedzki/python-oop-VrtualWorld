from Organism import Organism
import random


class Animal(Organism):
    _LEFT = 0
    _RIGHT = 1
    _UP = 2
    _DOWN = 3
    __WON = 1
    __LOST = 2
    __REPRODUCE = 3
    __DRAW = 4

    def __init__(self, world, strength, initiative, posX, posY, name, image):
        super().__init__(world, strength, initiative, posX, posY, name, image)

    def isTheSameSpecies(self, organism):
        return False

    def action(self):
        self._hasMoved = True
        direction = random.randint(0, 3)

        if direction == self._UP:
            if self.getY() > 0:
                self._nextY += -1

        elif direction == self._DOWN:
            if self.getY() < self._world.getHeight() - 1:
                self._nextY += 1

        elif direction == self._LEFT:
            if self.getX() > 0:
                self._nextX += -1

        elif direction == self._RIGHT:
            if self.getX() < self._world.getWidth() - 1:
                self._nextX += 1

    def colision(self, organism):
        if self.isTheSameSpecies(organism):
            if self.getAge() > 1 and organism.getAge() > 1:
                return self.__REPRODUCE
            else:
                return self.__DRAW

        elif self.getStrength() >= organism.getStrength():
            if organism.hasDefended(self):
                return self.__DRAW
            else:
                return self.__WON

        else:
            if self.hasDefended(organism):
                return self.__DRAW
            else:
                return self.__LOST

