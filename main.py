############### Blackjack Project #####################
import random
from replit import clear
from art import logo
#Difficulty Normal 😎: Use all Hints below to complete the project.
#Difficulty Hard 🤔: Use only Hints 1, 2, 3 to complete the project.
#Difficulty Extra Hard 😭: Only use Hints 1 & 2 to complete the project.
#Difficulty Expert 🤯: Only use Hint 1 to complete the project.

############### Our Blackjack House Rules #####################

## The deck is unlimited in size. 
## There are no jokers. 
## The Jack/Queen/King all count as 10.
## The the Ace can count as 11 or 1.
## Use the following list as the deck of cards:
cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
## The cards in the list have equal probability of being drawn.
## Cards are not removed from the deck as they are drawn.
## The computer is the dealer.

##################### Hints #####################

#Hint 1: Go to this website and try out the Blackjack game: 
#   https://games.washingtonpost.com/games/blackjack/
#Then try out the completed Blackjack project here: 
#   http://blackjack-final.appbrewery.repl.run

#Hint 2: Read this breakdown of program requirements: 
#   http://listmoz.com/view/6h34DJpvJBFVRlZfJvxF
#Then try to create your own flowchart for the program.

#Hint 3: Download and read this flow chart I've created: 
#   https://drive.google.com/uc?export=download&id=1rDkiHCrhaf9eX7u7yjM1qwSuyEk-rPnt

#Hint 4: Create a deal_card() function that uses the List below to *return* a random card.
#11 is the Ace.
#cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
def deal_card():
  cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
  card = random.choice(cards)
  return card
#Hint 5: Deal the user and computer 2 cards each using deal_card() and append().

def calculate_score(card_list):
  """Takes a list of cards and returns the score calculated from the cards"""
  if sum(card_list) == 21 and len(card_list) == 2:
    return 0
  if 11 in card_list and sum(card_list) > 21:
    card_list.remove(11)
    card_list.append(1)
  return sum(card_list)

def compare(user_score, computer_score):
  if user_score == computer_score:
    return "It's a draw!"
  elif computer_score == 0:
    return "You lose!"
  elif user_score == 0:
    return "You win!"
  elif user_score > 21:
    return "You lose!"
  elif computer_score > 21:
    return "You win!"
  elif user_score > computer_score:
      return "You win!"
  else:
      return "You lose!"

def play_game():
  print(logo)

  user_cards = []
  computer_cards = []
  is_game_over = False
  
  for i in range(2):
    user_cards.append(deal_card())
    computer_cards.append(deal_card())
  
  while not is_game_over:
    user_score = calculate_score(user_cards)
    computer_score = calculate_score(computer_cards)
    print(f"Your cards: {user_cards}, current score: {user_score}")
    print(f"Computer's first card is: {computer_cards[0]}")
    
    
    if user_score == 0 or computer_score == 0 or user_score > 21:
      is_game_over = True
    else:
      play_on = input("Type 'y' to draw another card or 'n' to end the game: ")
      if play_on == 'y':
        user_cards.append(deal_card())
      elif play_on == 'n':
        is_game_over = True
  
  while computer_score != 0 and computer_score < 17:
    computer_cards.append(deal_card())
    computer_score = calculate_score(computer_cards)
  
  
  print(f"  Your cards: {user_cards} and final score: {user_score}")
  print(f"  Computer's cards: {computer_cards} and final score: {computer_score}")
  print(compare(user_score, computer_score))

while input("Type 'y' if you want to start a new game and 'n' if you wish to exit: ") == 'y':
  clear()
  play_game()