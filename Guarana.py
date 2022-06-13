from Plant import Plant


class Guarana(Plant):
    __GUARANA_STRENGTH = 0
    __BONUS_STRENGTH = 3

    def __init__(self, posX, posY, strength, world):
        if strength is None:
            super().__init__(world, self.__GUARANA_STRENGTH, posX, posY, "guarana", "guarana.png")
        else:
            super().__init__(world,strength,posX,posY,'gurana', 'guarana.png')
        world.addOrganism(self)

    def printSign(self):
        print("U", end='', sep='')

    def createChild(self, posX, posY, world):
        Guarana(posX, posY, None, world)

    def hasDefended(self, attacker):
        attacker.increaseStrength(self.__BONUS_STRENGTH)
        return False
    