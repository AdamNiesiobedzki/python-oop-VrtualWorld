from Animal import Animal


class Sheep(Animal):
    __SHEEP_INITIATIVE = 4
    __SHEEP_STRENGTH = 4

    def __init__(self, posX, posY, strength, world):
        if strength is None:
            super().__init__(world, self.__SHEEP_STRENGTH, self.__SHEEP_INITIATIVE, posX, posY, "sheep", "sheep.png")
        else:
            super().__init__(world, strength, self.__SHEEP_INITIATIVE, posX, posY, 'sheep', 'sheep.png')
        world.addOrganism(self)


    def printSign(self):
        print("S", end='', sep='')

    def isTheSameSpecies(self, organism):
        if isinstance(organism, Sheep):
            return True
        else:
            return False

    def createChild(self, posX, posY, world):
        Sheep(posX, posY, None, world)
