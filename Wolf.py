from Animal import Animal


class Wolf(Animal):
    __WOLF_INITIATIVE = 5
    __WOLF_STRENGTH = 9

    def __init__(self, posX, posY, strength, world):
        if strength is None:
            super().__init__(world, self.__WOLF_STRENGTH, self.__WOLF_INITIATIVE, posX, posY, "wolf", "wolf.png")
        else:
            super().__init__(world,strength,self.__WOLF_INITIATIVE,posX,posY, 'wolf', 'wolf.png')
        world.addOrganism(self)

    def printSign(self):
        print("W", end='', sep='')

    def isTheSameSpecies(self, organism):
        if isinstance(organism, Wolf):
            return True
        else:
            return False

    def createChild(self, posX, posY, world):
        Wolf(posX, posY, None, world)