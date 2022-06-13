from Plant import Plant
import random


class Dandelion(Plant):
    __DANDELION_STRENGTH = 0
    __TRIES_TO_REPRODUCE = 3

    def __init__(self, posX, posY, strength, world):
        if strength is None:
            super().__init__(world, self.__DANDELION_STRENGTH, posX, posY, "dandelion", "dandelion.png")
        else:
            super().__init__(world, strength, posX, posY, 'dandelion', 'dandelion.png')
        world.addOrganism(self)


    def printSign(self):
        print("D", end='', sep='')

    def action(self):
        self._hasMoved = True
        for i in range(self.__TRIES_TO_REPRODUCE):
            reproduce = random.randint(0, 15)
            if reproduce < Plant._CHANCE_TO_REPRODUCE:
                self.reproduce()

    def createChild(self, posX, posY, world):
        Dandelion(posX, posY, None, world)
