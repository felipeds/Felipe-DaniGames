import pygame

# Define colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
DEFAULT_IMAGE_SIZE = (800, 600)

# Set the width and height of the screen
size = (800, 600)
# Game menu loop
def game_menu(screen):
    menu = True

    while menu:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_q:
                    pygame.quit()
                    sys.exit()

            # Clear the screen
            screen.fill(BLACK)

            # Draw title text
            font = pygame.font.Font(None, 100)
            title_text = font.render("Game Menu", True, WHITE)
            title_text_rect = title_text.get_rect(center=(size[0] // 2, size[1] // 4))
            screen.blit(title_text, title_text_rect)

            # Draw menu options
            font = pygame.font.Font(None, 50)
            option1_text = font.render("Start Game", True, WHITE)
            option1_text_rect = option1_text.get_rect(center=(size[0] // 2, size[1] // 2))
            screen.blit(option1_text, option1_text_rect)

            option2_text = font.render("Exit", True, WHITE)
            option2_text_rect = option2_text.get_rect(center=(size[0] // 2, size[1] // 2 + 100))
            screen.blit(option2_text, option2_text_rect)

            # Check for mouse click on menu options
            mouse_pos = pygame.mouse.get_pos()
            mouse_click = pygame.mouse.get_pressed()

            if option1_text_rect.collidepoint(mouse_pos):
                if mouse_click[0] == 1:
                    # Start game logic goes here
                    menu = False

            if option2_text_rect.collidepoint(mouse_pos):
                if mouse_click[0] == 1:
                    pygame.quit()
                    

            # Update the screen
            pygame.display.flip()
