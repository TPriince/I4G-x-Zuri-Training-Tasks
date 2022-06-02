import random
from secrets import choice

print("******************** Welcome to my Rock-Paper-Scissors game ********************")
print("\n")

print("How the game works: ")
print("Rock beats Scissors\nPaper beats Rock\nScissors beats Paper")
print('If the two players choose the same "character” it\'s a tie, and the game repeats')
print("\n")

print('"R" for "Rock"')
print('"P" for "Paper"')
print('"S" for "Scissors"')

print("YOU = Player\nCOMPUTER = CPU")
print("\n")


while True:
    
    player_choice = input('Pick an option - "R", "P" or "S": ')
    cpu_options = ["R", "P", "S"]
    cpu_choice = random.choice(cpu_options)

    if player_choice != "R" and player_choice != "P" and player_choice != "S":
        print('Invalid choice. Please input either "R", "P", or "S"\n')
        
    else:
        if player_choice == "R" and cpu_choice == "S":
            print("Player (Rock) : CPU (Scissors)")
            print("You win!")
            break

        elif player_choice == "R" and cpu_choice == "P":
            print("Player (Rock) : CPU (Paper)")
            print("You lose.")
            break

        elif player_choice == "P" and cpu_choice == "R":
            print("Player (Paper) : CPU (Rock)")
            print("You win!")
            break

        elif player_choice == "P" and cpu_choice == "S":
            print("Player (Paper) : CPU (Scissors)")
            print("You lose.")
            break

        elif player_choice == "S" and cpu_choice == "R":
            print("Player (Scissors) : CPU (Rock)")
            print("You lose.")
            break

        elif player_choice == "S" and cpu_choice == "P":
            print("Player (Scissors) : CPU (Paper)")
            print("You win!")
            break

        # If player choice is the same as CPU choice
        elif player_choice == cpu_choice:
            if player_choice == "R":
                # Since Player and CPU choices are the same, if player_choice = "Rock", CPU will have the same choice
                print("Player (Rock) : CPU (Rock)")
                print("It's a tie!")
                print("Make another pick")

            if player_choice == "P":
                # Since Player and CPU choices are the same, if player_choice = "Paper", CPU will have the same choice
                print("Player (Paper) : CPU (Paper)")
                print("It's a tie!")
                print("Make another pick")

            if player_choice == "S":
                # Since Player and CPU choices are the same, if player_choice = "Scissors", CPU will have the same choice
                print("Player (Scissors) : CPU (Scissors)")
                print("It's a tie!")
                print("Make another pick")

