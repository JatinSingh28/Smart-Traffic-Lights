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
class carClass:
    radius = 10
    color = "blue"
    emergencyVehicle = False
    direction = -1  # left=0, right=1, straight=2
    starting_time = -1
    xCoordinate = -1
    yCoordinate = -1
    speed = 10
    lane = -1
    outgoing = True

    def __init__(self):
        self.direction = random.randint(0, 2)
        self.starting_time = datetime.now()
        self.lane = random.randint(1, 4)
        if self.lane == 1:
            self.xCoordinate = x + roadWidth - (roadWidth / 4)
            self.yCoordinate = 0
        elif self.lane == 2:
            self.xCoordinate = screenx
            self.yCoordinate = y + roadWidth - (roadWidth / 4)
        elif self.lane == 3:
            self.xCoordinate = x + (roadWidth / 4)
            self.yCoordinate = screeny
        else:
            self.xCoordinate = 0
            self.yCoordinate = y + roadWidth / 4


# To access those vars which are same for all cars
carConfig = carClass()


# Traffic light class
class trafficLightClass:
    state = 0  # red=0,yellow=1,green=2
    color = ["red", "yellow", "green"]

    def __init__(self) -> None:
        pass


class laneClass:
    carsWaiting = 0
    emergencyVehicle = 0

    def score(carsWaiting, emergencyVehicle):
        x = emergencyVehicle * 3
        if carsWaiting + x == 0:
            return 0
        score = 1 / (carsWaiting + x)
        return score


# Lanes
class lane1(laneClass, trafficLightClass):
    def __init__(self) -> None:
        pass

    def score():
        return laneClass.score(lane1.carsWaiting, lane1.emergencyVehicle)


class lane2(laneClass, trafficLightClass):
    def __init__(self) -> None:
        pass

    def score():
        return laneClass.score(lane2.carsWaiting, lane2.emergencyVehicle)


class lane3(laneClass, trafficLightClass):
    def __init__(self) -> None:
        pass

    def score():
        return laneClass.score(lane3.carsWaiting, lane3.emergencyVehicle)


class lane4(laneClass, trafficLightClass):
    def __init__(self) -> None:
        pass

    def score():
        return laneClass.score(lane4.carsWaiting, lane4.emergencyVehicle)


# Car obj
car1 = carClass()
car2 = carClass()

carArray = [car1, car2]


done = False
# Create Cars
event_id = 2828
pygame.time.set_timer(event_id, 1000)

# Text font
font = pygame.font.Font("freesansbold.ttf", 32)


while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        elif event.type == event_id:
            for i in range(2):
                carArray.append(carClass())

    # Grass and Roads
    pygame.draw.rect(screen, (129, 133, 137), (0, 0, screenx, screeny))
    pygame.draw.rect(screen, (0, 128, 0), (0, 0, x, y))
    pygame.draw.rect(screen, (0, 128, 0), (x + roadWidth, 0, screenx, y))
    pygame.draw.rect(screen, (0, 128, 0), (0, y + roadWidth, x, screeny))
    pygame.draw.rect(
        screen, (0, 128, 0), (x + roadWidth, y + roadWidth, screenx, screeny)
    )
    # Lane Text
    text1 = font.render("LANE 1", True, "White", "Black")
    text2 = font.render("LANE 2", True, "White", "Black")
    text3 = font.render("LANE 3", True, "White", "Black")
    text4 = font.render("LANE 4", True, "White", "Black")

    screen.blit(text1, (x + roadWidth, 0))
    screen.blit(text2, (screenx - 120, y - 32))
    screen.blit(text3, (x + roadWidth, screeny - 30))
    screen.blit(text4, (0, y - 32))

    # Render Traffic Lights
    # Lane 1
    if lane1.state == 0:
        pygame.draw.rect(
            screen, (255, 36, 0), (x + roadWidth / 2, y, roadWidth / 2, 25)
        )
    elif lane1.state == 1:
        pygame.draw.rect(
            screen, (255, 234, 0), (x + roadWidth / 2, y, roadWidth / 2, 25)
        )
    else:
        pygame.draw.rect(screen, (0, 0, 255), (x + roadWidth / 2, y, roadWidth / 2, 25))

    # Lane 2
    if lane2.state == 0:
        pygame.draw.rect(
            screen,
            (255, 36, 0),
            (x + roadWidth - 25, y + roadWidth / 2, 25, roadWidth / 2),
        )
    elif lane2.state == 1:
        pygame.draw.rect(
            screen, (255, 234, 0), (x + roadWidth - 25, y, 25, roadWidth / 2)
        )
    else:
        pygame.draw.rect(
            screen, (0, 0, 255), (x + roadWidth - 25, y, 25, roadWidth / 2)
        )

    # Lane 3
    if lane3.state == 0:
        pygame.draw.rect(
            screen, (255, 36, 0), (x, y + roadWidth - 25, roadWidth / 2, 25)
        )
    elif lane3.state == 1:
        pygame.draw.rect(
            screen, (255, 234, 0), (x, y + roadWidth - 25, roadWidth / 2, 25)
        )
    else:
        pygame.draw.rect(
            screen, (0, 0, 255), (x, y + roadWidth - 25, roadWidth / 2, 25)
        )

    # Lane 4
    if lane4.state == 0:
        pygame.draw.rect(screen, (255, 36, 0), (x, y, 25, roadWidth / 2))
    elif lane4.state == 1:
        pygame.draw.rect(screen, (255, 234, 0), (x, y, 25, roadWidth / 2))
    else:
        pygame.draw.rect(screen, (0, 0, 255), (x, y, 25, roadWidth / 2))

    # Horizontal Bands
    for i in range(int(x), 0, -120):
        # if i + bandLength <= x:
        pygame.draw.rect(
            screen,
            (255, 255, 255),
            (i - bandLength, y + roadWidth / 2 - bandWidth / 2, bandLength, bandWidth),
        )
    for i in range(int(x + roadWidth), screenx, 120):
        pygame.draw.rect(
            screen,
            (255, 255, 255),
            (i, y + roadWidth / 2 - bandWidth / 2, bandLength, bandWidth),
        )

    # Vertical Bands
    for i in range(int(y), 0, -120):
        pygame.draw.rect(
            screen,
            (255, 255, 255),
            (x + roadWidth / 2 - bandWidth / 2, i-bandLength, bandWidth, bandLength),
        )
    for i in range(int(y + roadWidth), screenx, 120):
        pygame.draw.rect(
            screen,
            (255, 255, 255),
            (x + roadWidth / 2 - bandWidth / 2, i, bandWidth, bandLength),
        )

    for car in carArray:
        pygame.draw.circle(
            screen, (0, 9, 255), (car.xCoordinate, car.yCoordinate), carConfig.radius
        )  # Render car in lane 1

        if (
            car.xCoordinate < 0
            or car.xCoordinate > screenx
            or car.yCoordinate < 0
            or car.yCoordinate > screeny
        ):
            carArray.remove(car)
        # Move Car
        if car.lane == 1:
            if car.outgoing:
                if car.direction == 0:
                    if car.yCoordinate >= y + roadWidth / 4:
                        car.outgoing = False
                elif car.direction == 1:
                    if car.yCoordinate >= y + roadWidth - roadWidth / 4:
                        car.outgoing = False
                car.yCoordinate += carConfig.speed
            else:
                if car.direction == 0:
                    car.xCoordinate += carConfig.speed
                elif car.direction == 1:
                    car.xCoordinate -= carConfig.speed
                else:
                    car.yCoordinate += carConfig.speed
        elif car.lane == 2:
            if car.outgoing:
                if car.direction == 0:
                    if car.xCoordinate <= x + roadWidth - roadWidth / 4:
                        car.outgoing = False
                elif car.direction == 1:
                    if car.xCoordinate <= x + roadWidth / 4:
                        car.outgoing = False
                car.xCoordinate -= carConfig.speed
            else:
                if car.direction == 0:
                    car.yCoordinate += carConfig.speed
                elif car.direction == 1:
                    car.yCoordinate -= carConfig.speed
                else:
                    car.yCoordinate += carConfig.speed
        elif car.lane == 3:
            if car.outgoing:
                if car.direction == 0:
                    if car.yCoordinate <= y + roadWidth / 4:
                        car.outgoing = False
                elif car.direction == 1:
                    if car.yCoordinate <= y + roadWidth - roadWidth / 4:
                        car.outgoing = False
                car.yCoordinate -= carConfig.speed
            else:
                if car.direction == 0:
                    car.xCoordinate -= carConfig.speed
                elif car.direction == 1:
                    car.xCoordinate += carConfig.speed
                else:
                    car.yCoordinate -= carConfig.speed
        else:
            if car.outgoing:
                if car.direction == 0:
                    if car.xCoordinate >= x + roadWidth / 4:
                        car.outgoing = False
                elif car.direction == 1:
                    if car.xCoordinate >= x + roadWidth - roadWidth / 4:
                        car.outgoing = False
                car.xCoordinate += carConfig.speed
            else:
                if car.direction == 0:
                    car.yCoordinate -= carConfig.speed
                elif car.direction == 1:
                    car.yCoordinate += carConfig.speed
                else:
                    car.xCoordinate += carConfig.speed

    pygame.display.flip()
