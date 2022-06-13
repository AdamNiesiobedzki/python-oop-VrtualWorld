import random

from Animal import Animal


class Turtle(Animal):
    __TURTLE_INITIATIVE = 1
    __TURTLE_STRENGTH = 2
    __ARMOR = 5

    def __init__(self, posX, posY, strength, world):
        if strength is None:
            super().__init__(world, self.__TURTLE_STRENGTH, self.__TURTLE_INITIATIVE, posX, posY, "turtle", "turtle.png")
        else:
            super().__init__(world, strength, self.__TURTLE_INITIATIVE, posX, posY, 'turtle', 'turtle.png')
        world.addOrganism(self)


    def printSign(self):
        print("T", end='', sep='')

    def isTheSameSpecies(self, organism):
        if isinstance(organism, Turtle):
            return True
        else:
            return False

    def createChild(self, posX, posY, world):
        Turtle(posX, posY, None, world)

    def hasDefended(self, attacker):
        if attacker.getStrength() < self.__ARMOR:
            return True
        else:
            return False

    def action(self):
        isMoving = random.randint(0, 3)
        if isMoving == 0:
            super().action()

