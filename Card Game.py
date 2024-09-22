import pygame
import sys
import random

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
    self.xpos = 0
    self.ypos = 0
    self.height = 100
    self.width = 75
    self.cardFace = pygame.transform.scale(pygame.image.load(imageFileName).convert_alpha(), (self.width, self.height))
    self.cardBack = pygame.transform.scale(pygame.image.load('BackOfCard.png').convert_alpha(), (self.width, self.height))
    self.selected = False


CARDS_PER_PLAYER = 7

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

Deck = [Ace_Hearts,King_Hearts,Queen_Hearts,Jack_Hearts,Ten_Hearts,Nine_Hearts,Eight_Hearts,Seven_Hearts,Six_Hearts,Five_Hearts,Four_Hearts,Three_Hearts,Two_Hearts,Ace_Clubs,King_Clubs,Queen_Clubs,Jack_Clubs,Ten_Clubs,Nine_Clubs,Eight_Clubs,Seven_Clubs,Six_Clubs,Five_Clubs,Four_Clubs,Three_Clubs,Two_Clubs,Ace_Diamonds,King_Diamonds,Queen_Diamonds,Jack_Diamonds,Ten_Diamonds,Nine_Diamonds,Eight_Diamonds,Seven_Diamonds,Six_Diamonds,Five_Diamonds,Four_Diamonds,Three_Diamonds,Two_Diamonds,Ace_Spades,King_Spades,Queen_Spades,Jack_Spades,Ten_Spades,Nine_Spades,Eight_Spades,Seven_Spades,Six_Spades,Five_Spades,Four_Spades,Three_Spades,Two_Spades]
Pot = []

class Player:
  def __init__(self, name, seat, cardArray):
    self.name = name
    self.seat = seat
    self.handArray = cardArray
    self.runArray = []
    self.points = 0

Player1 = Player("Connor", 1, [])
Player2 = Player("Christian", 2, [])
Player3 = Player("Mom", 3, [])
Player4 = Player("Dad", 4, [])

playerArray = [Player1, Player2, Player3, Player4]

def DealCards(numCards):
  for i in range(numCards):
    for j in range(len(playerArray)):
      if len(Deck) > 0:
        ind = random.randint(0, len(Deck) - 1)
        playerArray[j].handArray.append(Deck[ind])
        Deck.pop(ind)

def Shuffle():
  test = 1




# Create a clock object to standardize framerate
gameClock = pygame.time.Clock()


# Main game loop
while True:
    screen.fill((79, 156, 78))

    # Handle window close
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.MOUSEBUTTONDOWN:
          print(event.pos[0] , event.pos[1])  # print for testing purposes
          if len(Deck) > 0:
            if (event.pos[0] >= Deck[len(Deck) - 1].xpos) & (event.pos[0] <= Deck[len(Deck) - 1].xpos + Deck[len(Deck) - 1].width):
              if (event.pos[1] >= Deck[len(Deck) - 1].ypos) & (event.pos[1] <= Deck[len(Deck) - 1].ypos + Deck[len(Deck) - 1].height):
                DealCards(CARDS_PER_PLAYER)
                break
          for i in range(len(playerArray)):
            for j in range(len(playerArray[i].handArray)):
              if (event.pos[0] >= playerArray[i].handArray[j].xpos) & (event.pos[0] <= playerArray[i].handArray[j].xpos + 10):
                if (event.pos[1] >= playerArray[i].handArray[j].ypos) & (event.pos[1] <= playerArray[i].handArray[j].ypos + playerArray[i].handArray[j].height):
                  Pot.append(playerArray[i].handArray[j])
                  playerArray[i].handArray.pop(j)
                  Pot[len(Pot) - 1].xpos = 500
                  Pot[len(Pot) - 1].xpos = 500
                  break
                  
                  



    # Set max game framerate
    gameClock.tick(60)

    for i in range(len(Deck)):
      screen.blit(Deck[i].cardBack, (Deck[i].xpos, Deck[i].ypos))

    for i in range(len(Pot)):
      screen.blit(Pot[i].cardFace, (Pot[i].xpos, Pot[i].ypos))

    for i in range(len(playerArray)):
      for j in range(len(playerArray[i].handArray)):
        playerArray[i].handArray[j].xpos = 300 + j*10
        playerArray[i].handArray[j].ypos = 25 + 150*i
        screen.blit(playerArray[i].handArray[j].cardFace, (playerArray[i].handArray[j].xpos, playerArray[i].handArray[j].ypos))



    pygame.display.flip()