from Antilope import Antilope
from CyberSheep import CyberSheep
from Dandelion import Dandelion
from Fox import Fox
from Grass import Grass
from Guarana import Guarana
from Human import Human
from Pine import Pine
from Sheep import Sheep
from Turtle import Turtle
from Wolf import Wolf
from Wolfberries import Wolfberries


class World:
    __NO_COLISION = 0
    __WON = 1
    __LOST = 2
    __REPRODUCE = 3
    __DRAW = 4
    __width = None
    __height = None
    __turn = None
    __population = None
    __organismToAdd = None
    __field = None
    __organisms = None
    __human = None
    __nextMove = None
    MAX_POPULATION = 1
    running = None
    screen = None
    pygame = None

    def __init__(self, width, height):
        self.__width = width
        self.__height = height
        self.__turn = 0
        self.__population = 0
        self.__nextMove = 0
        if self.__width <= 0 or self.__height <= 0:
            print("Wrong parameters")
            return
        else:
            self.__field = [[None for _ in range(width)] for _ in range(height)]
            self.__organisms = [None for _ in range((width * height) + 1)]
            self.MAX_POPULATION = width * height + 1

    def getHeight(self):
        return self.__height

    def getWidth(self):
        return self.__width

    def getPopulation(self):
        return self.__population

    def getField(self, x, y):
        return self.__field[y][x]

    def getHumanStrength(self):
        if self.__human is not None:
            return self.__human.getStrength()
        else:
            return "dead"

    def getHumanCooldown(self):
        if self.__human is not None:
            return self.__human.getCooldown()
        else:
            return "dead"

    def useHumanSkill(self):
        self.__human.useSkill()

    def getOrganism(self, i):
        return self.__organisms[i]

    def getNextMove(self):
        return self.__nextMove

    def getTurn(self):
        return self.__turn

    def setTurn(self, turn):
        self.__turn = turn

    def setInput(self):
        move = input()
        self.setNextMove(move)

    def asignHuman(self, human):
        self.__human = human

    def printGame(self):
        for y in range(self.getHeight()):
            for x in range(self.getWidth()):
                if self.__field[y][x] is None:
                    print(" ", end='', sep='')
                else:
                    self.__field[y][x].printSign()
            print('')

    def addOrganism(self, newOrganism):
        self.__organisms[self.getPopulation()] = newOrganism
        self.__population += 1

    def updateGameField(self):
        for y in range(self.getHeight()):
            for x in range(self.getWidth()):
                self.__field[y][x] = None

        for i in range(self.getPopulation()):
            if self.__organisms[i] is not None:
                posX = self.__organisms[i].getX()
                posY = self.__organisms[i].getY()
                self.__field[posY][posX] = self.__organisms[i]

    def playTurn(self):
        for i in range(self.getPopulation()):
            if self.__organisms[i] is not None and self.__organisms[i].getAge() > 0:
                self.__organisms[i].action()
                result = self.__NO_COLISION
                for j in range(self.getPopulation()):
                    if self.__organisms[j] is not None and self.__organisms[i] is not None and j != i:
                        if (self.__organisms[j].getNextX() == self.__organisms[i].getNextX()
                                and self.__organisms[j].getNextY() == self.__organisms[i].getNextY()):
                            result = self.__organisms[i].colision(self.__organisms[j])

                            if result == World.__WON:
                                self.__organisms[j] = None
                                if self.__organisms[i] is not None:
                                    self.__organisms[i].move()

                            elif result == World.__LOST:
                                self.__organisms[i] = None

                            elif result == World.__REPRODUCE:
                                self.__organisms[i].reproduce()
                                self.__organisms[i].stayInPlace()

                            elif result == World.__DRAW:
                                self.__organisms[i].stayInPlace()

                if result == self.__NO_COLISION:
                    self.__organisms[i].move()

                self.updateGameField()
        self.__turn += 1
        self.sortOrganisms()
        self.countOrganisms()
        self.updateGameField()
        self.ageAllOrganisms()
        self.printGame()

    def setNextMove(self, move):
        if move == 'a':
            self.__nextMove = 0
        elif move == 'w':
            self.__nextMove = 2
        elif move == 'd':
            self.__nextMove = 1
        elif move == 's':
            self.__nextMove = 3
        elif move == 'q':
            self.__human.useSkill()
        elif move == 'e':
            # self.save()
            pass

    def ageAllOrganisms(self):
        for i in range(self.getPopulation()):
            self.__organisms[i].agingProcess()

    def sortOrganisms(self):
        while True:
            change = 0
            for i in range(1, self.getPopulation(), 1):
                if self.__organisms[i] is not None:
                    if self.__organisms[i - 1] is None:
                        tmp = self.__organisms[i]
                        self.__organisms[i] = self.__organisms[i - 1]
                        self.__organisms[i - 1] = tmp
                        change = 1
                    elif self.__organisms[i].getInitiative() > self.__organisms[i - 1].getInitiative():
                        tmp = self.__organisms[i]
                        self.__organisms[i] = self.__organisms[i - 1]
                        self.__organisms[i - 1] = tmp
                        change = 1
                    elif (self.__organisms[i].getInitiative() == self.__organisms[i - 1].getInitiative()
                          and self.__organisms[i].getAge() > self.__organisms[i - 1].getAge()):
                        tmp = self.__organisms[i]
                        self.__organisms[i] = self.__organisms[i - 1]
                        self.__organisms[i - 1] = tmp
                        change = 1
            if change == 0:
                break

    def countOrganisms(self):
        self.__population = 0
        for i in range(self.getWidth() * self.getHeight()):
            if self.__organisms[i] is not None:
                self.__population += 1

    def kill(self, killX, killY):
        for i in range(self.__population):
            if (self.__organisms[i] is not None
                    and self.__organisms[i].getX() == killX
                    and self.__organisms[i].getY() == killY):
                self.__organisms[i] = None
                break

    def save(self):
        file = open('save.txt', 'w')
        file.writelines(str(self.getTurn()) + '\n')
        for i in range(self.__population):
            name = self.__organisms[i].getName()
            file.writelines(name + '\n')
            if name == 'human':
                file.writelines(str(self.getHumanCooldown()) + '\n')
            file.writelines(str(self.__organisms[i].getStrength()) + '\n')
            file.writelines(str(self.__organisms[i].getX()) + '\n')
            file.writelines(str(self.__organisms[i].getY()) + '\n')

    def load(self):
        self.__human = None
        for k in range(self.__population):
            self.__organisms[k] = None
        self.__population = 0
        file = open('save.txt', 'r')
        Lines = file.readline()
        self.setTurn(int(Lines))
        while True:
            Lines = file.readline()
            if Lines == "human\n":
                cooldown = int(file.readline())
                strength = int(file.readline())
                posX = int(file.readline())
                posY = int(file.readline())
                Human(posX, posY, cooldown, strength, self)
            elif Lines == 'antilope\n':
                strength = int(file.readline())
                posX = int(file.readline())
                posY = int(file.readline())
                Antilope(posX, posY, strength, self)
            elif Lines == 'cybersheep\n':
                strength = int(file.readline())
                posX = int(file.readline())
                posY = int(file.readline())
                CyberSheep(posX, posY, strength, self)
            elif Lines == 'dandelion\n':
                strength = int(file.readline())
                posX = int(file.readline())
                posY = int(file.readline())
                Dandelion(posX, posY, strength, self)
            elif Lines == 'fox\n':
                strength = int(file.readline())
                posX = int(file.readline())
                posY = int(file.readline())
                Fox(posX, posY, strength, self)
            elif Lines == 'grass\n':
                strength = int(file.readline())
                posX = int(file.readline())
                posY = int(file.readline())
                Grass(posX, posY, strength, self)
            elif Lines == 'guarana\n':
                strength = int(file.readline())
                posX = int(file.readline())
                posY = int(file.readline())
                Guarana(posX, posY, strength, self)
            elif Lines == 'pine\n':
                strength = int(file.readline())
                posX = int(file.readline())
                posY = int(file.readline())
                Pine(posX, posY, strength, self)
            elif Lines == 'sheep\n':
                strength = int(file.readline())
                posX = int(file.readline())
                posY = int(file.readline())
                Sheep(posX, posY, strength, self)
            elif Lines == 'turtle\n':
                strength = int(file.readline())
                posX = int(file.readline())
                posY = int(file.readline())
                Turtle(posX, posY, strength, self)
            elif Lines == 'wolf\n':
                strength = int(file.readline())
                posX = int(file.readline())
                posY = int(file.readline())
                Wolf(posX, posY, strength, self)
            elif Lines == 'wolfberries\n':
                strength = int(file.readline())
                posX = int(file.readline())
                posY = int(file.readline())
                Wolfberries(posX, posY, strength, self)
            elif Lines == '':
                break
