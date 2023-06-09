import pygame
import random
import MainMenu

# Initialize Pygame
pygame.init()

# Set up the display
screen_width, screen_height = 800, 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Square Catcher")

# Define colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
DEFAULT_IMAGE_SIZE = (800, 600)

background = pygame.image.load("/Users/fsouza/Downloads/img.jpeg").convert()

background = pygame.transform.scale(background, DEFAULT_IMAGE_SIZE)

# Set up the clock
clock = pygame.time.Clock()

# Set up the font
font = pygame.font.Font(None, 36)

# Define the player block
block_width, block_height = 100, 20
block_x = screen_width // 2 - block_width // 2
block_y = screen_height - block_height - 10
block_speed = 5

# Define the falling square
square_width, square_height = 30, 30
square_x = random.randint(0, screen_width - square_width)
square_y = -square_height
square_speed = 3

# Game variables
score = 0

# Define the colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)

# Set the width and height of the screen
size = (800, 600)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Game Menu")

MainMenu.game_menu(screen)

# Game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    
    
    # Move the player block
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and block_x > 0:
        block_x -= block_speed
    if keys[pygame.K_RIGHT] and block_x < screen_width - block_width:
        block_x += block_speed

    # Move the falling square
    square_y += square_speed

    # Check collision
    if square_y + square_height >= block_y and block_x <= square_x + square_width <= block_x + block_width:
        # Square caught
        score += 1
        square_x = random.randint(0, screen_width - square_width)
        square_y = -square_height

    # Check if the square missed
    if square_y >= screen_height:
        # Square missed
        square_x = random.randint(0, screen_width - square_width)
        square_y = -square_height

    # Clear the screen
    screen.fill(BLACK)

    screen.blit(background, (0, 0))

    # Draw the player block
    pygame.draw.rect(screen, WHITE, (block_x, block_y, block_width, block_height))

    # Draw the falling square
    pygame.draw.rect(screen, RED, (square_x, square_y, square_width, square_height))

    # Display the score
    score_text = font.render("Score: " + str(score), True, WHITE)
    screen.blit(score_text, (10, 10))
    

    # Update the display
    pygame.display.flip()

    # Set the game's FPS
    clock.tick(100)

# Quit the game
pygame.quit()