from TrafficLights import trafficLightClass
import Info


class laneClass(trafficLightClass):
    carsWaiting = 0
    emergencyVehicle = 0

    def score(carsWaiting, emergencyVehicle):
        x = emergencyVehicle * 5
        if carsWaiting + x == 0:
            return 100
        score = 1 / (carsWaiting + x) * 100
        return score

    def changeState(self, red=False, yellow=False, green=False):
        if red:
            self.state = 0
        elif yellow:
            self.state = 1
        else:
            self.state = 2


# Lanes
class lane1(laneClass, trafficLightClass):
    lastCar = Info.y
    # state = 0

    def __init__(self) -> None:
        pass

    def score():
        return laneClass.score(lane1.carsWaiting, lane1.emergencyVehicle)

    # def changeState(self, red=False, yellow=False, green=False):
    #     if red:
    #         self.state = 0
    #     elif yellow:
    #         self.state = 1
    #     else:
    #         self.state = 2


class lane2(laneClass, trafficLightClass):
    lastCar = Info.x + Info.roadWidth
    # state = 0

    def __init__(self) -> None:
        pass

    def score():
        return laneClass.score(lane2.carsWaiting, lane2.emergencyVehicle)

    # def changeState(self, red=False, yellow=False, green=False):
    #     if red:
    #         self.state = 0
    #     elif yellow:
    #         self.state = 1
    #     else:
    #         self.state = 2


class lane3(laneClass, trafficLightClass):
    lastCar = Info.y + Info.roadWidth
    # state = 0

    def __init__(self) -> None:
        pass

    def score():
        return laneClass.score(lane3.carsWaiting, lane3.emergencyVehicle)

    # def changeState(self, red=False, yellow=False, green=False):
    #     if red:
    #         self.state = 0
    #     elif yellow:
    #         self.state = 1
    #     else:
    #         self.state = 2


class lane4(laneClass, trafficLightClass):
    lastCar = Info.x
    state = 0

    def __init__(self) -> None:
        pass

    def score():
        return laneClass.score(lane4.carsWaiting, lane4.emergencyVehicle)

    # def changeState(self, red=False, yellow=False, green=False):
    #     if red:
    #         self.state = 0
    #     elif yellow:
    #         self.state = 1
    #     else:
    #         self.state = 2
