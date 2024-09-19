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
    self.imageFront = pygame.transform.scale(pygame.image.load(imageFileName).convert_alpha(), (75, 100))
    self.imageBack = pygame.transform.scale(pygame.image.load('BackOfCard.png').convert_alpha(), (75, 100))




Ace_Hearts = Card('H', 13, 'AceHearts.png')
Ace_Clubs = Card('C', 13, 'AceClubs.png')



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

    
    screen.blit(Ace_Clubs.imageFront, (400,400))
    screen.blit(Ace_Hearts.imageBack, (600,400))



    pygame.display.flip()