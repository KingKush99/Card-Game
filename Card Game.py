import pygame
import sys
import random
import math


# Initialize Pygame
pygame.init()
pygame.font.init()
game_font = pygame.font.SysFont('Constantia', 20)

# Set up screen dimensions
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
CARDS_PER_PLAYER = 7
CARD_SEPARATION = 20
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Card Game")


##########
## CLASSES
##########
class Card:
  def __init__(self, suit, value, imageFileName):
    self.suit = suit
    self.value = value
    self.xpos = 0
    self.ypos = 0
    self.height = 100
    self.width = 75
    self.cardFace = pygame.transform.scale(pygame.image.load(imageFileName).convert_alpha(), (self.width, self.height))
    self.cardBack = pygame.transform.scale(pygame.image.load('BackOfCard.png').convert_alpha(), (self.width*1.1, self.height*1.1))
    self.selected = False


class cardPile:
  def __init__(self, xpos, ypos, cardSep, cardArray):
    self.cardArray = cardArray
    self.xpos = xpos
    self.ypos = ypos
    self.cardSep = cardSep

  def set_Coordinates(self):
    for i in range(len(self.cardArray)):
      self.cardArray[i].xpos = self.xpos + self.cardSep * i
      self.cardArray[i].ypos = self.ypos

  def deal_Cards(self, numCards, playerArray):
    for i in range(numCards):
      for j in range(len(playerArray)):
        if len(Deck.cardArray) > 0:
          playerArray[j].handArray.append(Deck.cardArray[len(Deck.cardArray) - 1]) # Deal top card
          Deck.cardArray.pop(len(Deck.cardArray) - 1)
        else:
          break

  def Shuffle(self):
    for i in range(len(self.cardArray)):
      j = random.randint(0,len(self.cardArray) - 1)
      self.cardArray[i], self.cardArray[j] = self.cardArray[j], self.cardArray[i]


class Player:
  def __init__(self, name, seat, cardArray):
    self.name = game_font.render(name, False, (0,0,0))
    self.seat = seat
    self.handArray = cardArray
    self.runArray = []
    self.points = 0
    self.numberOfSelectedCards = 0
    self.turn = False
    self.text_xpos = 0
    self.text_ypos = 0
    self.message = game_font.render("", False, (0,0,0))

  def set_turn_true(self):
    self.turn = True
  
  def set_turn_false(self):
    self.turn = False

  def set_Coordinates(self, playerTurn, numPlayers):
    relativeSeat = (self.seat - playerTurn) % numPlayers
    self.text_xpos = ((relativeSeat + 0) % 2) * pow(-1, (relativeSeat + 1) % 3) * 250 + SCREEN_WIDTH/2 -90
    self.text_ypos = ((relativeSeat + 1) % 2) * pow(-1, (relativeSeat + 2) % 3) * 200 + SCREEN_HEIGHT/2 -75
    for i in range(len(self.handArray)):
      self.handArray[i].xpos = ((relativeSeat + 0) % 2) * pow(-1, (relativeSeat + 1) % 3) * 250 + SCREEN_WIDTH/2 -100 + CARD_SEPARATION * i
      self.handArray[i].ypos = ((relativeSeat + 1) % 2) * pow(-1, (relativeSeat + 2) % 3) * 200 + SCREEN_HEIGHT/2 -50
      
  def select_Card(self, cardIndex, allowedNumberOfSelectedCards):
    if self.numberOfSelectedCards < allowedNumberOfSelectedCards:
        self.handArray[cardIndex].selected = True
        self.handArray[cardIndex].ypos = self.handArray[cardIndex].ypos - 10
        self.numberOfSelectedCards = self.numberOfSelectedCards + 1
        self.message = game_font.render("", False, (0,0,0))
    else:
        text = "*Can only select " + str(allowedNumberOfSelectedCards) + " cards"
        self.message = game_font.render(text, False, (0,0,0))

  def play_Card(self, cardToPlay, pileToPlayTo): # To develop
    pileToPlayTo.cardArray.append(self.handArray[cardToPlay])
    self.handArray.pop(cardToPlay)

  def play_Selected_Cards(self, allowedNumberOfSelectedCards, pileToPlayTo):
      i = 0
      if self.numberOfSelectedCards < allowedNumberOfSelectedCards:
        text = "*Must select " + str(allowedNumberOfSelectedCards) + " cards"
        self.message = game_font.render(text, False, (0,0,0))
        return False
      else:
          while i < len(self.handArray):
            if self.handArray[i].selected == True:
                self.deselect_Card(i)
                self.play_Card(i, pileToPlayTo)            
            else:
                i = i + 1
          return True

  def deselect_Card(self, cardIndex):
    if self.handArray[cardIndex].selected == True:
      self.handArray[cardIndex].selected = False
      self.handArray[cardIndex].ypos = self.handArray[cardIndex].ypos + 10
      self.numberOfSelectedCards = self.numberOfSelectedCards - 1
      self.message = game_font.render("", False, (0,0,0))

  def sort_Cards(self):
    sortGap = math.floor(len(self.handArray)/2)
    unSorted = True
    swaps = False
    if len(self.handArray) > 0:
        while unSorted == True:
            for i in range(len(self.handArray)):
                if (i == len(self.handArray) - 1) and (sortGap == 1) and (swaps == False): # If it's gone through one by one and made no swaps, then it's fully sorted
                    unSorted = False  
                if i + sortGap < len(self.handArray):   
                    if self.handArray[i].value < self.handArray[i + sortGap].value:     # If left card greater than right card, then swap them
                        self.handArray[i], self.handArray[i + sortGap] = self.handArray[i + sortGap], self.handArray[i]
                        swaps = True
                else :  # Once we're out of range of the player's hand, lower the comparison gap by one (minimum gap of 1)
                    sortGap = max(sortGap - 1, 1)
                    swaps = False
                    break
        

class Button:
    def __init__(self, text, xpos, ypos, width, height):
        self.text = game_font.render(text, False, (0,0,0))
        self.xpos = xpos
        self.ypos = ypos
        self.width = width
        self.height = height
        self.text_xpos = self.xpos + 5 #self.width/3
        self.text_ypos = self.ypos + self.height/3
        self.colour = (233,196,73)
        #self.unclickedImage = pygame.transform.scale(pygame.image.load(imageFileName).convert_alpha(), (self.width, self.height))
        #self.clickedImage = pygame.transform.scale(pygame.image.load(imageFileName).convert_alpha(), (self.width, self.height))

    def click_Button(self):
        self.colour = (227,181,28)

    def unclick_Button(self):
        self.colour = (233,196,73)

    def do_something(self, funcToCall):
        funcToCall



#######################
## OBJECT INSTANTIATION
#######################

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


Deck = cardPile(0, 0, 0.5, [Ace_Hearts,King_Hearts,Queen_Hearts,Jack_Hearts,Ten_Hearts,Nine_Hearts,Eight_Hearts,Seven_Hearts,Six_Hearts,Five_Hearts,Four_Hearts,Three_Hearts,Two_Hearts,Ace_Clubs,King_Clubs,Queen_Clubs,Jack_Clubs,Ten_Clubs,Nine_Clubs,Eight_Clubs,Seven_Clubs,Six_Clubs,Five_Clubs,Four_Clubs,Three_Clubs,Two_Clubs,Ace_Diamonds,King_Diamonds,Queen_Diamonds,Jack_Diamonds,Ten_Diamonds,Nine_Diamonds,Eight_Diamonds,Seven_Diamonds,Six_Diamonds,Five_Diamonds,Four_Diamonds,Three_Diamonds,Two_Diamonds,Ace_Spades,King_Spades,Queen_Spades,Jack_Spades,Ten_Spades,Nine_Spades,Eight_Spades,Seven_Spades,Six_Spades,Five_Spades,Four_Spades,Three_Spades,Two_Spades])
Pot = cardPile(SCREEN_WIDTH/2 - 100, SCREEN_HEIGHT/2 - 50, CARD_SEPARATION, [])
#LeftPot = cardPile(SCREEN_WIDTH/2 - 150, SCREEN_HEIGHT/2 - 50, CARD_SEPARATION, [])
#RightPot = cardPile(SCREEN_WIDTH/2 - 50, SCREEN_HEIGHT/2 - 50, CARD_SEPARATION, [])
playCardsButton = Button("Play Cards", 3*SCREEN_WIDTH/4, 3*SCREEN_HEIGHT/4, 100, 50)

Player1 = Player("Connor", 0, [])
Player2 = Player("Christian", 1, [])
Player3 = Player("Mom", 2, [])
Player4 = Player("Dad", 3, [])

playerArray = [Player1, Player2, Player3, Player4]




# Create a clock object to standardize framerate
gameClock = pygame.time.Clock()

#################
## Main game loop
#################
Deck.Shuffle()
Deck.set_Coordinates()
playerTurn = 0
playerArray[0].set_turn_true() # It's the first player's turn
while True:
    screen.fill((79, 156, 78))

    # Handle mouse clicks
    for event in pygame.event.get():
        # If you click close window
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.MOUSEBUTTONDOWN:
          # If you click the Deck then deal the cards
          if len(Deck.cardArray) > 0:
            if (event.pos[0] >= Deck.cardArray[len(Deck.cardArray) - 1].xpos) & (event.pos[0] <= Deck.cardArray[len(Deck.cardArray) - 1].xpos + Deck.cardArray[len(Deck.cardArray) - 1].width):
              if (event.pos[1] >= Deck.cardArray[len(Deck.cardArray) - 1].ypos) & (event.pos[1] <= Deck.cardArray[len(Deck.cardArray) - 1].ypos + Deck.cardArray[len(Deck.cardArray) - 1].height):
                Deck.deal_Cards(CARDS_PER_PLAYER, playerArray)
                Deck.set_Coordinates()
                Pot.set_Coordinates()
                for i in range(len(playerArray)):
                  playerArray[i].sort_Cards()
                  playerArray[i].set_Coordinates(playerTurn, len(playerArray))
                break
          # If you click a card in hand then play the card
          for j in range(len(playerArray[playerTurn].handArray)):
            selectionWidth = (j == len(playerArray[playerTurn].handArray) -1)*(playerArray[playerTurn].handArray[j].width) + (j != len(playerArray[playerTurn].handArray) -1)*(CARD_SEPARATION) # if it's the last card in the hand then the selection area is larger
            if (event.pos[0] >= playerArray[playerTurn].handArray[j].xpos) & (event.pos[0] <= playerArray[playerTurn].handArray[j].xpos + selectionWidth):
              if (event.pos[1] >= playerArray[playerTurn].handArray[j].ypos) & (event.pos[1] <= playerArray[playerTurn].handArray[j].ypos + playerArray[playerTurn].handArray[j].height):
                if playerArray[playerTurn].handArray[j].selected == True:
                  playerArray[playerTurn].deselect_Card(j)  # Deselect card if it was already selected
                  break
                else:
                  playerArray[playerTurn].select_Card(j, 1 + 1*(len(Pot.cardArray) > 0)) # Select the card that was clicked
                  break
          # if you click the button
          if (event.pos[0] >= playCardsButton.xpos) & (event.pos[0] <= playCardsButton.xpos + playCardsButton.width):
              if (event.pos[1] >= playCardsButton.ypos) & (event.pos[1] <= playCardsButton.ypos + playCardsButton.height):
                  playCardsButton.click_Button() # Changes button colour
                  #playCardsButton.do_something(playerArray[playerTurn].play_Selected_Cards(1 + 1*(len(Pot.cardArray) > 0), Pot))
                  if playerArray[playerTurn].play_Selected_Cards(1 + 1*(len(Pot.cardArray) > 0), Pot):
                      playerArray[playerTurn].sort_Cards()
                      playerArray[playerTurn].set_turn_false()
                      playerTurn = (playerTurn + 1) % len(playerArray)
                      playerArray[playerTurn].set_turn_true()
                      for i in range(len(playerArray)):
                        playerArray[i].set_Coordinates(playerTurn, len(playerArray))
                      Pot.set_Coordinates()

    
    

    # Draw Button
    pygame.draw.rect(screen, playCardsButton.colour, pygame.Rect(playCardsButton.xpos, playCardsButton.ypos, playCardsButton.width, playCardsButton.height))
    screen.blit(playCardsButton.text, (playCardsButton.text_xpos, playCardsButton.text_ypos))
    playCardsButton.unclick_Button() # reset button colour (after it's been displayed)

    # Draw Deck
    for i in range(len(Deck.cardArray)):
      screen.blit(Deck.cardArray[i].cardBack, (Deck.cardArray[i].xpos, Deck.cardArray[i].ypos))
    
    # Draw Pot
    for i in range(len(Pot.cardArray)):
      screen.blit(Pot.cardArray[i].cardFace, (Pot.cardArray[i].xpos, Pot.cardArray[i].ypos))

    # Draw Player Hands
    for i in range(len(playerArray)):
      for j in range(len(playerArray[i].handArray)):
          if playerArray[i].turn == True:
            screen.blit(playerArray[i].handArray[j].cardFace, (playerArray[i].handArray[j].xpos, playerArray[i].handArray[j].ypos))
            screen.blit(playerArray[i].name, (playerArray[i].text_xpos, playerArray[i].text_ypos))
            screen.blit(playerArray[i].message, (playerArray[i].text_xpos, playerArray[i].text_ypos - 50))
          else:
            screen.blit(playerArray[i].handArray[j].cardBack, (playerArray[i].handArray[j].xpos, playerArray[i].handArray[j].ypos))
            screen.blit(playerArray[i].name, (playerArray[i].text_xpos, playerArray[i].text_ypos))


    # Set max game framerate
    gameClock.tick(15)

    pygame.display.flip()