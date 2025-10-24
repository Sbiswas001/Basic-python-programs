import pygame
import random

# Initialize Pygame
pygame.init()

# Screen dimensions
WIDTH, HEIGHT = 400, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Flappy Bird")

# Colors
WHITE = (255, 255, 255)
GREEN = (0, 200, 0)
BLUE = (135, 206, 250)

# Game variables
GRAVITY = 0.5
BIRD_JUMP = -10
PIPE_GAP = 170
PIPE_WIDTH = 70
PIPE_SPEED = 3

# Load bird image
bird_img = pygame.image.load("transparent-phoenix-fire-sun-feathers-colorful-colorful-phoenix-surrounded-by-flames-vibrant-1710898077754.webp")  # Add a small bird image in the same folder
bird_img = pygame.transform.scale(bird_img, (40, 30))

# Bird properties
bird_x, bird_y = 50, HEIGHT // 2
bird_velocity = 0

# Pipes list
pipes = []

def create_pipe():
    """Creates a new pipe with a random gap position."""
    gap_start = random.randint(100, 400)
    pipes.append({"x": WIDTH, "top": gap_start - PIPE_GAP//2, "bottom": gap_start + PIPE_GAP//2})

def move_pipes():
    """Moves pipes left and removes old ones."""
    global pipes
    for pipe in pipes:
        pipe["x"] -= PIPE_SPEED
    pipes = [pipe for pipe in pipes if pipe["x"] > -PIPE_WIDTH]

def check_collision():
    """Checks if the bird collides with pipes or the ground."""
    for pipe in pipes:
        if bird_x < pipe["x"] + PIPE_WIDTH and bird_x + 40 > pipe["x"]:
            if bird_y < pipe["top"] or bird_y + 30 > pipe["bottom"]:
                return True
    return bird_y > HEIGHT - 30 or bird_y < 0  # Ground & ceiling collision

# Main game loop
clock = pygame.time.Clock()
running = True
frame_count = 0

while running:
    screen.fill(BLUE)

    # Event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
            bird_velocity = BIRD_JUMP

    # Bird physics
    bird_velocity += GRAVITY
    bird_y += bird_velocity

    # Generate pipes
    if frame_count % 90 == 0:
        create_pipe()

    move_pipes()

    # Draw bird
    screen.blit(bird_img, (bird_x, bird_y))

    # Draw pipes
    for pipe in pipes:
        pygame.draw.rect(screen, GREEN, (pipe["x"], 0, PIPE_WIDTH, pipe["top"]))  # Top pipe
        pygame.draw.rect(screen, GREEN, (pipe["x"], pipe["bottom"], PIPE_WIDTH, HEIGHT - pipe["bottom"]))  # Bottom pipe

    # Collision check
    if check_collision():
        running = False

    frame_count += 1
    pygame.display.update()
    clock.tick(30)

pygame.quit()
