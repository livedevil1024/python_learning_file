import random
data = [
    {
        'name': 'Instagram',
        'follower_count': 626000000,
        'description': 'Social Media Platform'
    },
    {
        'name': 'Cristiano Ronaldo',
        'follower_count': 614000000,
        'description': 'Footballer'
    },
    {
        'name': 'Lionel Messi',
        'follower_count': 505000000,
        'description': 'Footballer'
    },
    {
        'name': 'Selena Gomez',
        'follower_count': 428000000,
        'description': 'Singer'
    },
    {
        'name': 'Kylie Jenner',
        'follower_count': 398000000,
        'description': 'Reality TV Star'
    },
    {
        'name': 'Dwayne Johnson',
        'follower_count': 389000000,
        'description': 'Actor'
    },
    {
        'name': 'Taylor Swift',
        'follower_count': 283000000,
        'description': 'Singer'
    },
    {
        'name': 'Ariana Grande',
        'follower_count': 376000000,
        'description': 'Singer'
    },
    {
        'name': 'Miley Cyrus',
        'follower_count': 196000000,
        'description': 'Singer'
    },
    {
        'name': 'Ellen DeGeneres',
        'follower_count': 199000000,
        'description': 'Comedian'
    }
]
score = 0
game_over = False
while not game_over:
    r_word1, r_word2 = random.sample(data,2)

    print("Wlecome to Highe Lower Game")
    print("First statement A:")
    print(r_word1['name'],r_word1['description'])
    print("v/s")
    print("Second statement B:")
    print(r_word2['name'],r_word2['description'])

    user_choice =str(input("Enter your guess Which statement have higher follower A or B : ")).lower()

    if user_choice == 'a':
        user_choice = r_word1
        if user_choice['follower_count'] > r_word2['follower_count']:
            score+=1
            print(f"your guess is correct, and your score is {score} ")
        else :
            print(f"your guess is wrong, your final score is {score}")
            game_over = True 
    elif user_choice == 'b':
        user_choice = r_word2
        if user_choice['follower_count'] > r_word1['follower_count']:
            score+=1
            print(f"your guess is correct, and your score is {score} ")
        else :
            print(f"your guess is wrong, your final score is {score}")
            game_over = True
    else:
        print("Enter the correct statement")


