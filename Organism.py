import pygame


class Organism:
    _strength = None
    _initiative = None
    _age = None
    _x = None
    _y = None
    _name = None
    _nextX = None
    _nextY = None
    _hasMoved = None
    _world = None
    image = None

    def __init__(self, world, strength, initiative, posX, posY, name, image):
        self._world = world
        self._strength = strength
        self._initiative = initiative
        self._x = posX
        self._nextX = posX
        self._y = posY
        self._nextY = posY
        self._name = name
        self._age = 0
        self._hasMoved = False
        self.image = pygame.image.load(image)

    def getStrength(self):
        return self._strength

    def getInitiative(self):
        return self._initiative

    def getAge(self):
        return self._age

    def getX(self):
        return self._x

    def getNextX(self):
        return self._nextX

    def getY(self):
        return self._y

    def getNextY(self):
        return self._nextY

    def getName(self):
        return self._name

    def getHasMoved(self):
        return self._hasMoved

    def agingProcess(self):
        self._age += 1
        self._hasMoved = False

    def increaseStrength(self, bonusStrength):
        self._strength += bonusStrength

    def printSign(self):
        pass

    def colision(self, organism):
        pass

    def move(self):
        self._x = self._nextX
        self._y = self._nextY

    def stayInPlace(self):
        self._nextX = self._x
        self._nextY = self._y

    def hasDefended(self, attacker):
        return False

    def createChild(self, posX, posY, world):
        pass

    def reproduce(self):
        if self._world.getPopulation() < self._world.MAX_POPULATION:
            if self._y - 1 >= 0 and self._world.getField(self._x, self._y - 1) is None:
                self.createChild(self._x, self._y - 1, self._world)

            elif self._x - 1 >= 0 and self._world.getField(self._x - 1, self._y) is None:
                self.createChild(self._x - 1, self._y, self._world)

            elif self._x + 1 < self._world.getWidth() and self._world.getField(self._x + 1, self._y) is None:
                self.createChild(self._x + 1, self._y, self._world)

            elif self._y + 1 < self._world.getHeight() and self._world.getField(self._x, self._y + 1) is None:
                self.createChild(self._x, self._y + 1, self._world)

        self._world.updateGameField()

    def action(self):
        pass
