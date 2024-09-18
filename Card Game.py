import pygame
import sys

# Initialize Pygame
pygame.init()

# Set up screen dimensions
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Card Game")

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)

Ace_Hearts = pygame.transform.scale(pygame.image.load('AceHearts.png').convert_alpha(), (50, 50))
Ace_Clubs = pygame.transform.scale(pygame.image.load('AceClubs.png').convert_alpha(), (50, 50))



# Create a clock object to standardize framerate
gameClock = pygame.time.Clock()


# Main game loop
while True:
    screen.fill(WHITE)

    # Handle window close
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    
    # Set max game framerate
    gameClock.tick(60)

    
    screen.blit(Ace_Hearts, (250,500))
    screen.blit(Ace_Clubs, (300,500))



    pygame.display.flip()