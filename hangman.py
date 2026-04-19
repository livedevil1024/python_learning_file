import random

word_list = ["python", "hangman", "programming", "challenge", "developer"] 
chosen_word = random.choice(word_list)
print(chosen_word)
lives = 6
correct_guess=[]
gameover = False


while not gameover:


    print("Wlecome to Hangman")
    placeholder =""
    for position in chosen_word:
        for letters in correct_guess:
            if (position == letters):
                placeholder += letters
                break
        else:
            placeholder += "_"
    
    if (lives==0):
        gameover = True
        print("Game Over! You lost.")
        break
    elif (placeholder == chosen_word):
        gameover = True
        print("Congratulations! You won.")
        break

    print(placeholder)

    

    player_guess= input("Enter your guess: ").lower()

    if player_guess in chosen_word:
        correct_guess.append(player_guess)
        print("Your guess is Right")
        print(f"you have left {lives} lives")
    elif player_guess in correct_guess:
        print("You have already guessed that letter. Try again.")
        print(f"you have left {lives} lives")
    else:
        print("Your guess is Wrong")
        lives -= 1
        print(f"you have left {lives} lives")
    