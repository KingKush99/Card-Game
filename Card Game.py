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




Ace_Hearts = Card('H', 14, 'AceHearts.png')
King_Hearts = Card('H', 13, 'KingHearts.png')
Queen_Hearts = Card('H', 12, 'QueenHearts.png')
Jack_Hearts = Card('H', 11, 'JackHearts.png')
Ten_Hearts = Card('H', 10, 'TenHearts.png')
Nine_Hearts = Card('H', 9, 'NineHearts.png')
Eight_Hearts = Card('H', 8, 'EightHearts.png')
Seven_Hearts = Card('H', 7, 'SevenHearts.png')
Six_Hearts = Card('H', 6, 'SixHearts.png')
Five_Hearts = Card('H', 5, 'FiveHearts.png')
Four_Hearts = Card('H', 4, 'FourHearts.png')
Three_Hearts = Card('H', 3, 'ThreeHearts.png')
Two_Hearts = Card('H', 2, 'TwoHearts.png')

Ace_Clubs = Card('C', 14, 'AceClubs.png')
King_Clubs = Card('C', 13, 'KingClubs.png')
Queen_Clubs = Card('C', 12, 'QueenClubs.png')
Jack_Clubs = Card('C', 11, 'JackClubs.png')
Ten_Clubs = Card('C', 10, 'TenClubs.png')
Nine_Clubs = Card('C', 9, 'NineClubs.png')
Eight_Clubs = Card('C', 8, 'EightClubs.png')
Seven_Clubs = Card('C', 7, 'SevenClubs.png')
Six_Clubs = Card('C', 6, 'SixClubs.png')
Five_Clubs = Card('C', 5, 'FiveClubs.png')
Four_Clubs = Card('C', 4, 'FourClubs.png')
Three_Clubs = Card('C', 3, 'ThreeClubs.png')
Two_Clubs = Card('C', 2, 'TwoClubs.png')

Ace_Diamonds = Card('D', 14, 'AceDiamonds.png')
King_Diamonds = Card('D', 13, 'KingDiamonds.png')
Queen_Diamonds = Card('D', 12, 'QueenDiamonds.png')
Jack_Diamonds = Card('D', 11, 'JackDiamonds.png')
Ten_Diamonds = Card('D', 10, 'TenDiamonds.png')
Nine_Diamonds = Card('D', 9, 'NineDiamonds.png')
Eight_Diamonds = Card('D', 8, 'EightDiamonds.png')
Seven_Diamonds = Card('D', 7, 'SevenDiamonds.png')
Six_Diamonds = Card('D', 6, 'SixDiamonds.png')
Five_Diamonds = Card('D', 5, 'FiveDiamonds.png')
Four_Diamonds = Card('D', 4, 'FourDiamonds.png')
Three_Diamonds = Card('D', 3, 'ThreeDiamonds.png')
Two_Diamonds = Card('D', 2, 'TwoDiamonds.png')

Ace_Spades = Card('S', 14, 'AceSpades.png')
King_Spades = Card('S', 13, 'KingSpades.png')
Queen_Spades = Card('S', 12, 'QueenSpades.png')
Jack_Spades = Card('S', 11, 'JackSpades.png')
Ten_Spades = Card('S', 10, 'TenSpades.png')
Nine_Spades = Card('S', 9, 'NineSpades.png')
Eight_Spades = Card('S', 8, 'EightSpades.png')
Seven_Spades = Card('S', 7, 'SevenSpades.png')
Six_Spades = Card('S', 6, 'SixSpades.png')
Five_Spades = Card('S', 5, 'FiveSpades.png')
Four_Spades = Card('S', 4, 'FourSpades.png')
Three_Spades = Card('S', 3, 'ThreeSpades.png')
Two_Spades = Card('S', 2, 'TwoSpades.png')


class Player:
  def __init__(self, name, seat, cardArray):
    self.name = name
    self.seat = seat
    self.handArray = cardArray
    self.runArray = []
    self.points = 0

Player1 = Player("Connor", 1, [Ace_Diamonds, King_Spades, Two_Clubs])



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

    for card in Player1.handArray:
       screen.blit(card.imageFront, (400,400))



    pygame.display.flip()