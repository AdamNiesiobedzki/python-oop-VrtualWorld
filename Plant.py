from Organism import Organism
import random


class Plant(Organism):
    _CHANCE_TO_REPRODUCE = 1
    _PLANT_INITIATIVE = 0

    def __init__(self, world, strength, posX, posY, name, image):
        super().__init__(world, strength, Plant._PLANT_INITIATIVE, posX, posY, name, image)

    def action(self):
        self._hasMoved = True
        reproduce = random.randint(0, 15)
        if reproduce < Plant._CHANCE_TO_REPRODUCE:
            self.reproduce()
