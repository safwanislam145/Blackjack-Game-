""" Blackjack Game """

############### Our Blackjack House Rules #####################

## The deck is unlimited in size. 
## There are no jokers. 
## The Jack/Queen/King all count as 10.
## The the Ace can count as 11 or 1.
## Use the following list as the deck of cards:
## cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
## The cards in the list have equal probability of being drawn.
## Cards are not removed from the deck as they are drawn.
## The computer is the dealer.

import random

# a function to deal cards
def deal_card():
    """Returns a random card from the deck."""
    cards = [11,2,3,4,5,6,7,8,9,10,10,10,10] 
    random_card = random.choice(cards)
    return random_card

# a function to calculate the score that takes a list of cards as input and returns the score.
def calculate_score(cards):
    """Take a list of cards and return the score calculated from the cards"""
    if sum(cards) == 21 and len(cards) == 2:
        return 0
    if sum(cards) > 21 and 11 in cards: # if the sum of the cards is greater than 21 and there is an ace in the cards
        cards.remove(11)
        cards.append(1)
    return sum(cards)

def compare(user_score, computer_score):
  #If you and the computer are both over, you lose.
  if user_score > 21 and computer_score > 21:
    return "You went over. You lose 😤"

  if user_score == computer_score:
    return "Draw 🙃"
  elif computer_score == 0:
    return "Lose, opponent has Blackjack 😱"
  elif user_score == 0:
    return "Win with a Blackjack 😎"
  elif user_score > 21:
    return "You went over. You lose 😭"
  elif computer_score > 21:
    return "Opponent went over. You win 😁"
  elif user_score > computer_score:
    return "You win 😃"
  else:
    return "You lose 😤"

def play_game():
    # Deal the user and computer 2 cards each using deal_card() and append().
    user_cards = []
    computer_cards = []
    is_game_over = False

    for i in range(2):
        user_cards.append(deal_card()) # use extend when adding a list to a list and append when adding a single item
        computer_cards.append(deal_card()) # use extend when adding a list to a list and append when adding a single item

    while not is_game_over:
        # If the computer or the user has a blackjack (0) or if the user's score is over 21, then the game ends.
        user_score = calculate_score(user_cards)
        computer_score = calculate_score(computer_cards) 
        print(f"Your cards: {user_cards}, current score: {user_score}")
        print(f"Computer's cards: {computer_cards}, current score: {computer_score}")
         
        if user_score == 0 or computer_score == 0 or user_score > 21:
            is_game_over = True
        else: 
          # If the game has not ended, ask the user if they want to draw another card. 
          # If yes, then use the deal_card() function to add another card to the user_cards List.
          # If no, then the game has ended.
            user_should_deal = input("Type 'y' to get another card, type 'n' to pass: ")
            if user_should_deal == "y":
                user_cards.append(deal_card())
            else:
                is_game_over = True

    # Once the user is done, it's time to let the computer play. 
    # The computer should keep drawing cards as long as it has a score less than 17.
    while computer_score != 0 and computer_score < 17:
        computer_cards.append(deal_card())
        computer_score = calculate_score(computer_cards)
    
    print(f"   Your final hand: {user_cards}, final score: {user_score}")
    print(f"   Computer's final hand: {computer_cards}, final score: {computer_score}")
    print(compare(user_score, computer_score))

def main():
    should_continue = True
    while should_continue:
        user_choice = input("Do you want to play a game of Blackjack? Type 'y' or 'n': ")
        if user_choice == "y":
            play_game()
        else:
            should_continue = False
            print("Goodbye!")

if __name__ == "__main__":
    main()
    


