import pygame
import sys

# Initialize Pygame
pygame.init()

# Set up screen dimensions
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Card Game")


class Card:
  def __init__(self, suit, value, imageFileName):
    self.suit = suit
    self.value = value
    self.image = pygame.transform.scale(pygame.image.load(imageFileName).convert_alpha(), (50, 50))




Ace_Hearts = Card('H', 13, 'AceHearts.png')
Ace_Clubs = Card('H', 13, 'AceClubs.png')



# Create a clock object to standardize framerate
gameClock = pygame.time.Clock()


# Main game loop
while True:
    screen.fill((255,255,255))

    # Handle window close
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    
    # Set max game framerate
    gameClock.tick(60)

    
    screen.blit(Ace_Clubs.image, (300,500))
    screen.blit(Ace_Hearts.image, (700,500))



    pygame.display.flip()