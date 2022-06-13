import pygame

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
from World import World

#tasks
#save
#cyberowca patch
#load
#koniec

def createHUD(screenGame, worldGame, font):
    pygame.draw.rect(screenGame, (192, 192, 192), (0, worldGame.getHeight() * 40, worldGame.getWidth() * 40, 50))
    pygame.draw.rect(screenGame, (192, 192, 192), (worldGame.getWidth() * 40, 0, 100, worldGame.getHeight() * 40 + 50))
    pygame.draw.rect(screenGame, (179, 218, 241), (selectedAnimal * 50, worldGame.getHeight() * 40, 40, 50))
    pygame.draw.rect(screenGame, (209, 153, 31), (worldGame.getWidth() * 40, 0, 100, 50))
    pygame.draw.rect(screenGame, (65, 186, 142), (worldGame.getWidth() * 40, 50, 100, 50))
    pygame.draw.rect(screenGame, (211, 237, 14), (worldGame.getWidth() * 40, 100, 100, 50))
    pygame.draw.rect(screenGame, (191, 23, 62), (worldGame.getWidth() * 40, 150, 100, 50))
    pygame.draw.rect(screenGame, (14, 237, 65), (worldGame.getWidth() * 40, 200, 100, 50))
    turnDisplay = font.render('Turn: ' + str(worldGame.getTurn()), False, (0, 0, 0))
    strengthDisplay = font.render('Strength: ' + str(worldGame.getHumanStrength()), False, (0, 0, 0))
    if worldGame.getHumanCooldown() == 0:
        skillDisplay = font.render('Use Skill', False, (0, 0, 0))
    else:
        skillDisplay = font.render('Cooldown: ' + str(worldGame.getHumanCooldown()), False, (0, 0, 0))
    saveDisplay = font.render('Save game', False, (0, 0, 0))
    loadDisplay = font.render('Load game', False, (0, 0, 0))
    for k in range(worldGame.getWidth() + 1):
        pygame.draw.line(screenGame, (0, 0, 0), (k * 40, 0), (k * 40, worldGame.getHeight() * 40))
    for l in range(worldGame.getHeight() + 1):
        pygame.draw.line(screenGame, (0, 0, 0), (0, l * 40), (worldGame.getWidth() * 40, l * 40))
    pygame.draw.line(screenGame, (0, 0, 0), (world.getWidth() * 40, 50), (world.getWidth() * 40 + 100, 50))
    pygame.draw.line(screenGame, (0, 0, 0), (world.getWidth() * 40, 100), (world.getWidth() * 40 + 100, 100))
    pygame.draw.line(screenGame, (0, 0, 0), (world.getWidth() * 40, 150), (world.getWidth() * 40 + 100, 150))
    pygame.draw.line(screenGame, (0, 0, 0), (world.getWidth() * 40, 200), (world.getWidth() * 40 + 100, 200))
    pygame.draw.line(screenGame, (0, 0, 0), (world.getWidth() * 40, 250), (world.getWidth() * 40 + 100, 250))

    screenGame.blit(turnDisplay, (worldGame.getWidth() * 40 + 5, 15))
    screenGame.blit(strengthDisplay, (worldGame.getWidth() * 40 + 5, 65))
    screenGame.blit(skillDisplay, (worldGame.getWidth() * 40 + 5, 115))
    screenGame.blit(saveDisplay, (worldGame.getWidth() * 40 + 5, 165))
    screenGame.blit(loadDisplay, (worldGame.getWidth() * 40 + 5, 215))

    screenGame.blit(grassImage, (0, worldGame.getHeight() * 40 + 5))
    screenGame.blit(dandelionImage, (50, worldGame.getHeight() * 40 + 5))
    screenGame.blit(guaranaImage, (100, worldGame.getHeight() * 40 + 5))
    screenGame.blit(wolfberriesImage, (150, worldGame.getHeight() * 40 + 5))
    screenGame.blit(pineImage, (200, worldGame.getHeight() * 40 + 5))
    screenGame.blit(sheepImage, (250, worldGame.getHeight() * 40 + 5))
    screenGame.blit(wolfImage, (300, worldGame.getHeight() * 40 + 5))
    screenGame.blit(foxImage, (350, worldGame.getHeight() * 40 + 5))
    screenGame.blit(turtleImage, (400, worldGame.getHeight() * 40 + 5))
    screenGame.blit(antilopeImage, (450, worldGame.getHeight() * 40 + 5))
    screenGame.blit(cybersheepImage, (500, worldGame.getHeight() * 40 + 5))


if __name__ == '__main__':

    world = World(25, 14)
    hania = Human(5, 5, None, None, world)
    play = 0
    backgroundColor = (128, 140, 0)
    selectedAnimal = 0
    antilopeImage = pygame.image.load("antilope.png")
    cybersheepImage = pygame.image.load("cybersheep.png")
    dandelionImage = pygame.image.load("dandelion.png")
    foxImage = pygame.image.load("fox.png")
    grassImage = pygame.image.load("grass.png")
    guaranaImage = pygame.image.load("guarana.png")
    pineImage = pygame.image.load("pine.png")
    sheepImage = pygame.image.load("sheep.png")
    turtleImage = pygame.image.load("turtle.png")
    wolfImage = pygame.image.load("wolf.png")
    wolfberriesImage = pygame.image.load("wolfberries.png")
    grass = 0
    dandelion = 1
    guarana = 2
    wolfberries = 3
    pine = 4
    sheep = 5
    wolf = 6
    fox = 7
    turtle = 8
    antilope = 9
    cybersheep = 10

    pygame.init()
    screen = pygame.display.set_mode((world.getWidth() * 40 + 100, world.getHeight() * 40 + 50))
    pygame.display.set_caption("Virtual World - Adam Niesiobedzki 188641")
    myFont = pygame.font.SysFont('Comic Sans MS', 15)
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    world.setNextMove('a')
                    play = 1

                elif event.key == pygame.K_RIGHT:
                    world.setNextMove('d')
                    play = 1

                elif event.key == pygame.K_UP:
                    world.setNextMove('w')
                    play = 1

                elif event.key == pygame.K_DOWN:
                    world.setNextMove('s')
                    play = 1

                if play == 1:
                    world.playTurn()
                    play = 0

            if event.type == pygame.MOUSEBUTTONDOWN:
                if pygame.mouse.get_pressed()[0]:
                    mouseX, mouseY = pygame.mouse.get_pos()
                    if mouseY > world.getHeight() * 40 and mouseX < 550:
                        selectedAnimal = mouseX // 50
                    elif mouseX < world.getWidth() * 40:
                        if selectedAnimal == grass:
                            Grass(mouseX // 40, mouseY // 40, None, world)
                        elif selectedAnimal == dandelion:
                            Dandelion(mouseX // 40, mouseY // 40, None, world)
                        elif selectedAnimal == guarana:
                            Guarana(mouseX // 40, mouseY // 40, None, world)
                        elif selectedAnimal == wolfberries:
                            Wolfberries(mouseX // 40, mouseY // 40, None, world)
                        elif selectedAnimal == pine:
                            Pine(mouseX // 40, mouseY // 40, None, world)
                        elif selectedAnimal == sheep:
                            Sheep(mouseX // 40, mouseY // 40, None, world)
                        elif selectedAnimal == wolf:
                            Wolf(mouseX // 40, mouseY // 40, None, world)
                        elif selectedAnimal == fox:
                            Fox(mouseX // 40, mouseY // 40, None, world)
                        elif selectedAnimal == turtle:
                            Turtle(mouseX // 40, mouseY // 40, None, world)
                        elif selectedAnimal == antilope:
                            Antilope(mouseX // 40, mouseY // 40, None, world)
                        elif selectedAnimal == cybersheep:
                            CyberSheep(mouseX // 40, mouseY // 40, None, world)
                    elif mouseX > world.getWidth() * 40:
                        if 100 < mouseY < 150:
                            world.useHumanSkill()
                        elif 150 < mouseY < 200:
                            world.save()
                        elif 200 < mouseY < 250:
                            world.load()

            screen.fill(backgroundColor)
            for i in range(world.getPopulation()):
                organism = world.getOrganism(i)
                screen.blit(organism.image, (organism.getX() * 40, organism.getY() * 40))

            createHUD(screen, world, myFont)
            pygame.display.update()
