import random

player_input = int(input("Please enter 0 for paper, 1 for rock, 2 for scissors "))
computer_input = random.randint(0, 2)
game_options = ["paper", "rock", "scissors"]
game_graphics = [
    '''
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)  
    '''
    ,
    '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
    ''',
    '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
    '''
]


def show_players_options():
    print("You have Chosen:")
    print(game_graphics[player_input])
    print("Computer has Chosen:")
    print(game_graphics[computer_input])
    
def show_you_won():
    print(
        f"You Won, You have chosen {game_options[player_input]} and Computer has chosen {game_options[computer_input]}")
def show_you_lost():
    print(
        f"You Lost, You have chosen {game_options[player_input]} and Computer has chosen {game_options[computer_input]}")


if player_input == computer_input:
    print("draw")
    show_players_options()
elif player_input == 0 and computer_input == 1:
    show_you_won()
    show_players_options()
elif player_input == 1 and computer_input == 2:
    show_you_won()
    show_players_options()
elif player_input == 2 and computer_input == 0:
    show_you_won()
    show_players_options()
else:
    show_you_lost()
    show_players_options()
