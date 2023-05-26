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
carConfig = car()


# Traffic light class
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