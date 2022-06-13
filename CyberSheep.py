from math import fabs
from Animal import Animal


class CyberSheep(Animal):
    __CYBER_SHEEP_INITIATIVE = 4
    __CYBER_SHEEP_STRENGTH = 11
    closestPine = None

    def __init__(self, posX, posY, strength, world):
        if strength is None:
            super().__init__(world, self.__CYBER_SHEEP_STRENGTH, self.__CYBER_SHEEP_INITIATIVE, posX, posY,
                             "cybersheep",
                             "cybersheep.png")
        else:
            super().__init__(world, strength, self.__CYBER_SHEEP_INITIATIVE, posX, posY, 'cybersheep', 'cybersheep.png')
        world.addOrganism(self)

    def printSign(self):
        print("M", end='', sep='')

    def isTheSameSpecies(self, organism):
        if isinstance(organism, CyberSheep):
            return True
        else:
            return False

    def createChild(self, posX, posY, world):
        CyberSheep(posX, posY, None, world)

    def scanForClosestPine(self):
        from Pine import Pine
        self.closestPine = None
        distance = None
        for i in range(self._world.getPopulation()):
            organism = self._world.getOrganism(i)
            if isinstance(organism, Pine):
                tempDistance = fabs(self.getX() - organism.getX()) + fabs(self.getY() - organism.getY())
                if distance is None:
                    distance = tempDistance
                    self.closestPine = organism
                elif distance > tempDistance:
                    distance = tempDistance
                    self.closestPine = organism

    def action(self):
        self.scanForClosestPine()
        if self.closestPine is None:
            super().action()
        else:
            if self.closestPine.getX() > self.getX():
                self._nextX += 1
            elif self.closestPine.getX() < self.getX():
                self._nextX += -1

            if self.closestPine.getY() > self.getY():
                self._nextY += 1
            elif self.closestPine.getY() < self.getY():
                self._nextY += -1
