from Animal import Animal

from Plant import Plant


class Pine(Plant):
    __PINE_STRENGTH = 0

    def __init__(self, posX, posY, strength, world):
        if strength is None:
            super().__init__(world, self.__PINE_STRENGTH, posX, posY, "pine", "pine.png")
        else:
            super().__init__(world, strength, posX, posY, 'pine', 'pine.png')
        world.addOrganism(self)


    def printSign(self):
        print("P", end='', sep='')

    def createChild(self, posX, posY, world):
        Pine(posX, posY, None, world)

    def action(self):
        super().action()
        self.killSurroundingFields()

    def killSurroundingFields(self):
        from CyberSheep import CyberSheep
        for i in range(self._y - 1, self._y + 2, 1):
            for k in range(self._x - 1, self._x + 2, 1):
                if (0 <= k < self._world.getWidth()
                        and 0 <= i < self._world.getHeight()):
                    organismToKill = self._world.getField(k, i)
                    if (isinstance(organismToKill, Animal) and
                            not isinstance(organismToKill, CyberSheep)):
                        self._world.kill(organismToKill.getX(), organismToKill.getY())
