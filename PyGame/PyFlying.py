import pygame
import random

WHITE = (255,255,255)
pad_width = 1024
pad_height = 512
backgound_width = 1024

gamepad = None
aircraft = None
clock = None
background1 = None
background2 = None
bat = None
fires = []


def drawObject(obj, x,y):
    global gamepad
    gamepad.blit(obj, (x,y))

def runGame():
    global gamepad, aircraft, clock, background1, background2, bat, fires

    x = pad_width * 0.05
    y = pad_height * 0.8
    y_change = 0

    background1_x = 0
    background2_x = backgound_width

    bat_x = pad_width
    bat_y = random.randrange(0, pad_height)

    fire_x = pad_width
    fire_y = random.randrange(0, pad_height)
    random.shuffle(fires)
    fire = fires[0]

    crashed = False

    while not crashed:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                crashed = True
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    y_change = -5
                elif event.key == pygame.K_DOWN:
                    y_change = 5
            elif event.type == pygame.KEYUP:
                if event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                    y_change = 0

        y += y_change
        gamepad.fill(WHITE)

        background1_x -= 2
        background2_x -= 2

        bat_x -= 7
        if bat_x <= 0:
            bat_x = pad_width
            bat_y = random.randrange(0, pad_height)
        
        if fire == None:
            fire_x -= 30
        else:
            fire_x -= 15

        if fire_x <= 0:
            fire_x = pad_width
            fire_y = random.randrange(0, pad_height)
            random.shuffle(fires)
            fire = fires[0]

        if background1_x == -backgound_width:
            background1_x = backgound_width

        if background2_x == -backgound_width:
            background2_x = backgound_width

        drawObject(background1, background1_x, 0)
        drawObject(background2, background2_x, 0)

        drawObject(bat, bat_x, bat_y)
        if fire != None:
            drawObject(fire, fire_x, fire_y)

        drawObject(aircraft, x, y)
        pygame.display.update()
        clock.tick(60)

    pygame.quit()
    quit()

def initGame():
    global gamepad, aircraft, clock, background1, background2, bat, fires

    pygame.init()
    gamepad = pygame.display.set_mode((pad_width, pad_height))
    pygame.display.set_caption('PyFlying')
    aircraft = pygame.image.load('PyGame/images/plane.png')
    background1 = pygame.image.load('PyGame/images/background.png')
    background2 = background1.copy()
    bat = pygame.image.load('PyGame/images/bat.png')
    fires.append(pygame.image.load('PyGame/images/fireball.png'))
    fires.append(pygame.image.load('PyGame/images/fireball2.png'))

    for i in range(5):
        fires.append(None)

    clock = pygame.time.Clock()
    runGame()

if __name__ == '__main__':
    initGame()
