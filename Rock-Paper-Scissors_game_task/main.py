import random
from secrets import choice

print("******************** Welcome to my Rock-Paper-Scissors game ********************")
print("\n")

print("How the game works: ")
print("Rock beats Paper \nPaper beats Rock \nScissors beats Paper")
print('If the two players choose the same "character” it\'s a tie, and the game repeats')
print("\n")

print("YOU = Player \nCOMPUTER = CPU")
print("\n")
cpu_options = ["R", "P", "S"]

while True:
    player_choice = input('Pick an option between "R", "P" or "S": ')
    if player_choice != "R" and player_choice != "P" and player_choice != "S":
        print('Invalid choice. Please input either "R", "P", or "S"\n')
        
    else:
        if player_choice == "R" and random.choice(cpu_options) == "S":
            print("You win!")
            print("Player (Rock) : CPU (Scissors)")
            break

        elif player_choice == "R" and random.choice(cpu_options) == "P":
            print("You lose.")
            print("Player (Rock) : CPU (Paper)")
            break

        elif player_choice == "P" and random.choice(cpu_options) == "R":
            print("You win!")
            print("Player (Paper) : CPU (Rock)")
            break

        elif player_choice == "P" and random.choice(cpu_options) == "S":
            print("You lose.")
            print("Player (Paper) : CPU (Scissors)")
            break

        elif player_choice == "S" and random.choice(cpu_options) == "R":
            print("You lose.")
            print("Player (Scissors) : CPU (Rock)")
            break

        elif player_choice == "S" and random.choice(cpu_options) == "P":
            print("You win!")
            print("Player (Scissors) : CPU (Paper)")
            break

        elif player_choice == random.choice(cpu_options):
            print("It's a tie!")
            print("Make another pick")

        print
