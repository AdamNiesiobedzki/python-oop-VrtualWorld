from Plant import Plant


class Grass(Plant):
    __GRASS_STRENGTH = 0

    def __init__(self, posX, posY, strength, world):
        if strength is None:
            super().__init__(world, self.__GRASS_STRENGTH, posX, posY, "grass", "grass.png")
        else:
            super().__init__(world,strength,posX,posY,'grass', 'grass.png')
        world.addOrganism(self)


    def printSign(self):
        print("G", end='', sep='')

    def createChild(self, posX, posY, world):
        Grass(posX, posY, None, world)
