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

IMAGE = pygame.image.load('AceHearts.png').convert_alpha()

'''
class Player(pygame.sprite.Sprite):
    def __init__(self, pos, image):
        super().__init__()
        self.image = image
        self.rect = self.image.get_rect(center=pos)

player1 = Player((100, 300), IMAGE)
'''


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


    #pygame.draw.rect(screen, (0,0,200), (100, 100, 100, 100))

    screen.blit(IMAGE, (25,25))



    pygame.display.flip()