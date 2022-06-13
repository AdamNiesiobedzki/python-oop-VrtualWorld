import random

from Animal import Animal


class Fox(Animal):
    __FOX_INITIATIVE = 4
    __FOX_STRENGTH = 4

    def __init__(self, posX, posY, strength, world):
        if strength is None:
            super().__init__(world, self.__FOX_STRENGTH, self.__FOX_INITIATIVE, posX, posY, "fox", "fox.png")
        else:
            super().__init__(world,strength,self.__FOX_INITIATIVE,posX,posY, 'fox', 'fox.png')
        world.addOrganism(self)


    def printSign(self):
        print("F", end='', sep='')

    def isTheSameSpecies(self, organism):
        if isinstance(organism, Fox):
            return True
        else:
            return False

    def createChild(self, posX, posY, world):
        Fox(posX, posY, None, world)

    def action(self):
        self._hasMoved = True
        direction = random.randint(0, 3)

        if direction == self._UP:
            if self.getY() > 0:
                if self.isSafe(self._nextX, self._nextY - 1, self._strength):
                    self._nextY += -1

        elif direction == self._DOWN:
            if self.getY() < self._world.getHeight() - 1:
                if self.isSafe(self._nextX, self._nextY + 1, self._strength):
                    self._nextY += 1

        elif direction == self._LEFT:
            if self.getX() > 0:
                if self.isSafe(self._nextX - 1, self._nextY, self._strength):
                    self._nextX += -1

        elif direction == self._RIGHT:
            if self.getX() < self._world.getWidth() - 1:
                if self.isSafe(self._nextX + 1, self._nextY, self._strength):
                    self._nextX += 1

    def isSafe(self, posX, posY, strength):
        temp = self._world.getField(posX, posY)
        if temp is None:
            return True
        elif temp.getStrength() <= strength:
            return True
        else:
            return False
