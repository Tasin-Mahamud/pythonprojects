import random

word_List = ["ardvark", "baboon", "camel"]
chosen_word = random.choice(word_List)
print(chosen_word)
stages = ['''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========
''', '''
  +---+
  |   |
      |
      |
      |
      |
=========
''']

lives = 6
end_of_game = False
while(end_of_game is not True):
    user_input = input("Guess a letter from the word \t").lower()
    my_list = []
    for _ in range(len(chosen_word)):
        my_list += "_"


    for position in range(0,len(chosen_word)-1):
        letter = chosen_word[position]
        if(letter == user_input):
            my_list[position] = user_input
    print(my_list)

    if(user_input  not in chosen_word):
        lives -= 1
        if(lives == 0):
            end_of_game = True
            print("YOU'VE LOST")


    if("_" not in my_list):
        end_of_game = True
        print("YOU'VE WON !!!!")

    print(stages[lives])





