import pygame
import random
from datetime import datetime

pygame.init()
screenx = 1300
screeny = 900
screen = pygame.display.set_mode((screenx, screeny))
pygame.display.set_caption("Intersection")

done = False
roadWidth = 300
x = (screenx - roadWidth) / 2
y = (screeny - roadWidth) / 2
bandWidth = 15
bandLength = 70

# Car class
class car:
    radius = 10
    color = "blue"
    emergencyVehicle = False
    direction = [0, 0, 0]
    starting_time = -1
    xCoordinate = -1
    yCoordinate = -1
    speed = 5
    lane = -1
    outgoing = 1

    def __init__(self):
        randx = random.randint(0, 2)
        print(randx)
        self.direction[randx] = 1
        self.starting_time = datetime.now()
        self.lane = random.randint(1, 4)
        print(self.lane)
        if(self.lane == 1):
            self.xCoordinate = x + roadWidth - (roadWidth / 4)
            self.yCoordinate = 0
        elif(self.lane == 2):
            self.xCoordinate = screenx
            self.yCoordinate = y+roadWidth-(roadWidth/4)
        elif(self.lane == 3):
            self.xCoordinate = x + (roadWidth / 4)
            self.yCoordinate = screeny
        else:
            self.xCoordinate = 0
            self.yCoordinate = y + roadWidth/4

# To access those vars which are same for all cars
carConfig = car()


#Traffic light class
class trafficLights:
    state = 0
    color = ["red", "yellow", "green"]

    def __init__(self) -> None:
        pass


class lane:
    carsWaiting = 0
    emergencyVehicle = 0

    def score(carsWaiting, emergencyVehicle):
        x = emergencyVehicle * 3
        if carsWaiting + x == 0:
            return 0
        score = 1 / (carsWaiting + x)
        return score


# Lanes
class lane1(lane):
    def __init__(self) -> None:
        pass

    def score():
        return lane.score(lane1.carsWaiting, lane1.emergencyVehicle)


class lane2:
    carsWaiting = 0
    emergencyVehicle = 0


class lane3:
    carsWaiting = 0
    emergencyVehicle = 0


class lane4:
    carsWaiting = 0
    emergencyVehicle = 0

# Car obj
car1 = car()

#Text font
font = pygame.font.Font('freesansbold.ttf', 32)

while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

    # Grass and Roads
    pygame.draw.rect(screen, (102, 102, 102), (0, 0, screenx, screeny))
    pygame.draw.rect(screen, (0, 255, 0), (0, 0, x, y))
    pygame.draw.rect(screen, (0, 255, 0), (x + roadWidth, 0, screenx, y))
    pygame.draw.rect(screen, (0, 255, 0), (0, y + roadWidth, x, screeny))
    pygame.draw.rect(
        screen, (0, 255, 0), (x + roadWidth, y + roadWidth, screenx, screeny)
    )
    # Lane Text
    text1 = font.render('LANE 1',True,'White','Black')
    text2 = font.render('LANE 2',True,'White','Black')
    text3 = font.render('LANE 3',True,'White','Black')
    text4 = font.render('LANE 4',True,'White','Black')

    screen.blit(text1,(x+roadWidth,0))
    screen.blit(text2,(screenx-120,y-32))
    screen.blit(text3,(x+roadWidth,screeny-30))
    screen.blit(text4,(0,y-32))
    

    # Horizontal Bands
    for i in range(0, int(x), 120):
        if i + bandLength <= x:
            pygame.draw.rect(
                screen,
                (255, 255, 255),
                (i, y + roadWidth / 2 - bandWidth / 2, bandLength, bandWidth),
            )
    for i in range(int(x + roadWidth), screenx, 120):
        pygame.draw.rect(
            screen,
            (255, 255, 255),
            (i, y + roadWidth / 2 - bandWidth / 2, bandLength, bandWidth),
        )

    # Vertical Bands
    for i in range(0, int(y), 120):
        if i + bandLength <= y:
            pygame.draw.rect(
                screen,
                (255, 255, 255),
                (x + roadWidth / 2 - bandWidth / 2, i, bandWidth, bandLength),
            )
    for i in range(int(y + roadWidth), screenx, 120):
        pygame.draw.rect(
            screen,
            (255, 255, 255),
            (x + roadWidth / 2 - bandWidth / 2, i, bandWidth, bandLength),
        )

    pygame.draw.circle(
        screen, (0, 9, 255), (car1.xCoordinate, car1.yCoordinate), carConfig.radius
    )  # Render car in lane 1

    if car1.lane == 1 and car1.outgoing:
        car1.yCoordinate += carConfig.speed
    elif car1.lane == 2 and car1.outgoing:
        car1.xCoordinate -= carConfig.speed
    elif car1.lane == 3 and car1.outgoing:
        car1.yCoordinate -= carConfig.speed
    else:
        car1.xCoordinate += carConfig.speed

    pygame.display.flip()
