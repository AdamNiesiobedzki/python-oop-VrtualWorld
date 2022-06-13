from Animal import Animal


class Human(Animal):
    __HUMAN_INITIATIVE = 4
    __HUMAN_STRENGTH = 5
    __BONUS_STRENGTH = 10
    __COOLDOWN = 10
    __skillCD = None

    def __init__(self, posX, posY, cooldown, strength, world):
        if cooldown is None and strength is None:
            super().__init__(world, self.__HUMAN_STRENGTH, self.__HUMAN_INITIATIVE, posX, posY, "human", "human.png")
            self.__skillCD = 0
        else:
            super().__init__(world, strength, self.__HUMAN_INITIATIVE, posX, posY, 'human', 'human.png')
            self.__skillCD = cooldown
        world.addOrganism(self)
        world.asignHuman(self)

    #def __init__(self, posX, posY, cooldown, strength, world):
    #    super().__init__(world, strength, self.__HUMAN_INITIATIVE, posX, posY, "human", "human.png")
    #    self.__skillCD = cooldown
    #    world.addOrganism(self)
    #    world.asignHuman(self)

    def printSign(self):
        print("H", end='', sep='')

    def action(self):
        if self.__skillCD > 0:
            self.__skillCD += -1
            self._strength += -1

        if self._world.getNextMove() == self._UP:
            if self.getY() > 0:
                self._nextY += -1
        elif self._world.getNextMove() == self._DOWN:
            if self.getY() < self._world.getHeight() - 1:
                self._nextY += 1
        elif self._world.getNextMove() == self._LEFT:
            if self.getX() > 0:
                self._nextX += -1
        elif self._world.getNextMove() == self._RIGHT:
            if self.getX() < self._world.getWidth() -1:
                self._nextX += 1

    def useSkill(self):
        if self.__skillCD == 0:
            self.increaseStrength(self.__BONUS_STRENGTH)
            self.__skillCD = self.__COOLDOWN

    def getCooldown(self):
        return self.__skillCD
