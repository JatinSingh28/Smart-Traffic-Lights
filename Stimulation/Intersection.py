import pygame
from car import carClass
from Lanes import lane1, lane2, lane3, lane4

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


def renderSimulation():
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
    score1 = font.render(str(round(lane1.score(), 3)), True, "White", "Black")
    # carw1 = font.render(str(lane1.carsWaiting),True,'White','Black')
    text2 = font.render("LANE 2", True, "White", "Black")
    score2 = font.render(str(round(lane2.score(), 3)), True, "White", "Black")
    text3 = font.render("LANE 3", True, "White", "Black")
    score3 = font.render(str(round(lane3.score(), 3)), True, "White", "Black")
    text4 = font.render("LANE 4", True, "White", "Black")
    score4 = font.render(str(round(lane4.score(), 3)), True, "White", "Black")
    score = font.render(
        "Score: "
        + str(round(lane1.score() + lane2.score() + lane3.score() + lane4.score(), 3)),
        True,
        "White",
        "Black",
    )

    screen.blit(text1, (x + roadWidth, 0))
    screen.blit(score1, (x + roadWidth, 30))
    # screen.blit(carw1, (x + roadWidth, 60))
    screen.blit(text2, (screenx - 120, y + roadWidth))
    screen.blit(score2, (screenx - 120, y + roadWidth + 30))
    screen.blit(text3, (x - 120, screeny - 30))
    screen.blit(score3, (x - 120, screeny - 60))
    screen.blit(text4, (0, y - 32))
    screen.blit(score4, (0, y - 60))
    screen.blit(score, (0, 0))

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
        pygame.draw.rect(
            screen, (124, 252, 0), (x + roadWidth / 2, y, roadWidth / 2, 25)
        )

    # Lane 2
    if lane2.state == 0:
        pygame.draw.rect(
            screen,
            (255, 36, 0),
            (x + roadWidth - 25, y + roadWidth / 2, 25, roadWidth / 2),
        )
    elif lane2.state == 1:
        pygame.draw.rect(
            screen,
            (255, 234, 0),
            (x + roadWidth - 25, y + roadWidth / 2, 25, roadWidth / 2),
        )
    else:
        pygame.draw.rect(
            screen,
            (124, 252, 0),
            (x + roadWidth - 25, y + roadWidth / 2, 25, roadWidth / 2),
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
            screen, (124, 252, 0), (x, y + roadWidth - 25, roadWidth / 2, 25)
        )

    # Lane 4
    if lane4.state == 0:
        pygame.draw.rect(screen, (255, 36, 0), (x, y, 25, roadWidth / 2))
    elif lane4.state == 1:
        pygame.draw.rect(screen, (255, 234, 0), (x, y, 25, roadWidth / 2))
    else:
        pygame.draw.rect(screen, (124, 252, 0), (x, y, 25, roadWidth / 2))

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
            (x + roadWidth / 2 - bandWidth / 2, i - bandLength, bandWidth, bandLength),
        )
    for i in range(int(y + roadWidth), screenx, 120):
        pygame.draw.rect(
            screen,
            (255, 255, 255),
            (x + roadWidth / 2 - bandWidth / 2, i, bandWidth, bandLength),
        )


def renderCar(car):
    if not car.emergencyVehicle:
        pygame.draw.circle(
            screen,
            (0, 9, 255),
            (car.xCoordinate, car.yCoordinate),
            carConfig.radius,
        )  # Render car
    else:
        pygame.draw.circle(
            screen,
            (136, 8, 8),
            (car.xCoordinate, car.yCoordinate),
            carConfig.radius,
        )

    if (
        car.xCoordinate < 0
        or car.xCoordinate > screenx
        or car.yCoordinate < 0
        or car.yCoordinate > screeny
    ):
        carArray.remove(car)


def moveCar(car):
    # Move Car
    if car.lane == 1:
        if car.outgoing:
            if car.yCoordinate <= y and lane1.state == 0:
                if car.yCoordinate + carConfig.speed < lane1.lastCar:
                    car.yCoordinate += carConfig.speed
                else:
                    lane1.lastCar = car.yCoordinate - car.radius
            else:
                car.yCoordinate += carConfig.speed
            if lane1.state != 0:
                car.yCoordinate += carConfig.speed
                if not car.crossed and car.yCoordinate > y + 5:
                    lane1.carsWaiting -= 1
                    car.crossed = True
                if car.direction == 0:
                    if car.yCoordinate >= y + roadWidth / 4:
                        car.outgoing = False
                elif car.direction == 1:
                    if car.yCoordinate >= y + roadWidth - roadWidth / 4:
                        car.outgoing = False

        else:
            if car.direction == 0:
                car.xCoordinate += carConfig.speed
            elif car.direction == 1:
                car.xCoordinate -= carConfig.speed
            else:
                car.yCoordinate += carConfig.speed
                if not car.crossed and car.yCoordinate > y + 5:
                    lane1.carsWaiting -= 1
                    car.crossed = True
    elif car.lane == 2:
        if car.outgoing:
            if car.xCoordinate >= x + roadWidth and lane2.state == 0:
                if car.xCoordinate - carConfig.speed > lane2.lastCar:
                    car.xCoordinate -= carConfig.speed

                else:
                    lane2.lastCar = car.xCoordinate + car.radius
            else:
                car.xCoordinate -= carConfig.speed

            if lane2.state != 0:
                car.xCoordinate -= carConfig.speed
                if not car.crossed and car.xCoordinate <= x + roadWidth - 5:
                    lane2.carsWaiting -= 1
                    car.crossed = True
                if car.direction == 0:
                    if car.xCoordinate <= x + roadWidth - roadWidth / 4:
                        car.outgoing = False
                elif car.direction == 1:
                    if car.xCoordinate <= x + roadWidth / 4:
                        car.outgoing = False
        else:
            if car.direction == 0:
                car.yCoordinate += carConfig.speed
            elif car.direction == 1:
                car.yCoordinate -= carConfig.speed
            else:
                car.yCoordinate += carConfig.speed
    elif car.lane == 3:
        if car.outgoing:
            if car.yCoordinate >= y + roadWidth and lane3.state == 0:
                if car.yCoordinate - carConfig.speed > lane3.lastCar:
                    car.yCoordinate -= carConfig.speed

                else:
                    lane3.lastCar = car.yCoordinate + car.radius

            else:
                car.yCoordinate -= carConfig.speed

            if lane3.state != 0:
                car.yCoordinate -= carConfig.speed
                if not car.crossed and car.yCoordinate <= y + roadWidth - 5:
                    lane3.carsWaiting -= 1
                    car.crossed = True
                if car.direction == 0:
                    if car.yCoordinate <= y + roadWidth / 4:
                        car.outgoing = False
                elif car.direction == 1:
                    if car.yCoordinate <= y + roadWidth - roadWidth / 4:
                        car.outgoing = False
        else:
            if car.direction == 0:
                car.xCoordinate -= carConfig.speed
            elif car.direction == 1:
                car.xCoordinate += carConfig.speed
            else:
                car.yCoordinate -= carConfig.speed
    else:
        if car.outgoing:
            if car.xCoordinate <= x and lane4.state == 0:
                if car.xCoordinate + carConfig.speed < lane4.lastCar:
                    car.xCoordinate += carConfig.speed

                else:
                    lane4.lastCar = car.xCoordinate - car.radius
            else:
                car.xCoordinate += carConfig.speed

            if lane4.state != 0:
                car.xCoordinate += carConfig.speed
                if not car.crossed and car.xCoordinate >= x + 5:
                    lane4.carsWaiting -= 1
                    car.crossed = True
                if car.direction == 0:
                    if car.xCoordinate >= x + roadWidth / 4:
                        car.outgoing = False
                elif car.direction == 1:
                    if car.xCoordinate >= x + roadWidth - roadWidth / 4:
                        car.outgoing = False

        else:
            if car.direction == 0:
                car.yCoordinate -= carConfig.speed
            elif car.direction == 1:
                car.yCoordinate += carConfig.speed
            else:
                car.xCoordinate += carConfig.speed


def signalChange(event):
    if event.key == pygame.K_q:
        lane1.changeState(lane1, 1, 0, 0)
    elif event.key == pygame.K_w:
        lane1.changeState(lane1, 0, 1, 0)
    elif event.key == pygame.K_e:
        lane1.changeState(lane1, 0, 0, 1)
        lane1.lastCar = y
    elif event.key == pygame.K_a:
        lane2.changeState(lane2, 1, 0, 0)
    elif event.key == pygame.K_s:
        lane2.changeState(lane2, 0, 1, 0)
    elif event.key == pygame.K_d:
        lane2.changeState(lane2, 0, 0, 1)
        lane2.lastCar = x + roadWidth
    elif event.key == pygame.K_z:
        lane3.changeState(lane3, 1, 0, 0)
    elif event.key == pygame.K_x:
        lane3.changeState(lane3, 0, 1, 0)
    elif event.key == pygame.K_c:
        lane3.changeState(lane3, 0, 0, 1)
        lane3.lastCar = y + roadWidth
    elif event.key == pygame.K_1:
        lane4.changeState(lane4, 1, 0, 0)
    elif event.key == pygame.K_2:
        lane4.changeState(lane4, 0, 1, 0)
    elif event.key == pygame.K_3:
        lane4.changeState(lane4, 0, 0, 1)
        lane4.lastCar = x


# # To access those vars which are same for all cars
carConfig = carClass(0)

# Car Array
carArray = []


done = False
# Create Cars
event_id = 2828
ev_event_id = 112


pygame.time.set_timer(event_id, 1000)  # event id for cars
pygame.time.set_timer(ev_event_id, 10000)  # event id for emergency vehicles

# Text font
font = pygame.font.Font("freesansbold.ttf", 32)


while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        elif event.type == event_id:
            for i in range(2):
                carObj = carClass(0)
                if carObj.lane == 1:
                    lane1.carsWaiting += 1
                elif carObj.lane == 2:
                    lane2.carsWaiting += 1
                elif carObj.lane == 3:
                    lane3.carsWaiting += 1
                else:
                    lane4.carsWaiting += 1
                carArray.append(carObj)
        elif event.type == ev_event_id:
            carObj = carClass(1)
            if carObj.lane == 1:
                lane1.carsWaiting += 1
            elif carObj.lane == 2:
                lane2.carsWaiting += 1
            elif carObj.lane == 3:
                lane3.carsWaiting += 1
            else:
                lane4.carsWaiting += 1
            carArray.append(carObj)
        elif event.type == pygame.KEYDOWN:
            signalChange(event)

    # Draw Simulation
    renderSimulation()

    for car in carArray:
        renderCar(car)
        moveCar(car)

    pygame.display.flip()
