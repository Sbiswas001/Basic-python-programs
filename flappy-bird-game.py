import pygame
import random

# --- Initialize Pygame ---
pygame.init()

# --- Game Constants ---
SCREEN_WIDTH = 400
SCREEN_HEIGHT = 600
FPS = 60

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
SKY_BLUE = (135, 206, 235)
GREEN = (50, 205, 50)
DARK_GREEN = (0, 100, 0)
BROWN = (210, 180, 140)
YELLOW = (255, 255, 0)
RED = (213, 50, 80)

# Bird properties
BIRD_WIDTH = 40
BIRD_HEIGHT = 30
BIRD_X = 50
GRAVITY = 0.5
FLAP_STRENGTH = -9

# Pipe properties
PIPE_WIDTH = 70
PIPE_GAP = 150
PIPE_SPEED = 3
PIPE_SPAWN_TIME = 1200  # milliseconds

# Ground
GROUND_HEIGHT = 50

# --- Game Setup ---
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Flappy Bird - Python")
clock = pygame.time.Clock()

# Fonts
score_font = pygame.font.SysFont("comicsansms", 40)
message_font = pygame.font.SysFont("bahnschrift", 25)

# Background image (optional)
try:
    background = pygame.image.load("background.png")
    background = pygame.transform.scale(background, (SCREEN_WIDTH, SCREEN_HEIGHT))
except:
    background = None  # fallback to solid color


# --- Utility Functions ---
def draw_gradient_background():
    """Draws a simple vertical gradient sky."""
    for y in range(SCREEN_HEIGHT):
        color = (135 - y // 15, 206 - y // 15, 235)
        pygame.draw.line(screen, color, (0, y), (SCREEN_WIDTH, y))


def draw_bird(x, y):
    """Draws the bird (a yellow rect)."""
    bird_rect = pygame.Rect(x, y, BIRD_WIDTH, BIRD_HEIGHT)
    pygame.draw.rect(screen, YELLOW, bird_rect, border_radius=6)
    pygame.draw.rect(screen, BLACK, bird_rect, 2, border_radius=6)
    return bird_rect


def create_pipe():
    """Creates a top and bottom pipe."""
    random_pipe_height = random.randint(120, 400)
    top_pipe = pygame.Rect(SCREEN_WIDTH, 0, PIPE_WIDTH, random_pipe_height)
    bottom_pipe_y = random_pipe_height + PIPE_GAP
    bottom_pipe = pygame.Rect(SCREEN_WIDTH, bottom_pipe_y, PIPE_WIDTH,
                              SCREEN_HEIGHT - bottom_pipe_y - GROUND_HEIGHT)
    return top_pipe, bottom_pipe


def move_pipes(pipe_pairs):
    """Moves all pipes to the left."""
    new_pipes = []
    for top, bottom in pipe_pairs:
        top.centerx -= PIPE_SPEED
        bottom.centerx -= PIPE_SPEED
        if top.right > 0:
            new_pipes.append((top, bottom))
    return new_pipes


def draw_pipes(pipe_pairs):
    """Draws all pipe pairs."""
    for top, bottom in pipe_pairs:
        pygame.draw.rect(screen, GREEN, top)
        pygame.draw.rect(screen, GREEN, bottom)
        pygame.draw.rect(screen, DARK_GREEN, top, 3)
        pygame.draw.rect(screen, DARK_GREEN, bottom, 3)


def check_collision(bird_rect, pipe_pairs):
    """Checks for collision with pipes or ground/ceiling."""
    for top, bottom in pipe_pairs:
        if bird_rect.colliderect(top) or bird_rect.colliderect(bottom):
            return True
    if bird_rect.bottom >= SCREEN_HEIGHT - GROUND_HEIGHT or bird_rect.top <= 0:
        return True
    return False


def update_score(score, bird_rect, pipe_pairs, passed_pipes):
    """Update score when passing a pipe."""
    for top, bottom in pipe_pairs:
        if top not in passed_pipes and bird_rect.centerx > top.centerx:
            passed_pipes.add(top)
            score += 1
    return score, passed_pipes


def display_text(text, y, font, color=BLACK):
    """Center display helper."""
    rendered = font.render(text, True, color)
    rect = rendered.get_rect(center=(SCREEN_WIDTH // 2, y))
    screen.blit(rendered, rect)


def main_game():
    """Main Flappy Bird loop with restart support."""
    high_score = 0

    while True:  # Outer loop for restart
        # --- Reset Game State ---
        bird_y = SCREEN_HEIGHT // 2
        bird_y_velocity = 0
        pipe_pairs = []
        passed_pipes = set()
        score = 0
        game_active = False
        game_over = False

        pygame.time.set_timer(pygame.USEREVENT, PIPE_SPAWN_TIME)

        # --- Inner Loop (Game Frame) ---
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    return

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                        if not game_active and not game_over:
                            game_active = True
                            bird_y_velocity = FLAP_STRENGTH  # initial flap
                        elif game_active:
                            bird_y_velocity = FLAP_STRENGTH
                        elif game_over:
                            # restart the game (break inner loop, restart outer)
                            break

                if event.type == pygame.USEREVENT and game_active:
                    pipe_pairs.append(create_pipe())

            else:
                # --- Drawing ---
                if background:
                    screen.blit(background, (0, 0))
                else:
                    draw_gradient_background()

                if game_active:
                    # Physics
                    bird_y_velocity += GRAVITY
                    bird_y += bird_y_velocity
                    bird_rect = draw_bird(BIRD_X, bird_y)

                    # Pipe Logic
                    pipe_pairs = move_pipes(pipe_pairs)
                    draw_pipes(pipe_pairs)

                    # Collision
                    if check_collision(bird_rect, pipe_pairs):
                        game_active = False
                        game_over = True
                        high_score = max(high_score, score)

                    # Scoring
                    score, passed_pipes = update_score(score, bird_rect, pipe_pairs, passed_pipes)
                    display_text(str(score), 50, score_font, WHITE)

                elif game_over:
                    display_text("GAME OVER", SCREEN_HEIGHT // 2 - 60, message_font, RED)
                    display_text(f"Score: {score}", SCREEN_HEIGHT // 2, message_font)
                    display_text(f"High Score: {high_score}", SCREEN_HEIGHT // 2 + 30, message_font)
                    display_text("Press SPACE to Restart", SCREEN_HEIGHT // 2 + 80, message_font)

                else:
                    draw_bird(BIRD_X, SCREEN_HEIGHT // 2)
                    display_text("Press SPACE to Start", SCREEN_HEIGHT // 2, message_font)

                # Draw ground
                pygame.draw.rect(screen, BROWN,
                                 (0, SCREEN_HEIGHT - GROUND_HEIGHT, SCREEN_WIDTH, GROUND_HEIGHT))
                pygame.draw.rect(screen, DARK_GREEN,
                                 (0, SCREEN_HEIGHT - GROUND_HEIGHT, SCREEN_WIDTH, 10))

                pygame.display.update()
                clock.tick(FPS)
                continue  # continue inner while
            break  # break triggered only by restart

# --- Run the Game ---
if __name__ == "__main__":
    main_game()
