from Animal import Animal
from Plant import Plant


class Wolfberries(Plant):
    __WOLFBERRIES_STRENGTH = 0

    def __init__(self, posX, posY, strength, world):
        if strength is None:
            super().__init__(world, self.__WOLFBERRIES_STRENGTH, posX, posY, "wolfberries", "wolfberries.png")
        else:
            super().__init__(world, strength, posX, posY, 'wolfberries', 'wolfberries.png')
        world.addOrganism(self)



    def printSign(self):
        print("B", end='', sep='')

    def createChild(self, posX, posY, world):
        Wolfberries(posX, posY, None, world)

    def hasDefended(self, attacker):
        if isinstance(attacker, Animal):
            self._world.kill(attacker.getX(), attacker.getY())
        return False

