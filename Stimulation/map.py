import pygame
import random

# Initialize Pygame
pygame.init()

# Set up the game window
WIDTH = 800
HEIGHT = 600
window = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Intersection Traffic Simulator")

# Define colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

# Define road dimensions
ROAD_WIDTH = 80
ROAD_HEIGHT = HEIGHT

# Define traffic light dimensions
TRAFFIC_LIGHT_SIZE = 40
TRAFFIC_LIGHT_MARGIN = 20

# Define car dimensions
CAR_WIDTH = 20
CAR_HEIGHT = 40

# Define car speed
CAR_SPEED = 3

# Define intersection position
INTERSECTION_X = WIDTH // 2 - ROAD_WIDTH // 2
INTERSECTION_Y = 0

# Define scores
score = 0

# Create lists to store cars and traffic lights
cars = []
traffic_lights = []

clock = pygame.time.Clock()

# Function to spawn cars randomly
def spawn_car():
    side = random.choice(["left", "right", "top", "bottom"])
    if side == "left":
        car_x = -CAR_WIDTH
        car_y = random.randint(INTERSECTION_Y, INTERSECTION_Y + ROAD_HEIGHT - CAR_HEIGHT)
        car_vel_x = CAR_SPEED
        car_vel_y = 0
    elif side == "right":
        car_x = WIDTH
        car_y = random.randint(INTERSECTION_Y, INTERSECTION_Y + ROAD_HEIGHT - CAR_HEIGHT)
        car_vel_x = -CAR_SPEED
        car_vel_y = 0
    elif side == "top":
        car_x = random.randint(INTERSECTION_X, INTERSECTION_X + ROAD_WIDTH - CAR_WIDTH)
        car_y = -CAR_HEIGHT
        car_vel_x = 0
        car_vel_y = CAR_SPEED
    else:  # side == "bottom"
        car_x = random.randint(INTERSECTION_X, INTERSECTION_X + ROAD_WIDTH - CAR_WIDTH)
        car_y = HEIGHT
        car_vel_x = 0
        car_vel_y = -CAR_SPEED

    cars.append({"x": car_x, "y": car_y, "vel_x": car_vel_x, "vel_y": car_vel_y})

# Function to create traffic lights
def create_traffic_lights():
    traffic_lights.append(
        {"x": INTERSECTION_X - TRAFFIC_LIGHT_SIZE - TRAFFIC_LIGHT_MARGIN, "y": INTERSECTION_Y + ROAD_HEIGHT // 2 - TRAFFIC_LIGHT_SIZE // 2, "color": RED}
    )
    traffic_lights.append(
        {"x": INTERSECTION_X + ROAD_WIDTH + TRAFFIC_LIGHT_MARGIN, "y": INTERSECTION_Y + ROAD_HEIGHT // 2 - TRAFFIC_LIGHT_SIZE // 2, "color": GREEN}
    )

# Function to update car positions
def update_cars():
    for car in cars:
        car["x"] += car["vel_x"]
        car["y"] += car["vel_y"]

        if (
            car["x"] < INTERSECTION_X + ROAD_WIDTH
            and car["x"] + CAR_WIDTH > INTERSECTION_X
            and car["y"] < INTERSECTION_Y + ROAD_HEIGHT
            and car["y"] + CAR_HEIGHT > INTERSECTION_Y
        ):
            if is_traffic_light_red():
                # score
                car["vel_x"] = 0
                car["vel_y"] = 0

def is_traffic_light_red():
    return traffic_lights[0]["color"] == RED

def handle_events():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                change_traffic_lights()

def change_traffic_lights():
    for traffic_light in traffic_lights:
        if traffic_light["color"] == RED:
            traffic_light["color"] = GREEN
        else:
            traffic_light["color"] = RED

def draw_objects():
    # Clear the screen
    window.fill(BLACK)

    # Draw roads
    pygame.draw.rect(window, WHITE, (INTERSECTION_X, INTERSECTION_Y, ROAD_WIDTH, ROAD_HEIGHT))

    # Draw traffic lights
    for traffic_light in traffic_lights:
        pygame.draw.rect(window, traffic_light["color"], (traffic_light["x"], traffic_light["y"], TRAFFIC_LIGHT_SIZE, TRAFFIC_LIGHT_SIZE))

    # Draw cars
    for car in cars:
        pygame.draw.rect(window, BLUE, (car["x"], car["y"], CAR_WIDTH, CAR_HEIGHT))

    # Draw score
    font = pygame.font.SysFont(None, 30)
    score_text = font.render("Score: " + str(score), True, WHITE)
    window.blit(score_text, (10, 10))

    # Update the display
    pygame.display.flip()


running = True
create_traffic_lights()

while running:
    handle_events()

    if random.randint(0, 100) < 5:
        spawn_car()

    update_cars()

    draw_objects()

    # Remove cars that have left the screen
    cars = [car for car in cars if not (car["x"] < 0 or car["x"] > WIDTH or car["y"] < 0 or car["y"] > HEIGHT)]

    # Set the frame rate
    clock.tick(60)

# Quit the game
pygame.quit()

