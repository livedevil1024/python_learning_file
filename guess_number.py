import random

random_number = random.randint(1, 100)
lives = 0
game_over = False 

def game():
    global lives
    global random_number, game_over
    while not game_over:
        if (lives==0):
            game_over = True
            print(f"Game Over! you lose the correct number was {random_number}")
            break

        print(f"you have {lives} lives remaining")
        user_input = int(input("Guess the number between 1 to 100: "))

        if (user_input == random_number):
            print(f"You Won! you get the correct guess {random_number}")
            game_over= True
        elif(user_input>random_number):
            print("you guess wrong number its TOO HIGH")
            lives -= 1
        elif(user_input<random_number):
            print("your guess is wrong, its TOO LOW")
            lives -= 1
        

print("Welcome to the Guessing Game")
print("Which game mode you want to play 'easy' or 'hard'")
choice = str(input("Enter your choice: ")).lower()

if (choice=="easy"):
    lives = 10
    game()
elif (choice=="hard"):    
    lives = 5
    game()
else:
    print("Invalid choice. Please choose 'easy' or 'hard'.")

