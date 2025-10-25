import pygame
import time
import random

# Initialize pygame
pygame.init()

# Define colors
white = (255, 255, 255)
yellow = (255, 255, 102)
black = (0, 0, 0)
red = (213, 50, 80)
green = (0, 255, 0)
blue = (50, 153, 213)

# Set up the display dimensions
dis_width = 600
dis_height = 400
dis = pygame.display.set_mode((dis_width, dis_height))
pygame.display.set_caption('Snake Game by Gemini')

# Clock for controlling game speed
clock = pygame.time.Clock()

# Snake properties
snake_block = 10
snake_speed = 15

# Font styles
font_style = pygame.font.SysFont("bahnschrift", 25)
score_font = pygame.font.SysFont("comicsansms", 35)


def Your_score(score):
    """Displays the current score on the screen."""
    value = score_font.render("Your Score: " + str(score), True, yellow)
    dis.blit(value, [0, 0])


def our_snake(snake_block, snake_list):
    """Draws the snake on the screen."""
    for x in snake_list:
        pygame.draw.rect(dis, green, [x[0], x[1], snake_block, snake_block])


def message(msg, color):
    """Displays a message in the center of the screen."""
    mesg = font_style.render(msg, True, color)
    # Get text dimensions to center it
    text_rect = mesg.get_rect(center=(dis_width / 2, dis_height / 2))
    dis.blit(mesg, text_rect)


def gameLoop():
    """The main function containing the game loop."""
    game_over = False
    game_close = False

    # Initial position of the snake (center of the screen)
    x1 = dis_width / 2
    y1 = dis_height / 2

    # Change in position
    x1_change = 0
    y1_change = 0

    # Snake body
    snake_List = []
    Length_of_snake = 1

    # Generate initial food
    foodx = round(random.randrange(0, dis_width - snake_block) / 10.0) * 10.0
    foody = round(random.randrange(0, dis_height - snake_block) / 10.0) * 10.0

    # --- Main Game Loop ---
    while not game_over:

        # --- "Game Over" Screen Loop ---
        while game_close:
            dis.fill(black)
            message("You Lost! Press C-Play Again or Q-Quit", red)
            Your_score(Length_of_snake - 1)
            pygame.display.update()

            # Check for user input to quit or restart
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        game_over = True
                        game_close = False
                    if event.key == pygame.K_c:
                        gameLoop()  # Restart the game

        # --- Event Handling (Key Presses) ---
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    # Prevent 180-degree turns
                    if x1_change == 0:
                        x1_change = -snake_block
                        y1_change = 0
                elif event.key == pygame.K_RIGHT:
                    if x1_change == 0:
                        x1_change = snake_block
                        y1_change = 0
                elif event.key == pygame.K_UP:
                    if y1_change == 0:
                        y1_change = -snake_block
                        x1_change = 0
                elif event.key == pygame.K_DOWN:
                    if y1_change == 0:
                        y1_change = snake_block
                        x1_change = 0

        # --- Game Logic ---

        # Check for wall collisions
        if x1 >= dis_width or x1 < 0 or y1 >= dis_height or y1 < 0:
            game_close = True
        
        # Update snake's position
        x1 += x1_change
        y1 += y1_change

        # --- Drawing ---
        dis.fill(black)
        pygame.draw.rect(dis, red, [foodx, foody, snake_block, snake_block])
        
        # Update snake body list
        snake_Head = []
        snake_Head.append(x1)
        snake_Head.append(y1)
        snake_List.append(snake_Head)
        
        # Remove the tail if the snake hasn't eaten
        if len(snake_List) > Length_of_snake:
            del snake_List[0]

        # Check for self-collision
        for x in snake_List[:-1]:
            if x == snake_Head:
                game_close = True

        # Draw the snake
        our_snake(snake_block, snake_List)
        # Display the score
        Your_score(Length_of_snake - 1)

        # Update the display
        pygame.display.update()

        # Check for food collision
        if x1 == foodx and y1 == foody:
            # Generate new food
            foodx = round(random.randrange(0, dis_width - snake_block) / 10.0) * 10.0
            foody = round(random.randrange(0, dis_height - snake_block) / 10.0) * 10.0
            Length_of_snake += 1

        # Control the game speed
        clock.tick(snake_speed)

    # Quit pygame and Python
    pygame.quit()
    quit()


# Start the game
gameLoop()
